# If you want to define a custom DAG, create
# a new file under plugins/airflow/dags/ and Airflow
# will pick it up automatically.

import json
import logging
import os
import subprocess
from collections.abc import Iterable

from airflow import DAG

try:
    from airflow.operators.bash_operator import BashOperator
except ImportError:
    from airflow.operators.bash import BashOperator

from datetime import datetime, timedelta
from pathlib import Path

logger = logging.getLogger(__name__)

DEFAULT_ARGS = {
    "owner": "airflow",
    "depends_on_past": False,
    "email_on_failure": False,
    "email_on_retry": False,
    "catchup": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
    "concurrency": 1,
}

DEFAULT_TAGS = ["meltano"]
PROJECT_ROOT = os.getenv("MELTANO_PROJECT_ROOT", os.getcwd())
MELTANO_BIN = ".meltano/run/bin"

if not Path(PROJECT_ROOT).joinpath(MELTANO_BIN).exists():
    logger.warning(
        f"A symlink to the 'meltano' executable could not be found at '{MELTANO_BIN}'. Falling back on expecting it "
        f"to be in the PATH instead. "
    )
    MELTANO_BIN = "meltano"


def _meltano_elt_generator(schedules):
    """Generate singular dag's for each legacy Meltano elt task.

    Args:
        schedules (list): List of Meltano schedules.
    """
    for schedule in schedules:
        logger.info(f"Considering schedule '{schedule['name']}': {schedule}")
        if not schedule["cron_interval"]:
            logger.info(
                f"No DAG created for schedule '{schedule['name']}' because its interval is set to `@once`.",
            )
            continue

        args = DEFAULT_ARGS.copy()
        if schedule["start_date"]:
            args["start_date"] = schedule["start_date"]

        dag_id = f"meltano_{schedule['name']}"

        tags = DEFAULT_TAGS.copy()
        if schedule["extractor"]:
            tags.append(schedule["extractor"])
        if schedule["loader"]:
            tags.append(schedule["loader"])
        if schedule["transform"] == "run":
            tags.append("transform")
        elif schedule["transform"] == "only":
            tags.append("transform-only")

        # from https://airflow.apache.org/docs/stable/scheduler.html#backfill-and-catchup
        #
        # It is crucial to set `catchup` to False so that Airflow only create a single job
        # at the tail end of date window we want to extract data.
        #
        # Because our extractors do not support date-window extraction, it serves no
        # purpose to enqueue date-chunked jobs for complete extraction window.
        dag = DAG(
            dag_id,
            tags=tags,
            catchup=False,
            default_args=args,
            schedule_interval=schedule["interval"],
            max_active_runs=1,
        )

        elt = BashOperator(
            task_id="extract_load",
            bash_command=f"cd {PROJECT_ROOT}; {MELTANO_BIN} schedule run {schedule['name']}",
            dag=dag,
        )

        # register the dag
        globals()[dag_id] = dag
        logger.info(f"DAG created for schedule '{schedule['name']}'")


def _meltano_job_generator(schedules):
    """Generate dag's for each task within a Meltano scheduled job.

    Args:
        schedules (list): List of Meltano scheduled jobs.
    """
    for schedule in schedules:
        if not schedule.get("job"):
            logger.info(
                f"No DAG's created for schedule '{schedule['name']}'. It was passed to job generator but has no job."
            )
            continue
        if not schedule["cron_interval"]:
            logger.info(
                f"No DAG created for schedule '{schedule['name']}' because its interval is set to `@once`."
            )
            continue

        base_id = f"meltano_{schedule['name']}_{schedule['job']['name']}"
        common_tags = DEFAULT_TAGS.copy()
        common_tags.append(f"schedule:{schedule['name']}")
        common_tags.append(f"job:{schedule['job']['name']}")
        interval = schedule["cron_interval"]
        args = DEFAULT_ARGS.copy()
        args["start_date"] = schedule.get("start_date", datetime(1970, 1, 1, 0, 0, 0))

        with DAG(
            base_id,
            tags=common_tags,
            catchup=False,
            default_args=args,
            schedule_interval=interval,
            max_active_runs=1,
        ) as dag:
            previous_task = None
            for idx, task in enumerate(schedule["job"]["tasks"]):
                logger.info(
                    f"Considering task '{task}' of schedule '{schedule['name']}': {schedule}"
                )

                task_id = f"{base_id}_task{idx}"

                if isinstance(task, Iterable) and not isinstance(task, str):
                    run_args = " ".join(task)
                else:
                    run_args = task

                task = BashOperator(
                    task_id=task_id,
                    bash_command=f"cd {PROJECT_ROOT}; {MELTANO_BIN} run {run_args}",
                    dag=dag,
                )
                if previous_task:
                    task.set_upstream(previous_task)
                previous_task = task
                logger.info(
                    f"Spun off task '{task}' of schedule '{schedule['name']}': {schedule}"
                )

        globals()[base_id] = dag
        logger.info(f"DAG created for schedule '{schedule['name']}', task='{run_args}'")


def create_dags():
    """Create DAGs for Meltano schedules."""
    list_result = subprocess.run(
        [MELTANO_BIN, "schedule", "list", "--format=json"],
        cwd=PROJECT_ROOT,
        stdout=subprocess.PIPE,
        universal_newlines=True,
        check=True,
    )
    schedule_export = json.loads(list_result.stdout)

    if schedule_export.get("schedules"):
        logger.info(f"Received meltano v2 style schedule export: {schedule_export}")
        _meltano_elt_generator(schedule_export["schedules"].get("elt"))
        _meltano_job_generator(schedule_export["schedules"].get("job"))
    else:
        logger.info(f"Received meltano v1 style schedule export: {schedule_export}")
        _meltano_elt_generator(schedule_export)


create_dags()

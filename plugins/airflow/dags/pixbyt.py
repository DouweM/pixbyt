import os
import yaml
import logging
from datetime import datetime, timedelta
from pathlib import Path

from airflow import DAG
from airflow.operators.bash import BashOperator

logger = logging.getLogger(__name__)

DEFAULT_DAG_OPTS = {
    "catchup": False,
    "max_active_runs": 1,
    "default_args": {
        "owner": "airflow",
        "depends_on_past": False,
        "email_on_failure": False,
        "email_on_retry": False,
        "catchup": False,
        "retries": 1,
        "retry_delay": timedelta(minutes=5),
        "concurrency": 1,
        "start_date": datetime(1970, 1, 1, 0, 0, 0),
    }
}
DEFAULT_SCHEDULE = "*/15 * * * *"

PROJECT_ROOT = os.getenv("MELTANO_PROJECT_ROOT", os.getcwd())
MELTANO_EXECUTABLE = ".meltano/run/bin"
APPS_FILENAME = "apps.yml"

apps_path = Path(PROJECT_ROOT).joinpath(APPS_FILENAME)
apps_config = yaml.safe_load(apps_path.read_text())

if isinstance(apps_config, list):
    apps_config = {"apps": apps_config} # `apps:` is optional
apps = [
    *apps_config.get("apps", []),
    *apps_config.get("schedules", []) # Backwards compatibility with meltano.yml format
]

for app in apps:
    name = app.get("name")

    if not name:
        logger.warning("Skipping app without a name")
        continue

    schedule = (
        app.get("schedule")
        or app.get("interval") # Backwards compatibility with meltano.yml format
        or DEFAULT_SCHEDULE
    )
    job = app.get("job", name)

    env = app.get("env", {}) # Backwards compatibility with meltano.yml format

    devices = app.get("devices", [])
    if devices:
        env["TIDBYT_DEVICE_NAMES"] = str(devices)

    dag_id = name.replace("/", "--")

    with DAG(dag_id, schedule=schedule, **DEFAULT_DAG_OPTS) as dag:
        cmd = f"{MELTANO_EXECUTABLE} run {job}"
        env = {k: str(v) for k, v in env.items()}

        task = BashOperator(
            dag=dag,
            task_id="run",
            cwd=str(PROJECT_ROOT),
            bash_command=cmd,
            env=env,
            append_env=True,
        )
    globals()[dag_id] = dag

    logger.info(f"Created DAG '{dag_id}': schedule='{schedule}', cmd='{cmd}', env={env}")

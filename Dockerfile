ARG MELTANO_IMAGE=meltano/meltano:latest
FROM $MELTANO_IMAGE

WORKDIR /project

ARG TARGETOS=linux
ARG TARGETARCH=amd64

RUN apt-get update

# Install Pixlet
RUN apt-get install -y curl
# TODO: Make this work
# RUN export PIXLET_VERSION=$(curl https://raw.githubusercontent.com/tidbyt/community/main/PIXLET_VERSION | sed 's/v//')
ARG PIXLET_VERSION=0.27.2
RUN echo $PIXLET_VERSION
RUN curl -L -o pixlet.tar.gz https://github.com/tidbyt/pixlet/releases/download/v${PIXLET_VERSION}/pixlet_${PIXLET_VERSION}_${TARGETOS}_${TARGETARCH}.tar.gz
RUN tar -xvf pixlet.tar.gz
RUN chmod +x ./pixlet
RUN mv pixlet /usr/local/bin/pixlet

# Install base Meltano plugins
COPY ./meltano.yml .
COPY ./plugins/ ./plugins/
RUN meltano install

COPY ./apps/ ./apps/

# Install apt packages
RUN cat ./apps/**/apt-packages.txt | sort | uniq > ./apps/apt-packages.txt
RUN xargs -a apps/apt-packages.txt apt-get install -y

# Install Meltano plugins
RUN meltano install

# Copy remaining project files
COPY . .

# Don't allow changes to containerized project files
ENV MELTANO_PROJECT_READONLY 1

ENTRYPOINT ["meltano"]
CMD ["invoke", "airflow", "scheduler"]

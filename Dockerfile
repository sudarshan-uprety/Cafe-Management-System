FROM python:3.8
ENV DockerHome=/home/app/webapp

RUN mkdir -p $DockerHome

WORKDIR $DockerHome

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . $DockerHome

ENTRYPOINT [ "/bin/bash", "docker-entrypoint.sh" ]
FROM python:3.10.7-slim-buster

ENV PYTHONDONTWRITEBYTECODE 1
ENV PIP_ROOT_USER_ACTION=ignore
ENV PYTHONPATH="$PYTHONPATH:/ta_framework"

COPY requirements.txt /tmp/requirements.txt

RUN pip install -r /tmp/requirements.txt

RUN apt-get update && apt-get install -y curl && \
    pip install --upgrade pip

COPY . /ta_framework

RUN chmod +x /ta_framework/wait_for_grid.sh

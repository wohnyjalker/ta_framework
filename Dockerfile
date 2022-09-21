FROM python:3.10.7-slim-buster

ENV PYTHONDONTWRITEBYTECODE 1
ENV PIP_ROOT_USER_ACTION=ignore
ENV PYTHONPATH="$PYTHONPATH:/ta_framework"

COPY requirements.txt /tmp/requirements.txt
COPY . /ta_framework

RUN pip install --upgrade pip && \
    pip install -r /tmp/requirements.txt && \
    chmod +x /ta_framework/wait_for_grid.sh

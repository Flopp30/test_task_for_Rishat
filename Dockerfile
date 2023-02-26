FROM python:3.9-alpine

RUN pip3 install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt && pip install gunicorn

COPY ./market /app

WORKDIR /app

COPY ./entrypoint.sh /
ENTRYPOINT ["sh", "/entrypoint.sh"]

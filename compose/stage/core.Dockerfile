# FROM python:3.6.11
FROM python:3.6.11-alpine3.11
ARG MYSQL_SERVER
ARG POSTGRES_SERVER
ENV ENVTYPE=local
ENV PYTHONUNBUFFERED 1
ENV APP_HOME=/home/app/web
RUN mkdir -p $APP_HOME
WORKDIR $APP_HOME

RUN apk update && apk add --no-cache bash
ADD /compose/scripts/ $APP_HOME
ADD /requirements/$ENVTYPE.txt $APP_HOME
RUN chmod +x db_deps.sh

RUN ./db_deps.sh
RUN python -m pip install --upgrade pip
RUN pip install -r /home/app/web/$ENVTYPE.txt --use-feature=2020-resolver; mkdir /log;

COPY /src/ $APP_HOME
CMD ["uvicorn", "main:app","--reload", "--host", "0.0.0.0", "--port", "8080"]
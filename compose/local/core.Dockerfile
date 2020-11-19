# FROM python:3.6.11
FROM python:3.6.11-alpine3.11
ENV ENVTYPE=local
ENV PYTHONUNBUFFERED 1
ENV APP_HOME=/home/app/web
RUN mkdir -p $APP_HOME
WORKDIR $APP_HOME
# postgres depends   
# apk update && apk add postgresql-dev gcc make \
# python3-dev musl-dev ; \

RUN apk update && apk add --no-cache mariadb-dev build-base gcc make python3-dev libffi-dev
ADD /requirements/$ENVTYPE.txt $APP_HOME
RUN pip install -r /home/app/web/$ENVTYPE.txt; mkdir /log;
COPY /src/ $APP_HOME
CMD ["uvicorn", "main:app","--reload", "--host", "0.0.0.0", "--port", "8080"]
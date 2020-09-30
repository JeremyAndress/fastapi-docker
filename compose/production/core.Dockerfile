# FROM python:3.6.11
FROM python:3.6.11-alpine3.11
ENV ENVTYPE=production
ENV PYTHONUNBUFFERED 1
ENV https_proxy=http://10.46.0.210:3128
ENV http_proxy=http://10.46.0.210:3128
ENV APP_HOME=/home/app/web
RUN mkdir -p $APP_HOME
WORKDIR $APP_HOME

RUN apk update && apk add --no-cache mariadb-dev build-base gcc make python3-dev
ADD /requirements/$ENVTYPE.txt $APP_HOME
RUN pip install -r /home/app/web/$ENVTYPE.txt; mkdir /log;
COPY /src/ $APP_HOME
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
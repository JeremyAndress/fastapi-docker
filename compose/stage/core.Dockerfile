# FROM python:3.6.11
FROM python:3.6.11-alpine3.11
ENV ENVTYPE=local
ENV PYTHONUNBUFFERED 1
ENV APP_HOME=/home/app/web
RUN mkdir -p $APP_HOME
WORKDIR $APP_HOME
ADD /requirements/$ENVTYPE.txt $APP_HOME
# postgres depends   
# apk update && apk add postgresql-dev gcc make \
# python3-dev musl-dev ; \

RUN export https_proxy=http://10.46.0.210:3128; \
    export http_proxy=http://10.46.0.210:3128; \
    apk update && apk add --no-cache mariadb-dev \
    build-base gcc make python3-dev libffi-dev ; \
    pip install -r /home/app/web/$ENVTYPE.txt; mkdir /log; \
    unset https_proxy; \
    unset http_proxy

COPY /src/ $APP_HOME
CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "8080"]
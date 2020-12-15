# FROM python:3.6.11
FROM python:3.6.11-alpine3.11
ARG MYSQL_SERVER
ARG POSTGRES_SERVER
ENV ENVTYPE=local
ENV PYTHONUNBUFFERED 1
ENV APP_HOME=/home/app/web
RUN mkdir -p $APP_HOME
WORKDIR $APP_HOME

ADD /compose/scripts.sh $APP_HOME
ADD /requirements/$ENVTYPE.txt $APP_HOME
RUN chmod +x scripts.sh

RUN export https_proxy=http://10.46.0.210:3128; \
    export http_proxy=http://10.46.0.210:3128; \
    ./scripts.sh; \
    pip install -r /home/app/web/$ENVTYPE.txt; mkdir /log; \
    unset https_proxy; \
    unset http_proxy
    
COPY /src/ $APP_HOME
CMD ["uvicorn", "main:app","--reload", "--host", "0.0.0.0", "--port", "8080"]

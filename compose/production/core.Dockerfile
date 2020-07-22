FROM python:3.6
ENV ENVTYPE=production
ENV PYTHONUNBUFFERED 1
ENV APP_HOME=/home/app/web
RUN mkdir -p $APP_HOME
WORKDIR $APP_HOME

ADD /requirements/$ENVTYPE.txt $APP_HOME

RUN pip install -r /home/app/web/$ENVTYPE.txt; mkdir /log;
COPY /src/ $APP_HOME
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
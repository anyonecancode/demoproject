FROM python:3-alpine
WORKDIR /usr/src/app
ENV FLASK_APP=brewnotes.py
RUN apk add --no-cache build-base && apk add --no-cache mariadb-connector-c-dev
RUN pip install flask==1.0.2
RUN pip install flask-sqlalchemy==2.3.1
RUN pip install flask-migrate==2.3.0
RUN pip install mysqlclient==1.3.13

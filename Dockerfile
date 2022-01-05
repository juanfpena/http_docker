FROM python:3.9-slim-buster
WORKDIR /app/sqlchallenge
RUN apt-get update
RUN apt-get install libssl-dev
RUN apt-get install -y default-libmysqlclient-dev python3-mysqldb
COPY requirements.txt /app/sqlchallenge/requirements.txt
RUN python -m pip install -r requirements.txt
ADD . /app/sqlchallenge/
RUN python setup.py install
EXPOSE 8000
WORKDIR /app
CMD ['gunicorn', '-k', 'uvicorn.workers.UvicornWorker', 'sqlchallenge.app:app', '-b', '0.0.0.0:8000', '--workers=4']
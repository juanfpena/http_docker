FROM python:3.9-slim-buster
WORKDIR /usr/src/sqlchallenge/
RUN apt-get update
RUN apt-get install libssl-dev
# RUN apt-get install -y default-libmysqlclient-dev python3-mysqldb
RUN apt-get install python3-dev default-libmysqlclient-dev build-essential -y
COPY requirements.txt /usr/src/sqlchallenge/
RUN python -m pip install -r requirements.txt
ADD . /usr/src/sqlchallenge/
RUN python setup.py install
EXPOSE 8000
WORKDIR /usr/src/
CMD ["gunicorn", "-k", "uvicorn.workers.UvicornWorker", "sqlchallenge.app:app", "-b", "0.0.0.0:8000", "--workers=4"]
# gunicorn -k uvicorn.workers.UvicornWorker sqlchallenge.app:app -b 0.0.0.0:8000 --workers=4
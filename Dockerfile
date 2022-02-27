FROM python:3.10.1
ENV PYTHONUNBUFFERED 1
RUN mkdir /fileshare
WORKDIR /fileshare
ADD . /fileshare/
RUN pip install -r requirements.txt
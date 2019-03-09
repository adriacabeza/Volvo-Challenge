FROM python:3
ADD . /src
WORKDIR /src
RUN pip3 install -r requirements.txt


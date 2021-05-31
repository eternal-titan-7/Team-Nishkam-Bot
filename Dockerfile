FROM ubuntu:latest

RUN apt update && apt upgrade -y
RUN apt install git curl -y

FROM python:latest

RUN python -m venv env
ENV VIRTUAL_ENV /env
ENV PATH /env/bin:$PATH
RUN pip install -U pip
RUN mkdir /infTeamNishkamApp/
WORKDIR /infTeamNishkamApp/
COPY . /infTeamNishkamApp/
RUN pip install -U -r requirements.txt
CMD python infMain.py
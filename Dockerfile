FROM debian:latest

RUN apt update && apt upgrade -y
RUN apt install git curl python3-pip -y
RUN mkdir /infTeamNishkamApp/
WORKDIR /infTeamNishkamApp/
COPY . /infTeamNishkamApp/
RUN python3 -m venv env
RUN source env/bin/activate
RUN pip3 install -U pip
RUN pip3 install -U -r requirements.txt
CMD python3 infMain.py
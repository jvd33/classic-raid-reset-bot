FROM python:3.8
COPY . /raidresetbot
WORKDIR /raidresetbot
RUN pip install -r requirements.txt
RUN rm requirements.txt

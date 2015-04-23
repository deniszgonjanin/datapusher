FROM python:2.7

ENV PYTHONUNBUFFERED 1
RUN mkdir /source
WORKDIR /source
ADD requirements.txt /source/
RUN pip install -r requirements.txt
ADD . /source/

EXPOSE 8800

CMD python /source/datapusher/main.py /source/deployment/datapusher_settings.py

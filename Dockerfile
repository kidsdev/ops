FROM python:3.7-stretch

RUN apt-get update && apt-get install -y \
  ntp

RUN echo "Asia/Bangkok" > /etc/timezone
RUN dpkg-reconfigure -f noninteractive tzdata

RUN mkdir /code
RUN mkdir /uwsgi

RUN pip install uwsgi
ADD requirements.txt /code

WORKDIR /code/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 80

CMD /etc/init.d/ntp start && uwsgi --emperor /uwsgi

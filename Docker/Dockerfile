FROM python:3.7-alpine
MAINTAINER geekwx@gmail.com
COPY . /app
WORKDIR /app
RUN pip install requests==2.23.0
CMD [ "python", "./app/clima.py" ]
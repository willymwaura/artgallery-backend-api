                                                                        Dockerfile                                                                                  
FROM python:3.8-slim-buster
# set environment variables  
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# install dependencies  
RUN pip install --upgrade pip
# create virtualenv named env and activate it
# instage.py runserver

COPY . .
# port where the Django app runs  

RUN pip install django djangorestframework django-cors-headers gunicorn pillow
RUN pip install --upgrade django


EXPOSE 8000
# start server  
CMD python manage.py migrate && python manage.py runserver 0.0.0.0:8000






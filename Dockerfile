FROM python:3.8
LABEL MAINTAINER="Mohammad Babazadeh | https://boby.cloud"

ENV PYTHONUNBUFFERED 1

# Set working directory
RUN mkdir /blogpy
WORKDIR /blogpy
COPY . /blogpy

# Installing requirements
ADD requirements/requirements.txt /blogpy
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Collect static files
RUN python manage.py collectstatic --no-input

CMD ["gunicorn", "--chdir", "blogpy", "--bind", ":8000", "blogpy.wsgi:application"]

# Pull base image
FROM python:3.7-alpine

# https://stackoverflow.com/a/46204015
RUN apk add python3-dev build-base linux-headers pcre-dev

# Set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /code

# Install dependencies
COPY requirements.txt /code/
RUN pip install -r requirements.txt

# Copy project
COPY . /code/

RUN chmod +x docker-entrypoint.sh

ENTRYPOINT ["/code/docker-entrypoint.sh"]

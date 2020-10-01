FROM python:3.7-slim-buster

ENV PYTHONUNBUFFERED 1
RUN apt-get update \
  # dependencies for building Python packages
  && apt-get install -y build-essential git \
  && apt-get install -y libpq-dev \
  && apt-get install -y gettext \
  && apt-get install -y libsm6 libxext6 libxrender-dev \
  && apt install -y python-tk ghostscript \
  # cleaning up unused files
  && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
  && rm -rf /var/lib/apt/lists/*


COPY ./requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY ./compose/django/start /start
#RUN sed -i 's/\r//' /start
RUN sed -i 's/\r$//g' /start
RUN chmod +x /start

WORKDIR /app


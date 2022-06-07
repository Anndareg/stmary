FROM python:3.9-buster
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DEBUG 0
# copy source and install dependencies
RUN mkdir -p /opt/app
RUN mkdir -p /opt/app/pip_cache
COPY requirements.txt /opt/app/
COPY .pip_cache /opt/app/pip_cache/
COPY . /opt/app/
WORKDIR /opt/app
RUN pip install -r requirements.txt --cache-dir /opt/app/pip_cache
RUN chown -R www-data:www-data /opt/app
EXPOSE 5000
STOPSIGNAL SIGTERM
CMD  gunicorn dmst.wsgi:application --bind 0.0.0.0:5000

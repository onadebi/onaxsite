FROM python:3.10-slim

WORKDIR /app
EXPOSE 5000

#COpy current contents into app directory
COPY . /app

# RUN apt-get install pkg-config
# RUN apt-get install libmysqlclient-dev
# Update package lists and install necessary dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc pkg-config libmariadb-dev-compat && \
    rm -rf /var/lib/apt/lists/*

#Install needed dependencies
RUN pip install --no-cache-dir --trusted-host pypi.python.org -r requirements.txt

RUN pwd

#whitenoise for static files migration in production
RUN python manage.py collectstatic --noinput

# ENTRYPOINT ["flask", "run", "--host=0.0.0.0"]
# ENTRYPOINT ["gunicorn","-b",":5000","main:app"]
ENTRYPOINT [ "python","manage.py","runserver","0.0.0.0:8000" ]

#To use docker-compose down to also delete the image associated with the service, you can add the --rmi all option. Here's the command:
# ```docker-compose down --rmi all```
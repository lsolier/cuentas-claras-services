# core-apicompany/Dockerfile
FROM python:3.10-slim-buster

# Set the working directory
WORKDIR /app

# Arguments
ARG FLASK_ENV
ARG TESTING
ARG FLASK_DEBUG

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Copy the requirements file
COPY requirements.txt /app/src/requirements.txt

# Install the dependencies
RUN apt-get update -y && apt-get install -y && \
    pip3 install --no-cache-dir -r src/requirements.txt --upgrade pip && \
    apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Copy the rest of the application files
COPY . /app/

# Labels
LABEL author="Luis Solier"
LABEL module="cuentas-claras-services"

# Flask environment variables
ENV FLASK_APP="src/app.py"
ENV FLASK_ENV=${FLASK_ENV}
ENV TESTING=${TESTING}
ENV FLASK_DEBUG=${FLASK_DEBUG}
ENV FLASK_APP_NAME="cuentas-claras-services"
ENV PYTHONPATH="./"

# Expose the port the app will run on
EXPOSE 9005

# Run the command to start the app
CMD [ "gunicorn", "-w", "2", "manage:app", "-b", "0.0.0.0:9005", "--log-level", "debug" ]

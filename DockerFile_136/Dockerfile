# Use python:alpine3.7 for the base image
FROM python:alpine3.7

# Copy the .py files in ./app from build's context to /app
COPY ./app/*.py /app/

# Copy the Pipfile in ./app from build's context to /app
COPY ./app/Pipfile /app/

# Change the working directory to /app with WORKDIR
WORKDIR /app

# Install bind-tools - alpine uses 'apk' packet manager
RUN /sbin/apk add bind-tools

# Install pipenv
RUN pip install pipenv

# Install the environment
RUN pipenv run pip install --upgrade pip
RUN pipenv install

# Expose port 8080
EXPOSE 8080

# Start the python application
CMD pipenv run python3.7 myapp.py
# our base image
FROM python:3.8-slim-buster

# Install python and pip
WORKDIR /app
# install Python modules needed by the Python app
COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

# copy files required for the app to run
COPY . .

COPY templates/main.html /app/templates/

# tell the port number the container should expose
EXPOSE 5000

# run the application
CMD [ "python", "/app/main.py"]

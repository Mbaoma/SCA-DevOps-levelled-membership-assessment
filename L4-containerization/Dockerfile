# our base image
FROM python:3.6

# create working directory
WORKDIR /app

# Install any needed packages specified in requirements.txt
COPY requirements.txt /app
RUN pip install -r requirements.txt

# Run main.py when the container launches
COPY main.py /app

# tell the port number the container should expose
EXPOSE 5000

ENTRYPOINT [ "python" ]
# run the application
CMD ["main.py"]
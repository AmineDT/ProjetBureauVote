# Use the official Python base image
FROM python:3.9

# Install netcat
RUN apt-get update && apt-get install -y netcat

# Set the working directory
WORKDIR /app/backend

# Copy the requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install -r requirements.txt

# Copy the project files
COPY . .

# Set the command to run the server
CMD python manage.py runserver 0.0.0.0:8000

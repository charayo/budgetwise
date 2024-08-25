FROM mcr.microsoft.com/devcontainers/python:1-3.11-bookworm

ENV PYTHONUNBUFFERED 1

# RUN apt-get update && apt-get install -y portaudio19-dev && rm -rf /var/lib/apt/lists/*

# set environment variables


# Set the working directory in the container
WORKDIR /app


# Copy the requirements file into the container at /app
COPY requirements.txt /app/


# COPY . .

RUN pip install -r requirements.txt

# Copy the rest of the application code into the container at /app
COPY . /app

# Make port 80 and 8000 available to the world outside this container
EXPOSE 80

# Run uvicorn server
CMD ["uvicorn", "server.budgetwise.api.api:app", "--host", "0.0.0.0", "--port", "9000"]

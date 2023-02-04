# The FROM instruction specifies the Parent Image from which you are building
FROM python:3.10-alpine

# Create a new virtual environment
RUN /usr/local/bin/python -m venv /app/venv

# Copy requirements.txt into container
COPY requirements.txt /app/venv

# Upgrade pip
RUN /app/venv/bin/python -m pip install --upgrade pip

# Install dependancies
RUN /app/venv/bin/pip install -r /app/venv/requirements.txt

# Set working directory
WORKDIR /app

# Copy files into container
COPY . /app

# Add /app/venv/bin to the path
ENV PATH="/app/venv/bin:${PATH}"

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

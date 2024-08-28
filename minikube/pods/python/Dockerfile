# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the hello.py file into the container at /app
COPY hello.py /app/

# Install Flask
RUN pip install --no-cache-dir flask

# Expose port 5000 to the outside world
EXPOSE 5000

# Run hello.py when the container launches
CMD ["python", "hello.py"]

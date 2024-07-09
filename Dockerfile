# Use the official Python image from the Docker Hub as the base image
# 
FROM python:3.9-slim as build

# Set the working directory in the container to /app
#
WORKDIR /api

# Copy the current directory contents into the container at /app
#
COPY ./api .

# Install any needed packages specified in requirements.txt
#
RUN pip install --no-cache-dir -r requirements.txt

ENV PYTHONUNBUFFERED=1


# Prodoction stage
FROM python:3.9-slim as production

# Set the working directory in the container to /app
#
WORKDIR /api

# Copy installed dependencies
#
COPY --from=build /usr/local/lib/python3.9/site-packages /usr/local/lib/python3.9/site-packages
COPY --from=build /usr/local/bin /usr/local/bin

# Copy the current directory contents into the container at /app
#
COPY ./api .

# Make port 5000 available to the world outside this container
#
EXPOSE 5000

# Define environment variable
#
ENV MINIO_ACCESS_KEY=access-key
ENV MINIO_SECRET_KEY=secret-key
ENV PYTHONUNBUFFERED=1

# Run app.py when the container launches
#
CMD ["python", "app.py"]

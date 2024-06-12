# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Install git and other dependencies
RUN apt-get update && apt-get install -y git && apt-get clean

# Set environment variable for GitHub token (if using a private repo)
ARG GITHUB_TOKEN

# Clone the repository using the token (replace with your repository URL)
RUN git clone https://$GITHUB_TOKEN@github.com/2soum/ApiCrimson.git .

# Change the working directory to the cloned repository
WORKDIR /app/ApiCrimson

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port the app runs on
EXPOSE 5000

# Run the application
CMD ["gunicorn", "-b", "0.0.0.0:5000", "run:app"]

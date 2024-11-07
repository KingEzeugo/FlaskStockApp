FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy all files to /app in the container
COPY . /app

# Install dependencies
RUN pip install -r requirements.txt

# Expose Flask's port
EXPOSE 5000

# Run the Flask app
CMD ["python", "project.py"]

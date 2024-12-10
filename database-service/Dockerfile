# Use Python as base image
FROM python:3.10

# Set the working directory
WORKDIR /app

# Copy the necessary files
COPY . .

# Install dependencies
RUN pip install -r requirements.txt

# Expose port
EXPOSE 5000

# Command to start the server
CMD ["python", "app.py"]

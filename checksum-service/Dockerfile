# Use Python 3.9 base image
# TODO : broken in 3.10 ?
FROM python:3.9

# Set the working directory
WORKDIR /app

# Copy dependencies and install them
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .

# Expose the service port
EXPOSE 5001

# Command to run the service
CMD ["python", "app.py"]

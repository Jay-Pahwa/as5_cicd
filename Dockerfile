# Start with a lightweight official Python image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the dependencies file and install them
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application code into the container
COPY . .

# Tell Docker that the container listens on port 5000
EXPOSE 5000

# The command to run your application when the container starts
CMD ["python3", "app.py"]

# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set a working directory inside the container
WORKDIR /app

# Copy the requirements file to the working directory
COPY requirements.txt .

# Install the required Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code to the working directory
COPY . .

# Expose the port that the application will run on (e.g., Flask uses 5000 by default)
EXPOSE 5000

# Specify the command to run your consumer forecasting app
CMD ["python", "train_model.py"]

# Define the base image to build from
FROM python:3.11-slim-buster

# Set the working directory for the app
WORKDIR /app

# Copy the requirements file to the working directory and install the requirements
COPY app/requirements.txt .
RUN pip install -r requirements.txt

# Copy the app to the working directory
COPY ./app .

# Expose the port the app will run on
EXPOSE 8000

# Run the app
# CMD ["uvicorn", "app.main:app", "--host", "8000", "--reload"]

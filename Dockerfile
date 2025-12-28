# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy requirements.txt first to leverage Docker cache
COPY requirements.txt ./

# Install dependencies
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY src/ ./src/
COPY src/xgb_model.pkl ./src/xgb_model.pkl

# Expose the port FastAPI will run on
EXPOSE 8000

# Set environment variables (optional, for production best practices)
ENV PYTHONUNBUFFERED=1
# Run the FastAPI app with uvicorn
CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "8000"]

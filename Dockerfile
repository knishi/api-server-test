FROM python:3.10-slim

# Create a non-root user
RUN groupadd -r myapi && useradd -r -g myapi myapi

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Change ownership to non-root user
RUN chown -R myapi:myapi /app

# Switch to non-root user
USER myapi

# Expose port
EXPOSE 8080

# Command to run the application
CMD ["gunicorn", "-b", "0.0.0.0:8080", "app:app"]

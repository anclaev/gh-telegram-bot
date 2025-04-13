FROM python:3.10.17-slim

# Set the working directory
WORKDIR /app

# Copy only the necessary files
COPY requirements.txt .
COPY bot.py .
COPY main.py .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port (optional, for debugging)
EXPOSE 8080

# Run the bot
CMD ["python3", "main.py"]
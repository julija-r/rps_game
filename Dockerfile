FROM python:3.11-slim

# Setting working directory in container
WORKDIR /app

# Copying code
COPY . /app

# Installing requirements
RUN pip install --no-cache-dir -r requirements.txt

# Expose port then Flask will use
EXPOSE 5000

# Running the script
CMD ["python", "rps_game.py"]

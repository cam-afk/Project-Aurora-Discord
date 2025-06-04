# 1. Use a lightweight Python base image
FROM python:3.9-slim

# 2. Set the working directory
WORKDIR /app

# 3. Copy required files
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# 4. Copy the rest of the bot's code into the image
COPY . .

# 5. Set the command to run your bot
CMD ["python", "bot/main.py"]


FROM python:3.11-slim-buster
WORKDIR /app
COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

# Expose the port the app runs on
EXPOSE 5000

# Define environment variable for Flask
ENV FLASK_APP=app.py

CMD ["python3", "app.py"]
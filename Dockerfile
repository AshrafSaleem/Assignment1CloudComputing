FROM python:3.9-slim

COPY requirements.txt ./
RUN apt-get update -y
RUN apt install libgl1-mesa-glx -y
RUN apt-get install 'ffmpeg'\
    'libsm6'\
    'libxext6'  -y
RUN pip install --no-cache-dir -r requirements.txt

COPY main.py object_detection.py /app/
COPY yolo_tiny_configs /app/
WORKDIR /app/
ENTRYPOINT FLASK_APP=/app/main.py flask run --host=0.0.0.0 --port 80

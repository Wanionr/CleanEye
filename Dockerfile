FROM python:3.13.3-slim

WORKDIR /app

RUN apt update && apt install -y libgl1-mesa-glx libglib2.0-0

COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY ./app /app

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
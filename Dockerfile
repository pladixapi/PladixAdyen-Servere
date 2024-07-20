FROM python:3.11-alpine

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

ENV PORT=80
EXPOSE 80
CMD ["python3", "app.py"]

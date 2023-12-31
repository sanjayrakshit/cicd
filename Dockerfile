FROM python:3.10.12-alpine3.18

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

CMD ["python", "-u",  "serving/src/flask_app.py"]
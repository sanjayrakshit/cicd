FROM python:3.10.12-alpine3.18

WORKDIR /sanjay

COPY . .

RUN pip install -r requirements.txt

CMD ["python", "serving/src/flask_app.py"]
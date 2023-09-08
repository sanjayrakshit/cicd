FROM python:3.10.12-alpine3.18

WORKDIR /sanjay

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY serving serving

EXPOSE 5010
ENTRYPOINT ["python", "serving/src/flask_app.py"]
FROM python:3.9-alpine

WORKDIR .

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

EXPOSE 6666

COPY . .
ENTRYPOINT ["python", "app/udaconnect/consumer.py"]
import os

DB_USERNAME = os.environ["DB_USERNAME"]
DB_PASSWORD = os.environ["DB_PASSWORD"]
DB_HOST = os.environ["DB_HOST"]
DB_PORT = os.environ["DB_PORT"]
DB_NAME = os.environ["DB_NAME"]

KAFKA_TOPIC = 'Location'
KAFKA_SERVER = "my-cluster-kafka-bootstrap.kafka.svc.cluster.local:9092"

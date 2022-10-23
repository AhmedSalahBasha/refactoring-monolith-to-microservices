from kafka import KafkaConsumer
import os
import logging
import json
import psycopg2
import config

consumer = KafkaConsumer(
    config.KAFKA_TOPIC,
    api_version=(0, 10, 1),
    bootstrap_servers=config.KAFKA_SERVER,
)


def add_location_to_db(location):
    conn = psycopg2.connect(
        dbname=config.DB_NAME,
        port=config.DB_PORT,
        user=config.DB_USERNAME,
        password=config.DB_PASSWORD,
        host=config.DB_HOST,
    )
    query = "INSERT INTO location (person_id, coordinate) VALUES ({}, ST_Point({}, {}));".format(
        int(location["person_id"]),
        float(location["latitude"]),
        float(location["longitude"]),
    )

    cur = conn.cursor()
    cur.execute(query)
    conn.commit()
    cur.close()
    conn.close()
    print("Location is added successfully to the database!")


def consume_locations():
    for message in consumer:
        print("Location message received: {}".format(message))
        decoded_message = message.value.decode("utf-8")
        location = json.loads(decoded_message)
        add_location_to_db(location)


if __name__ == "__main__":
    consume_locations()

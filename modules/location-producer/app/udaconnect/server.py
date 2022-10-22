import location_pb2
import location_pb2_grpc
import json
import grpc
from concurrent import futures
from kafka import KafkaProducer


producer = KafkaProducer(bootstrap_servers="my-cluster-kafka-bootstrap.kafka.svc.cluster.local:9092",
                         value_serializer=lambda v: json.dumps(v).encode('utf-8'),
                         api_version=(0, 10, 2)
                         )


class LocationServicer(location_pb2_grpc.LocationServiceServicer):
    def Create(self, request, context):
        location = {
            "person_id": int(request.person_id),
            "latitude": float(request.latitude),
            "longitude": float(request.longitude),
        }
        publish_message(message=location)
        return location_pb2.LocationMessage(**location)


def publish_message(message):
    request = json.dumps(message).encode()
    producer.send("Location", request)
    producer.flush()


def run_grpc_server():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    location_pb2_grpc.add_LocationServiceServicer_to_server(LocationServicer(), server)
    server.add_insecure_port("[::]:5005")
    server.start()
    keep_server_alive(server)


def keep_server_alive(server, sleep_sec=86400):
    try:
        while True:
            time.sleep(sleep_sec)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == "__main__":
    logging.basicConfig()
    run_grpc_server()


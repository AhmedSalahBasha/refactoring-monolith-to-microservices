import grpc
import location_pb2
import location_pb2_grpc


print("Sending sample payload using gRPC...")

channel = grpc.insecure_channel("localhost:30007")
stub = location_pb2_grpc.LocationServiceStub(channel)

location = location_pb2.LocationMessage(
    person_id=1,
    latitude=52.52,
    longitude=13.40
)

response = stub.Create(location)


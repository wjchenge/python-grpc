from concurrent import futures
import grpc

import demo_service_pb2_grpc
from demo.demo_service_impl import DemoService


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    demo_service_pb2_grpc.add_DemoServiceServicer_to_server(
        DemoService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
from __future__ import print_function


import grpc

import demo_service_pb2
import demo_service_pb2_grpc


def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = demo_service_pb2_grpc.DemoServiceStub(channel)
        response = stub.SayHello(demo_service_pb2.DemoRequest(name=" word !!!!!!!!!!!!!!!!!!!!!"))
        print("Received message %s" %response.message)


if __name__ == '__main__':
    run()
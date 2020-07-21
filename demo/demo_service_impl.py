import demo_service_pb2
import demo_service_pb2_grpc

class DemoService(demo_service_pb2_grpc.DemoServiceServicer):
    def SayHello(self, request, context):
        return demo_service_pb2.HelloReply(message='python--hello {msg}'.format(msg=request.name))


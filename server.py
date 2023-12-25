import grpc
import base64
from concurrent import futures
import captcha_pb2
import captcha_pb2_grpc
import easyocr
reader = easyocr.Reader(['en']) # this needs to run only once to load the model into memory


class CaptchaDecoderServicer(captcha_pb2_grpc.CaptchaDecoderServicer):
        def Base64ToText(self, request, context):
            # Implement your logic here to decode base64 and return text
            base64_data = request.base64_data
            
            binary_data = base64.b64decode(base64_data)
            result = reader.readtext(binary_data)
            print(result);
            text_data = result[0][-2]
            print(text_data)
            # text_data = "Decoded Text: " + text_data
            return captcha_pb2.Base64Output(text_data=text_data)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    captcha_pb2_grpc.add_CaptchaDecoderServicer_to_server(CaptchaDecoderServicer(), server)
    server.add_insecure_port('[::]:50051')
    print("Server started on port 50051")
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()

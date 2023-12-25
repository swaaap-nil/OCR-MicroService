# OCR-Microservice

Decode captchas as a microservice without any language constraints. Thanks to gRPC !
It accepts a image as a base64 encoded string -> converts it into a binary -> runs an AI model to detect the text in the image -> returns the response to the client

## Table of Contents

- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)

## Getting Started

Explain how to get started with your project. Provide instructions on how to install dependencies and set up the environment.

### Dependencies

The service uses easyOCR from JaidedAI to decode the captcha. Drop them a star at https://github.com/JaidedAI/EasyOCR

### Installation steps
```bash
# clone the repository
git clone https://github.com/yourusername/OCR-MicroService.git
# change the working directory
cd OCR-MicroService
# installing all the prerequistes
pip install -r requirements.txt
```

### Setting up the server

once in the correct working directory, run server.py using the following command:

```bash
python3 server.py
```

NOTE: The initial boot of model takes time to load into the memory. once loaded and live, it is pretty fast. So a rule of thumb would be to keep the model in the memory for fast responses.
you should see: 

```bash
Server started on port 50051
```

### Setting up the client 

The beauty (and one of the reasons of using) gRPC is that client can be written in any language of your choice. You will be required to create gRPC files using captcha.proto file according to your client side language.
You can easily figure out with a little bit of googling. I will be showing a sample Python client

Use the .proto file to create required protocol buffers code :

```bash
  python3 -m grpc_tools.protoc -I./ --python_out=. --pyi_out=. --grpc_python_out=. ./captcha.proto
```

```bash -I./ ``` Specifies the directory where the Protocol Buffers compiler should look for the captcha.proto file and its dependencies. In this case, it looks in the current directory (./).

```bash --python_out=. ``` Specifies the output directory for the generated Python files. In this case, it's set to the current directory (.).

```bash --pyi_out=. ``` Specifies the output directory for the generated Python interface files (.pyi). Interface files are used for static type checking in tools like MyPy. Here, it's set to the current directory.

```bash --grpc_python_out=. ``` Specifies the output directory for the generated gRPC Python files. It is used to generate code that supports gRPC communication. The current directory (.) is used here as well.

```bash ./captcha.proto ``` This is the path to the Protocol Buffers file (captcha.proto) that will be used as input to the protoc compiler. The file is located in the current directory.

Now we can write the client app using the three generated files :

![Sample Image](https://github.com/swaaap-nil/OCR-MicroService/blob/main/sample-py-client/images/1.png)

```python
import grpc
import captcha_pb2
import captcha_pb2_grpc

def run():
    # Connect to the gRPC server
    with grpc.insecure_channel('localhost:50051') as channel:
        # Create a stub (client)
        stub = captcha_pb2_grpc.CaptchaDecoderStub(channel)

        # Replace the following base64_string with your actual base64-encoded image data
        base64_string = 'iVBORw0KGgoAAAANSUhEUgAAAMsAAAAyCAYAAADyZi/iAAAF3ElEQVR42u1cYWRdSRSuqKh6SkVUxQqVH9Ufq8Raq2ItsSpWxKNirVprWVWrqpaoFWvFEhVVq0JFRVSFempVVah4VjwrPBVRq0qtqFpRalVFVHg7w3mM0zP3ztw3c9909/sYkpk5Z+bde74755yZe/ftAwAAAAAAAAAAAAAAAAAAAID/N1oMEcfpUeWsKndU2VJlR5W9MsYG/lsGu8xsdleVIU8dx0nOxO0UyEJze9LKgSD3lHX5zHPcB0x+zVP+Uyb/DNbafbL0qfKywxu7zuS3td5uk0WprNBK0ipAlkXWZdpzJXvL5PVKtt9DxzSTX4K1pkGYLwX7OecoOyXITqTghimVP7Ih/lJlVJVeB9lJJvvQY9wRCyfHPHSsMNlJWGo6hLnHbs5rVQZyZIbI//dyv0okS72oK6X6HmGyeqXocZS9zNzaNmY6WJmOwErTIctRIoiJezkyjSLuV4lkecOG6PGULxS3qH73zYeH8feqo/woG/cJLDQ9wnwnuA6Tlr4Xi7pfJZKlo4yXErnJpviT46pgriaDvquTHoeNexPWWQ4BTlPGa8u4ibserss7q0Wn7leJZGl1SJYzTMWqg8wpo/9jqtvwWZ30OGzcKiw5olGQz123BJpZZDkmEGGJ9VnrxP0qaszCE7eNCzadRTJhhq5+IW7Z75HwWKC6665ZNa2fr4hFri3gaHSUDn6aYR+7Ofp+EGQ+p7YLQls1FMkz+s4L477lbmJIspC+P6Xr4JgoOUN1VaNuxcETaPHVCYhHlpqRiflFlZNtX5k26RYddDaFtOuHwqqzHNNNoidtTfiNryWXJgJZbrDuMznxinl9+qn+sGvcQvfLxDwsPC5ZNF6pMtyBzhOCO7ATwv1yJQttKq4Kv23b5beFiInYqqBRz+j7sS2DxVaokQwdvyNeKZ8sEwH0Tuc8lKsh5y3EC4+EMXWiYrCsBAJbFTLjFlV/yei3yNoWjLbLHvHKYVh4XLI0A+nVbsVjC1GWQ8/bqB8kt49jo+3alJltU6KbLjvxqv6uLeXOTgT8ZpEfY+Nswrrjk+ViQN3DFhevLwZZKL7aFsbU7smhbqSmWTZLY9bSz3RTj7I280TAjkV+lo1zHdYdnywjAXVPWVaWT2LMW5V/hPq7Lue5IpKlmnfQlD1Unln0mBnKj4T2RmhXGsg3ut5AeoeEo/dt6Bt/IPC8pbFuxMy2Oeo5lHeCmKXUlyx6lmyrv75nLF7Z811JgRKNQtC7lhPgX4uQmCh0LD72dWG78BpfsPaawxEhM26psbZxpv8RLPs9IYtl87Ep1J2KRBa9clUSIsuvTN0V1m4e2hyw6BiwxS3q/6shH0RASWShbBQ/sVun7NimsFlZiUCWFu2xHEiELDxuaRhtJ83rkaPHfBlt2KjnD6JxWPb7QZaHTOWb9t4G7eLvhdhlFsghnWVb8XnDMCJZKkLc0ktt37u+0ajabxl9z1PdQSFeOQjLTpwslmP651mfn4U+owHIUrHESQ+KECbCQ6QpxS0sXvkqR8dZo+8dqptgetdh1YmTxfICWF3oJ7ljW77umGWfRRPmDyl9nABZrjGVV6nevGaDOTqOmftVlnhoDladPlnu29wvoa/kji2EmDcdMVnv9NRABLK8swLQdWjjuaOeF4bMibxMG5AYWZh7ILpfgozkjp0OMW8izIag/1YXySLFFlO+c2Ofn7pki4WABMlChxZfuZ6uzXHHXrge/nM4ddwvvE/ivIJFSqk3M05if+2o45uMk9wNWHTaZKm5ul+O7thiqHkTYaSP5M13iSxzGanuIUcdxzN0zMKiEyWL8J55rvvl6I6NhZo3JR6kj+XNdYEs4xYj/9tTz0uLHsQrKZKFXj/e9nW/PNyxvlDzJsI8F4xrpmSy9AorqfcHO4TP5np/tRIolyzLRd0vR3fsdsh5qy4fsExS5hmyiGfmGsIcvvXUcU56DQHWDAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGTiXzReCvknNGsEAAAAAElFTkSuQmCC'

        # Create a request with the base64-encoded image
        request = captcha_pb2.Base64Input(base64_data=base64_string)

        # Make the gRPC request
        response = stub.Base64ToText(request)

        # Print the server's response
        print("Server Response:", response.text_data)

if __name__ == '__main__':
    run()

```

on running the script we get response from server :
```bash
rXkfW
```

which is the desired text read from the image

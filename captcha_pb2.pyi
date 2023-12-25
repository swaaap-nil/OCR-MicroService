from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Base64Input(_message.Message):
    __slots__ = ("base64_data",)
    BASE64_DATA_FIELD_NUMBER: _ClassVar[int]
    base64_data: str
    def __init__(self, base64_data: _Optional[str] = ...) -> None: ...

class Base64Output(_message.Message):
    __slots__ = ("text_data",)
    TEXT_DATA_FIELD_NUMBER: _ClassVar[int]
    text_data: str
    def __init__(self, text_data: _Optional[str] = ...) -> None: ...

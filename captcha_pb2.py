# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: captcha.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rcaptcha.proto\x12\x04swap\"\"\n\x0b\x42\x61se64Input\x12\x13\n\x0b\x62\x61se64_data\x18\x01 \x01(\t\"!\n\x0c\x42\x61se64Output\x12\x11\n\ttext_data\x18\x01 \x01(\t2G\n\x0e\x43\x61ptchaDecoder\x12\x35\n\x0c\x42\x61se64ToText\x12\x11.swap.Base64Input\x1a\x12.swap.Base64Outputb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'captcha_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_BASE64INPUT']._serialized_start=23
  _globals['_BASE64INPUT']._serialized_end=57
  _globals['_BASE64OUTPUT']._serialized_start=59
  _globals['_BASE64OUTPUT']._serialized_end=92
  _globals['_CAPTCHADECODER']._serialized_start=94
  _globals['_CAPTCHADECODER']._serialized_end=165
# @@protoc_insertion_point(module_scope)

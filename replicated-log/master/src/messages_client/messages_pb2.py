# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: messages.proto
# Protobuf Python Version: 5.27.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    27,
    2,
    '',
    'messages.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0emessages.proto\x12\x08messages\",\n\rAppendRequest\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0f\n\x07message\x18\x02 \x01(\t\" \n\x0e\x41ppendResponse\x12\x0e\n\x06status\x18\x01 \x01(\t\"\x17\n\x15GetAllMessagesRequest\".\n\x0fMessageResponse\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0f\n\x07message\x18\x02 \x01(\t\"E\n\x16GetAllMessagesResponse\x12+\n\x08messages\x18\x01 \x03(\x0b\x32\x19.messages.MessageResponse\"\r\n\x0bPingRequest\"4\n\x0cPingResponse\x12$\n\x06status\x18\x01 \x01(\x0e\x32\x14.messages.PingStatus*=\n\nPingStatus\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x06\n\x02OK\x10\x01\x12\x0f\n\x0bUNREACHABLE\x10\x02\x12\t\n\x05\x45RROR\x10\x03\x32\xd3\x01\n\x08Messages\x12;\n\x06\x41ppend\x12\x17.messages.AppendRequest\x1a\x18.messages.AppendResponse\x12S\n\x0eGetAllMessages\x12\x1f.messages.GetAllMessagesRequest\x1a .messages.GetAllMessagesResponse\x12\x35\n\x04Ping\x12\x15.messages.PingRequest\x1a\x16.messages.PingResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'messages_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_PINGSTATUS']._serialized_start=321
  _globals['_PINGSTATUS']._serialized_end=382
  _globals['_APPENDREQUEST']._serialized_start=28
  _globals['_APPENDREQUEST']._serialized_end=72
  _globals['_APPENDRESPONSE']._serialized_start=74
  _globals['_APPENDRESPONSE']._serialized_end=106
  _globals['_GETALLMESSAGESREQUEST']._serialized_start=108
  _globals['_GETALLMESSAGESREQUEST']._serialized_end=131
  _globals['_MESSAGERESPONSE']._serialized_start=133
  _globals['_MESSAGERESPONSE']._serialized_end=179
  _globals['_GETALLMESSAGESRESPONSE']._serialized_start=181
  _globals['_GETALLMESSAGESRESPONSE']._serialized_end=250
  _globals['_PINGREQUEST']._serialized_start=252
  _globals['_PINGREQUEST']._serialized_end=265
  _globals['_PINGRESPONSE']._serialized_start=267
  _globals['_PINGRESPONSE']._serialized_end=319
  _globals['_MESSAGES']._serialized_start=385
  _globals['_MESSAGES']._serialized_end=596
# @@protoc_insertion_point(module_scope)
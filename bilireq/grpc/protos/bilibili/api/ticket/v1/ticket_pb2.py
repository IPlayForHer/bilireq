# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: bilireq.grpc.protos.bilibili/api/ticket/v1/ticket.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n#bilibili/api/ticket/v1/ticket.proto\x12\x16\x62ilibili.api.ticket.v1\"\xb7\x01\n\x10GetTicketRequest\x12\x46\n\x07\x63ontext\x18\x01 \x03(\x0b\x32\x35.bilibili.api.ticket.v1.GetTicketRequest.ContextEntry\x12\x0e\n\x06key_id\x18\x02 \x01(\t\x12\x0c\n\x04sign\x18\x03 \x01(\x0c\x12\r\n\x05token\x18\x04 \x01(\t\x1a.\n\x0c\x43ontextEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x0c:\x02\x38\x01\"\xa6\x01\n\x11GetTicketResponse\x12\x0e\n\x06ticket\x18\x01 \x01(\t\x12\x12\n\ncreated_at\x18\x02 \x01(\x03\x12\x0b\n\x03ttl\x18\x03 \x01(\x03\x12\x42\n\x07\x63ontext\x18\x04 \x01(\x0b\x32\x31.bilibili.api.ticket.v1.GetTicketResponse.Context\x1a\x1c\n\x07\x43ontext\x12\x11\n\tv_voucher\x18\x01 \x01(\t2j\n\x06Ticket\x12`\n\tGetTicket\x12(.bilibili.api.ticket.v1.GetTicketRequest\x1a).bilibili.api.ticket.v1.GetTicketResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'bilibili.api.ticket.v1.ticket_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _GETTICKETREQUEST_CONTEXTENTRY._options = None
  _GETTICKETREQUEST_CONTEXTENTRY._serialized_options = b'8\001'
  _globals['_GETTICKETREQUEST']._serialized_start=64
  _globals['_GETTICKETREQUEST']._serialized_end=247
  _globals['_GETTICKETREQUEST_CONTEXTENTRY']._serialized_start=201
  _globals['_GETTICKETREQUEST_CONTEXTENTRY']._serialized_end=247
  _globals['_GETTICKETRESPONSE']._serialized_start=250
  _globals['_GETTICKETRESPONSE']._serialized_end=416
  _globals['_GETTICKETRESPONSE_CONTEXT']._serialized_start=388
  _globals['_GETTICKETRESPONSE_CONTEXT']._serialized_end=416
  _globals['_TICKET']._serialized_start=418
  _globals['_TICKET']._serialized_end=524
# @@protoc_insertion_point(module_scope)
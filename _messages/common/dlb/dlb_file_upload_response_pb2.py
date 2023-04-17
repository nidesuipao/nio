# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: common/dlb/dlb_file_upload_response.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='common/dlb/dlb_file_upload_response.proto',
  package='nio.ad.messages',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n)common/dlb/dlb_file_upload_response.proto\x12\x0fnio.ad.messages\"\xc0\x01\n\x15\x44LBFileUploadResponse\x12\x0c\n\x04uuid\x18\x01 \x01(\t\x12\x36\n\x0cupload_state\x18\x02 \x01(\x0e\x32 .nio.ad.messages.FileUploadState\x12\x1a\n\x0epublish_ptp_ts\x18\xfb\xff\xff\xff\x01 \x01(\x04\x12\x18\n\x0cpublisher_id\x18\xfd\xff\xff\xff\x01 \x01(\t\x12\x13\n\x07\x63ounter\x18\xfe\xff\xff\xff\x01 \x01(\x04\x12\x16\n\npublish_ts\x18\xff\xff\xff\xff\x01 \x01(\x04*[\n\x0f\x46ileUploadState\x12\x18\n\x14UploadFile_SUCCEEDED\x10\x00\x12\x17\n\x13UploadFile_REJECTED\x10\x01\x12\x15\n\x11UploadFile_FAILED\x10\x02')
)

_FILEUPLOADSTATE = _descriptor.EnumDescriptor(
  name='FileUploadState',
  full_name='nio.ad.messages.FileUploadState',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UploadFile_SUCCEEDED', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UploadFile_REJECTED', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UploadFile_FAILED', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=257,
  serialized_end=348,
)
_sym_db.RegisterEnumDescriptor(_FILEUPLOADSTATE)

FileUploadState = enum_type_wrapper.EnumTypeWrapper(_FILEUPLOADSTATE)
UploadFile_SUCCEEDED = 0
UploadFile_REJECTED = 1
UploadFile_FAILED = 2



_DLBFILEUPLOADRESPONSE = _descriptor.Descriptor(
  name='DLBFileUploadResponse',
  full_name='nio.ad.messages.DLBFileUploadResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='uuid', full_name='nio.ad.messages.DLBFileUploadResponse.uuid', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='upload_state', full_name='nio.ad.messages.DLBFileUploadResponse.upload_state', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='publish_ptp_ts', full_name='nio.ad.messages.DLBFileUploadResponse.publish_ptp_ts', index=2,
      number=536870907, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='publisher_id', full_name='nio.ad.messages.DLBFileUploadResponse.publisher_id', index=3,
      number=536870909, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='counter', full_name='nio.ad.messages.DLBFileUploadResponse.counter', index=4,
      number=536870910, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='publish_ts', full_name='nio.ad.messages.DLBFileUploadResponse.publish_ts', index=5,
      number=536870911, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=63,
  serialized_end=255,
)

_DLBFILEUPLOADRESPONSE.fields_by_name['upload_state'].enum_type = _FILEUPLOADSTATE
DESCRIPTOR.message_types_by_name['DLBFileUploadResponse'] = _DLBFILEUPLOADRESPONSE
DESCRIPTOR.enum_types_by_name['FileUploadState'] = _FILEUPLOADSTATE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DLBFileUploadResponse = _reflection.GeneratedProtocolMessageType('DLBFileUploadResponse', (_message.Message,), {
  'DESCRIPTOR' : _DLBFILEUPLOADRESPONSE,
  '__module__' : 'common.dlb.dlb_file_upload_response_pb2'
  # @@protoc_insertion_point(class_scope:nio.ad.messages.DLBFileUploadResponse)
  })
_sym_db.RegisterMessage(DLBFileUploadResponse)


# @@protoc_insertion_point(module_scope)

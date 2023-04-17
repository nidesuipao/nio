# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: common/dlb/dlb_file_download_response.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='common/dlb/dlb_file_download_response.proto',
  package='nio.ad.messages',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n+common/dlb/dlb_file_download_response.proto\x12\x0fnio.ad.messages\"\xb3\x02\n\x17\x44LBFileDownloadResponse\x12\x12\n\ncommand_id\x18\x01 \x01(\x04\x12\x45\n\x06status\x18\x02 \x01(\x0e\x32\x35.nio.ad.messages.DLBFileDownloadResponse.ResultStatus\x12\x13\n\x0b\x66\x61il_reason\x18\x03 \x03(\t\x12\x1a\n\x0epublish_ptp_ts\x18\xfb\xff\xff\xff\x01 \x01(\x04\x12\x18\n\x0cpublisher_id\x18\xfd\xff\xff\xff\x01 \x01(\t\x12\x13\n\x07\x63ounter\x18\xfe\xff\xff\xff\x01 \x01(\x04\x12\x16\n\npublish_ts\x18\xff\xff\xff\xff\x01 \x01(\x04\"E\n\x0cResultStatus\x12\x0b\n\x07SUCCESS\x10\x00\x12\x0b\n\x07\x46\x41ILURE\x10\x01\x12\x0b\n\x07RUNNING\x10\x02\x12\x0e\n\nADDITIONAL\x10\x03')
)



_DLBFILEDOWNLOADRESPONSE_RESULTSTATUS = _descriptor.EnumDescriptor(
  name='ResultStatus',
  full_name='nio.ad.messages.DLBFileDownloadResponse.ResultStatus',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='SUCCESS', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAILURE', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RUNNING', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ADDITIONAL', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=303,
  serialized_end=372,
)
_sym_db.RegisterEnumDescriptor(_DLBFILEDOWNLOADRESPONSE_RESULTSTATUS)


_DLBFILEDOWNLOADRESPONSE = _descriptor.Descriptor(
  name='DLBFileDownloadResponse',
  full_name='nio.ad.messages.DLBFileDownloadResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='command_id', full_name='nio.ad.messages.DLBFileDownloadResponse.command_id', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='nio.ad.messages.DLBFileDownloadResponse.status', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fail_reason', full_name='nio.ad.messages.DLBFileDownloadResponse.fail_reason', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='publish_ptp_ts', full_name='nio.ad.messages.DLBFileDownloadResponse.publish_ptp_ts', index=3,
      number=536870907, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='publisher_id', full_name='nio.ad.messages.DLBFileDownloadResponse.publisher_id', index=4,
      number=536870909, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='counter', full_name='nio.ad.messages.DLBFileDownloadResponse.counter', index=5,
      number=536870910, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='publish_ts', full_name='nio.ad.messages.DLBFileDownloadResponse.publish_ts', index=6,
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
    _DLBFILEDOWNLOADRESPONSE_RESULTSTATUS,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=65,
  serialized_end=372,
)

_DLBFILEDOWNLOADRESPONSE.fields_by_name['status'].enum_type = _DLBFILEDOWNLOADRESPONSE_RESULTSTATUS
_DLBFILEDOWNLOADRESPONSE_RESULTSTATUS.containing_type = _DLBFILEDOWNLOADRESPONSE
DESCRIPTOR.message_types_by_name['DLBFileDownloadResponse'] = _DLBFILEDOWNLOADRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DLBFileDownloadResponse = _reflection.GeneratedProtocolMessageType('DLBFileDownloadResponse', (_message.Message,), {
  'DESCRIPTOR' : _DLBFILEDOWNLOADRESPONSE,
  '__module__' : 'common.dlb.dlb_file_download_response_pb2'
  # @@protoc_insertion_point(class_scope:nio.ad.messages.DLBFileDownloadResponse)
  })
_sym_db.RegisterMessage(DLBFileDownloadResponse)


# @@protoc_insertion_point(module_scope)

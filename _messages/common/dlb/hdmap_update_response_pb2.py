# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: common/dlb/hdmap_update_response.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='common/dlb/hdmap_update_response.proto',
  package='nio.ad.messages',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n&common/dlb/hdmap_update_response.proto\x12\x0fnio.ad.messages\"\xfe\x01\n\x13HDMapUpdateResponse\x12\x0c\n\x04uuid\x18\x01 \x01(\t\x12\x41\n\x06status\x18\x02 \x01(\x0e\x32\x31.nio.ad.messages.HDMapUpdateResponse.ResultStatus\x12\x1a\n\x0epublish_ptp_ts\x18\xfb\xff\xff\xff\x01 \x01(\x04\x12\x18\n\x0cpublisher_id\x18\xfd\xff\xff\xff\x01 \x01(\t\x12\x13\n\x07\x63ounter\x18\xfe\xff\xff\xff\x01 \x01(\x04\x12\x16\n\npublish_ts\x18\xff\xff\xff\xff\x01 \x01(\x04\"3\n\x0cResultStatus\x12\x0b\n\x07SUCCESS\x10\x00\x12\x0b\n\x07\x46\x41ILURE\x10\x01\x12\t\n\x05\x45XIST\x10\x02')
)



_HDMAPUPDATERESPONSE_RESULTSTATUS = _descriptor.EnumDescriptor(
  name='ResultStatus',
  full_name='nio.ad.messages.HDMapUpdateResponse.ResultStatus',
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
      name='EXIST', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=263,
  serialized_end=314,
)
_sym_db.RegisterEnumDescriptor(_HDMAPUPDATERESPONSE_RESULTSTATUS)


_HDMAPUPDATERESPONSE = _descriptor.Descriptor(
  name='HDMapUpdateResponse',
  full_name='nio.ad.messages.HDMapUpdateResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='uuid', full_name='nio.ad.messages.HDMapUpdateResponse.uuid', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='nio.ad.messages.HDMapUpdateResponse.status', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='publish_ptp_ts', full_name='nio.ad.messages.HDMapUpdateResponse.publish_ptp_ts', index=2,
      number=536870907, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='publisher_id', full_name='nio.ad.messages.HDMapUpdateResponse.publisher_id', index=3,
      number=536870909, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='counter', full_name='nio.ad.messages.HDMapUpdateResponse.counter', index=4,
      number=536870910, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='publish_ts', full_name='nio.ad.messages.HDMapUpdateResponse.publish_ts', index=5,
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
    _HDMAPUPDATERESPONSE_RESULTSTATUS,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=60,
  serialized_end=314,
)

_HDMAPUPDATERESPONSE.fields_by_name['status'].enum_type = _HDMAPUPDATERESPONSE_RESULTSTATUS
_HDMAPUPDATERESPONSE_RESULTSTATUS.containing_type = _HDMAPUPDATERESPONSE
DESCRIPTOR.message_types_by_name['HDMapUpdateResponse'] = _HDMAPUPDATERESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

HDMapUpdateResponse = _reflection.GeneratedProtocolMessageType('HDMapUpdateResponse', (_message.Message,), {
  'DESCRIPTOR' : _HDMAPUPDATERESPONSE,
  '__module__' : 'common.dlb.hdmap_update_response_pb2'
  # @@protoc_insertion_point(class_scope:nio.ad.messages.HDMapUpdateResponse)
  })
_sym_db.RegisterMessage(HDMapUpdateResponse)


# @@protoc_insertion_point(module_scope)

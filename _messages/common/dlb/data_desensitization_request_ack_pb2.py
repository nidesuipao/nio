# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: common/dlb/data_desensitization_request_ack.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='common/dlb/data_desensitization_request_ack.proto',
  package='nio.ad.messages',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n1common/dlb/data_desensitization_request_ack.proto\x12\x0fnio.ad.messages\"\xcd\x02\n\x19\x44\x61taDesensitizationReqAck\x12\x0c\n\x04uuid\x18\x01 \x01(\t\x12N\n\x05state\x18\x02 \x01(\x0e\x32?.nio.ad.messages.DataDesensitizationReqAck.DesensitizationState\x12\x1a\n\x0epublish_ptp_ts\x18\xfb\xff\xff\xff\x01 \x01(\x04\x12\x18\n\x0cpublisher_id\x18\xfd\xff\xff\xff\x01 \x01(\t\x12\x13\n\x07\x63ounter\x18\xfe\xff\xff\xff\x01 \x01(\x04\x12\x16\n\npublish_ts\x18\xff\xff\xff\xff\x01 \x01(\x04\"o\n\x14\x44\x65sensitizationState\x12\x1d\n\x19\x44\x65sensitization_SUCCEEDED\x10\x00\x12\x1c\n\x18\x44\x65sensitization_REJECTED\x10\x01\x12\x1a\n\x16\x44\x65sensitization_FAILED\x10\x02')
)



_DATADESENSITIZATIONREQACK_DESENSITIZATIONSTATE = _descriptor.EnumDescriptor(
  name='DesensitizationState',
  full_name='nio.ad.messages.DataDesensitizationReqAck.DesensitizationState',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='Desensitization_SUCCEEDED', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Desensitization_REJECTED', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Desensitization_FAILED', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=293,
  serialized_end=404,
)
_sym_db.RegisterEnumDescriptor(_DATADESENSITIZATIONREQACK_DESENSITIZATIONSTATE)


_DATADESENSITIZATIONREQACK = _descriptor.Descriptor(
  name='DataDesensitizationReqAck',
  full_name='nio.ad.messages.DataDesensitizationReqAck',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='uuid', full_name='nio.ad.messages.DataDesensitizationReqAck.uuid', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='state', full_name='nio.ad.messages.DataDesensitizationReqAck.state', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='publish_ptp_ts', full_name='nio.ad.messages.DataDesensitizationReqAck.publish_ptp_ts', index=2,
      number=536870907, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='publisher_id', full_name='nio.ad.messages.DataDesensitizationReqAck.publisher_id', index=3,
      number=536870909, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='counter', full_name='nio.ad.messages.DataDesensitizationReqAck.counter', index=4,
      number=536870910, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='publish_ts', full_name='nio.ad.messages.DataDesensitizationReqAck.publish_ts', index=5,
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
    _DATADESENSITIZATIONREQACK_DESENSITIZATIONSTATE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=71,
  serialized_end=404,
)

_DATADESENSITIZATIONREQACK.fields_by_name['state'].enum_type = _DATADESENSITIZATIONREQACK_DESENSITIZATIONSTATE
_DATADESENSITIZATIONREQACK_DESENSITIZATIONSTATE.containing_type = _DATADESENSITIZATIONREQACK
DESCRIPTOR.message_types_by_name['DataDesensitizationReqAck'] = _DATADESENSITIZATIONREQACK
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DataDesensitizationReqAck = _reflection.GeneratedProtocolMessageType('DataDesensitizationReqAck', (_message.Message,), {
  'DESCRIPTOR' : _DATADESENSITIZATIONREQACK,
  '__module__' : 'common.dlb.data_desensitization_request_ack_pb2'
  # @@protoc_insertion_point(class_scope:nio.ad.messages.DataDesensitizationReqAck)
  })
_sym_db.RegisterMessage(DataDesensitizationReqAck)


# @@protoc_insertion_point(module_scope)

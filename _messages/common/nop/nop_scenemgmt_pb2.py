# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: common/nop/nop_scenemgmt.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='common/nop/nop_scenemgmt.proto',
  package='nio.ad.messages',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n\x1e\x63ommon/nop/nop_scenemgmt.proto\x12\x0fnio.ad.messages\"\x8c\x01\n\x0cNopSceneMgmt\x12\x19\n\x11nop_scene_mgmt_ok\x18\x01 \x01(\x08\x12\x1a\n\x0epublish_ptp_ts\x18\xfb\xff\xff\xff\x01 \x01(\x04\x12\x18\n\x0cpublisher_id\x18\xfd\xff\xff\xff\x01 \x01(\t\x12\x13\n\x07\x63ounter\x18\xfe\xff\xff\xff\x01 \x01(\x04\x12\x16\n\npublish_ts\x18\xff\xff\xff\xff\x01 \x01(\x04')
)




_NOPSCENEMGMT = _descriptor.Descriptor(
  name='NopSceneMgmt',
  full_name='nio.ad.messages.NopSceneMgmt',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='nop_scene_mgmt_ok', full_name='nio.ad.messages.NopSceneMgmt.nop_scene_mgmt_ok', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='publish_ptp_ts', full_name='nio.ad.messages.NopSceneMgmt.publish_ptp_ts', index=1,
      number=536870907, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='publisher_id', full_name='nio.ad.messages.NopSceneMgmt.publisher_id', index=2,
      number=536870909, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='counter', full_name='nio.ad.messages.NopSceneMgmt.counter', index=3,
      number=536870910, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='publish_ts', full_name='nio.ad.messages.NopSceneMgmt.publish_ts', index=4,
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
  serialized_start=52,
  serialized_end=192,
)

DESCRIPTOR.message_types_by_name['NopSceneMgmt'] = _NOPSCENEMGMT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

NopSceneMgmt = _reflection.GeneratedProtocolMessageType('NopSceneMgmt', (_message.Message,), {
  'DESCRIPTOR' : _NOPSCENEMGMT,
  '__module__' : 'common.nop.nop_scenemgmt_pb2'
  # @@protoc_insertion_point(class_scope:nio.ad.messages.NopSceneMgmt)
  })
_sym_db.RegisterMessage(NopSceneMgmt)


# @@protoc_insertion_point(module_scope)

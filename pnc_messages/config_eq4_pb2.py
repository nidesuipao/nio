# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: config_eq4.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import stream_pb2 as stream__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='config_eq4.proto',
  package='nio.proto',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n\x10\x63onfig_eq4.proto\x12\tnio.proto\x1a\x0cstream.proto\",\n\tConfigEQ4\x12\x1f\n\x04\x64\x61ta\x18\x01 \x01(\x0b\x32\x11.nio.proto.Stream')
  ,
  dependencies=[stream__pb2.DESCRIPTOR,])




_CONFIGEQ4 = _descriptor.Descriptor(
  name='ConfigEQ4',
  full_name='nio.proto.ConfigEQ4',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='nio.proto.ConfigEQ4.data', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=45,
  serialized_end=89,
)

_CONFIGEQ4.fields_by_name['data'].message_type = stream__pb2._STREAM
DESCRIPTOR.message_types_by_name['ConfigEQ4'] = _CONFIGEQ4
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ConfigEQ4 = _reflection.GeneratedProtocolMessageType('ConfigEQ4', (_message.Message,), {
  'DESCRIPTOR' : _CONFIGEQ4,
  '__module__' : 'config_eq4_pb2'
  # @@protoc_insertion_point(class_scope:nio.proto.ConfigEQ4)
  })
_sym_db.RegisterMessage(ConfigEQ4)


# @@protoc_insertion_point(module_scope)

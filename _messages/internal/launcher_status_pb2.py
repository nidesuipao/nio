# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: messages/internal/launcher_status.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='messages/internal/launcher_status.proto',
  package='nio.ad.messages.internal',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n\'messages/internal/launcher_status.proto\x12\x18nio.ad.messages.internal\"l\n\x0eLauncherStatus\x12\x11\n\tsteady_ts\x18\x01 \x01(\x04\x12\x1a\n\x0epublish_ptp_ts\x18\xfb\xff\xff\xff\x01 \x01(\x04\x12\x13\n\x07\x63ounter\x18\xfe\xff\xff\xff\x01 \x01(\x04\x12\x16\n\npublish_ts\x18\xff\xff\xff\xff\x01 \x01(\x04')
)




_LAUNCHERSTATUS = _descriptor.Descriptor(
  name='LauncherStatus',
  full_name='nio.ad.messages.internal.LauncherStatus',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='steady_ts', full_name='nio.ad.messages.internal.LauncherStatus.steady_ts', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='publish_ptp_ts', full_name='nio.ad.messages.internal.LauncherStatus.publish_ptp_ts', index=1,
      number=536870907, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='counter', full_name='nio.ad.messages.internal.LauncherStatus.counter', index=2,
      number=536870910, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='publish_ts', full_name='nio.ad.messages.internal.LauncherStatus.publish_ts', index=3,
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
  serialized_start=69,
  serialized_end=177,
)

DESCRIPTOR.message_types_by_name['LauncherStatus'] = _LAUNCHERSTATUS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

LauncherStatus = _reflection.GeneratedProtocolMessageType('LauncherStatus', (_message.Message,), {
  'DESCRIPTOR' : _LAUNCHERSTATUS,
  '__module__' : 'messages.internal.launcher_status_pb2'
  # @@protoc_insertion_point(class_scope:nio.ad.messages.internal.LauncherStatus)
  })
_sym_db.RegisterMessage(LauncherStatus)


# @@protoc_insertion_point(module_scope)

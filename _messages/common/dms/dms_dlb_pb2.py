# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: common/dms/dms_dlb.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from common.dms import dms_dlb_enum_pb2 as common_dot_dms_dot_dms__dlb__enum__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='common/dms/dms_dlb.proto',
  package='nio.ad.messages',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n\x18\x63ommon/dms/dms_dlb.proto\x12\x0fnio.ad.messages\x1a\x1d\x63ommon/dms/dms_dlb_enum.proto\"\xf4\x02\n\x07\x44MS_DLB\x12@\n\x0e\x64rowsiness_lvl\x18\x01 \x01(\x0e\x32(.nio.ad.messages.DMS_DrowsinessLevel_DLB\x12\x42\n\x0f\x64istraction_lvl\x18\x02 \x01(\x0e\x32).nio.ad.messages.DMS_DistractionLevel_DLB\x12>\n\x0e\x64rowsiness_sts\x18\x03 \x01(\x0e\x32&.nio.ad.messages.DMS_DrowsinessSts_DLB\x12@\n\x0f\x64istraction_sts\x18\x04 \x01(\x0e\x32\'.nio.ad.messages.DMS_DistractionSts_DLB\x12\x1a\n\x0epublish_ptp_ts\x18\xfb\xff\xff\xff\x01 \x01(\x04\x12\x18\n\x0cpublisher_id\x18\xfd\xff\xff\xff\x01 \x01(\t\x12\x13\n\x07\x63ounter\x18\xfe\xff\xff\xff\x01 \x01(\x04\x12\x16\n\npublish_ts\x18\xff\xff\xff\xff\x01 \x01(\x04')
  ,
  dependencies=[common_dot_dms_dot_dms__dlb__enum__pb2.DESCRIPTOR,])




_DMS_DLB = _descriptor.Descriptor(
  name='DMS_DLB',
  full_name='nio.ad.messages.DMS_DLB',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='drowsiness_lvl', full_name='nio.ad.messages.DMS_DLB.drowsiness_lvl', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='distraction_lvl', full_name='nio.ad.messages.DMS_DLB.distraction_lvl', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='drowsiness_sts', full_name='nio.ad.messages.DMS_DLB.drowsiness_sts', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='distraction_sts', full_name='nio.ad.messages.DMS_DLB.distraction_sts', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='publish_ptp_ts', full_name='nio.ad.messages.DMS_DLB.publish_ptp_ts', index=4,
      number=536870907, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='publisher_id', full_name='nio.ad.messages.DMS_DLB.publisher_id', index=5,
      number=536870909, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='counter', full_name='nio.ad.messages.DMS_DLB.counter', index=6,
      number=536870910, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='publish_ts', full_name='nio.ad.messages.DMS_DLB.publish_ts', index=7,
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
  serialized_start=77,
  serialized_end=449,
)

_DMS_DLB.fields_by_name['drowsiness_lvl'].enum_type = common_dot_dms_dot_dms__dlb__enum__pb2._DMS_DROWSINESSLEVEL_DLB
_DMS_DLB.fields_by_name['distraction_lvl'].enum_type = common_dot_dms_dot_dms__dlb__enum__pb2._DMS_DISTRACTIONLEVEL_DLB
_DMS_DLB.fields_by_name['drowsiness_sts'].enum_type = common_dot_dms_dot_dms__dlb__enum__pb2._DMS_DROWSINESSSTS_DLB
_DMS_DLB.fields_by_name['distraction_sts'].enum_type = common_dot_dms_dot_dms__dlb__enum__pb2._DMS_DISTRACTIONSTS_DLB
DESCRIPTOR.message_types_by_name['DMS_DLB'] = _DMS_DLB
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DMS_DLB = _reflection.GeneratedProtocolMessageType('DMS_DLB', (_message.Message,), {
  'DESCRIPTOR' : _DMS_DLB,
  '__module__' : 'common.dms.dms_dlb_pb2'
  # @@protoc_insertion_point(class_scope:nio.ad.messages.DMS_DLB)
  })
_sym_db.RegisterMessage(DMS_DLB)


# @@protoc_insertion_point(module_scope)

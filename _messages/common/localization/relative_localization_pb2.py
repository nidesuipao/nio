# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: common/localization/relative_localization.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from common.localization import geometry_pb2 as common_dot_localization_dot_geometry__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='common/localization/relative_localization.proto',
  package='nio.ad.messages',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n/common/localization/relative_localization.proto\x12\x0fnio.ad.messages\x1a\"common/localization/geometry.proto\"\xea\x05\n\x14RelativeLocalization\x12\x11\n\ttimestamp\x18\x01 \x01(\x01\x12<\n\x06status\x18\x02 \x01(\x0e\x32,.nio.ad.messages.RelativeLocalization.Status\x12\x33\n\x0b\x65uler_angle\x18\x03 \x01(\x0b\x32\x1e.nio.ad.messages.LocEulerAngle\x12-\n\x08position\x18\x04 \x01(\x0b\x32\x1b.nio.ad.messages.LocVector3\x12-\n\x08velocity\x18\x05 \x01(\x0b\x32\x1b.nio.ad.messages.LocVector3\x12\x32\n\nquaternion\x18\x06 \x01(\x0b\x32\x1e.nio.ad.messages.LocQuaternion\x12/\n\nlinear_acc\x18\x07 \x01(\x0b\x32\x1b.nio.ad.messages.LocVector3\x12\x30\n\x0b\x61ngular_vel\x18\x08 \x01(\x0b\x32\x1b.nio.ad.messages.LocVector3\x12\x12\n\nconfidence\x18\t \x01(\x02\x12\x16\n\x0estatus_message\x18\n \x01(\t\x12\x18\n\x10timestamp_ptp_ns\x18\x0b \x01(\x04\x12\x16\n\x0e\x64im_confidence\x18\x0c \x03(\x02\x12\x19\n\x11online_parameters\x18\r \x03(\x01\x12\x34\n\x0c\x61ttitude_ref\x18\x0e \x01(\x0b\x32\x1e.nio.ad.messages.LocEulerAngle\x12\x1a\n\x0epublish_ptp_ts\x18\xfb\xff\xff\xff\x01 \x01(\x04\x12\x18\n\x0cpublisher_id\x18\xfd\xff\xff\xff\x01 \x01(\t\x12\x13\n\x07\x63ounter\x18\xfe\xff\xff\xff\x01 \x01(\x04\x12\x16\n\npublish_ts\x18\xff\xff\xff\xff\x01 \x01(\x04\"E\n\x06Status\x12\x11\n\rUNINITIALIZED\x10\x00\x12\t\n\x05VALID\x10\x01\x12\x0b\n\x07INVALID\x10\x02\x12\x10\n\x0cSENSOR_ERROR\x10\x03')
  ,
  dependencies=[common_dot_localization_dot_geometry__pb2.DESCRIPTOR,])



_RELATIVELOCALIZATION_STATUS = _descriptor.EnumDescriptor(
  name='Status',
  full_name='nio.ad.messages.RelativeLocalization.Status',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNINITIALIZED', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VALID', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SENSOR_ERROR', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=782,
  serialized_end=851,
)
_sym_db.RegisterEnumDescriptor(_RELATIVELOCALIZATION_STATUS)


_RELATIVELOCALIZATION = _descriptor.Descriptor(
  name='RelativeLocalization',
  full_name='nio.ad.messages.RelativeLocalization',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='nio.ad.messages.RelativeLocalization.timestamp', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='nio.ad.messages.RelativeLocalization.status', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='euler_angle', full_name='nio.ad.messages.RelativeLocalization.euler_angle', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='position', full_name='nio.ad.messages.RelativeLocalization.position', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='velocity', full_name='nio.ad.messages.RelativeLocalization.velocity', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='quaternion', full_name='nio.ad.messages.RelativeLocalization.quaternion', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='linear_acc', full_name='nio.ad.messages.RelativeLocalization.linear_acc', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='angular_vel', full_name='nio.ad.messages.RelativeLocalization.angular_vel', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='confidence', full_name='nio.ad.messages.RelativeLocalization.confidence', index=8,
      number=9, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status_message', full_name='nio.ad.messages.RelativeLocalization.status_message', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timestamp_ptp_ns', full_name='nio.ad.messages.RelativeLocalization.timestamp_ptp_ns', index=10,
      number=11, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dim_confidence', full_name='nio.ad.messages.RelativeLocalization.dim_confidence', index=11,
      number=12, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='online_parameters', full_name='nio.ad.messages.RelativeLocalization.online_parameters', index=12,
      number=13, type=1, cpp_type=5, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='attitude_ref', full_name='nio.ad.messages.RelativeLocalization.attitude_ref', index=13,
      number=14, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='publish_ptp_ts', full_name='nio.ad.messages.RelativeLocalization.publish_ptp_ts', index=14,
      number=536870907, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='publisher_id', full_name='nio.ad.messages.RelativeLocalization.publisher_id', index=15,
      number=536870909, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='counter', full_name='nio.ad.messages.RelativeLocalization.counter', index=16,
      number=536870910, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='publish_ts', full_name='nio.ad.messages.RelativeLocalization.publish_ts', index=17,
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
    _RELATIVELOCALIZATION_STATUS,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=105,
  serialized_end=851,
)

_RELATIVELOCALIZATION.fields_by_name['status'].enum_type = _RELATIVELOCALIZATION_STATUS
_RELATIVELOCALIZATION.fields_by_name['euler_angle'].message_type = common_dot_localization_dot_geometry__pb2._LOCEULERANGLE
_RELATIVELOCALIZATION.fields_by_name['position'].message_type = common_dot_localization_dot_geometry__pb2._LOCVECTOR3
_RELATIVELOCALIZATION.fields_by_name['velocity'].message_type = common_dot_localization_dot_geometry__pb2._LOCVECTOR3
_RELATIVELOCALIZATION.fields_by_name['quaternion'].message_type = common_dot_localization_dot_geometry__pb2._LOCQUATERNION
_RELATIVELOCALIZATION.fields_by_name['linear_acc'].message_type = common_dot_localization_dot_geometry__pb2._LOCVECTOR3
_RELATIVELOCALIZATION.fields_by_name['angular_vel'].message_type = common_dot_localization_dot_geometry__pb2._LOCVECTOR3
_RELATIVELOCALIZATION.fields_by_name['attitude_ref'].message_type = common_dot_localization_dot_geometry__pb2._LOCEULERANGLE
_RELATIVELOCALIZATION_STATUS.containing_type = _RELATIVELOCALIZATION
DESCRIPTOR.message_types_by_name['RelativeLocalization'] = _RELATIVELOCALIZATION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RelativeLocalization = _reflection.GeneratedProtocolMessageType('RelativeLocalization', (_message.Message,), {
  'DESCRIPTOR' : _RELATIVELOCALIZATION,
  '__module__' : 'common.localization.relative_localization_pb2'
  # @@protoc_insertion_point(class_scope:nio.ad.messages.RelativeLocalization)
  })
_sym_db.RegisterMessage(RelativeLocalization)


# @@protoc_insertion_point(module_scope)

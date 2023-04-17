# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: common/sensors/camera_signal_data.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from common.sensors import camera_data_pb2 as common_dot_sensors_dot_camera__data__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='common/sensors/camera_signal_data.proto',
  package='nio.ad.messages',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n\'common/sensors/camera_signal_data.proto\x12\x0fnio.ad.messages\x1a common/sensors/camera_data.proto\"\xda\x01\n\rCameraSigData\x12\'\n\x06header\x18\x01 \x01(\x0b\x32\x17.nio.ad.messages.Header\x12\x13\n\x0bsys_time_us\x18\x02 \x01(\x04\x12\x0e\n\x06status\x18\x03 \x01(\x08\x12\x18\n\x10timestamp_ptp_ns\x18\x04 \x01(\x04\x12\x1a\n\x0epublish_ptp_ts\x18\xfb\xff\xff\xff\x01 \x01(\x04\x12\x18\n\x0cpublisher_id\x18\xfd\xff\xff\xff\x01 \x01(\t\x12\x13\n\x07\x63ounter\x18\xfe\xff\xff\xff\x01 \x01(\x04\x12\x16\n\npublish_ts\x18\xff\xff\xff\xff\x01 \x01(\x04')
  ,
  dependencies=[common_dot_sensors_dot_camera__data__pb2.DESCRIPTOR,])




_CAMERASIGDATA = _descriptor.Descriptor(
  name='CameraSigData',
  full_name='nio.ad.messages.CameraSigData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='nio.ad.messages.CameraSigData.header', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sys_time_us', full_name='nio.ad.messages.CameraSigData.sys_time_us', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='nio.ad.messages.CameraSigData.status', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timestamp_ptp_ns', full_name='nio.ad.messages.CameraSigData.timestamp_ptp_ns', index=3,
      number=4, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='publish_ptp_ts', full_name='nio.ad.messages.CameraSigData.publish_ptp_ts', index=4,
      number=536870907, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='publisher_id', full_name='nio.ad.messages.CameraSigData.publisher_id', index=5,
      number=536870909, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='counter', full_name='nio.ad.messages.CameraSigData.counter', index=6,
      number=536870910, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='publish_ts', full_name='nio.ad.messages.CameraSigData.publish_ts', index=7,
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
  serialized_start=95,
  serialized_end=313,
)

_CAMERASIGDATA.fields_by_name['header'].message_type = common_dot_sensors_dot_camera__data__pb2._HEADER
DESCRIPTOR.message_types_by_name['CameraSigData'] = _CAMERASIGDATA
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CameraSigData = _reflection.GeneratedProtocolMessageType('CameraSigData', (_message.Message,), {
  'DESCRIPTOR' : _CAMERASIGDATA,
  '__module__' : 'common.sensors.camera_signal_data_pb2'
  # @@protoc_insertion_point(class_scope:nio.ad.messages.CameraSigData)
  })
_sym_db.RegisterMessage(CameraSigData)


# @@protoc_insertion_point(module_scope)

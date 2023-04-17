# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: common/sensors/camera_compress_data.proto

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
  name='common/sensors/camera_compress_data.proto',
  package='nio.ad.messages',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n)common/sensors/camera_compress_data.proto\x12\x0fnio.ad.messages\x1a common/sensors/camera_data.proto\"\x88\x03\n\x12\x43\x61meraCompressData\x12\'\n\x06header\x18\x01 \x01(\x0b\x32\x17.nio.ad.messages.Header\x12\x13\n\x0bsys_time_us\x18\x02 \x01(\x04\x12\x0e\n\x06height\x18\x03 \x01(\x05\x12\r\n\x05width\x18\x04 \x01(\x05\x12\x0f\n\x07\x63hannel\x18\x05 \x01(\x05\x12\x0c\n\x04\x64\x61ta\x18\x06 \x01(\x0c\x12\x30\n\x0b\x63olor_space\x18\x07 \x01(\x0e\x32\x1b.nio.ad.messages.ColorSpace\x12\x34\n\rcompress_type\x18\x08 \x01(\x0e\x32\x1d.nio.ad.messages.CompressType\x12\x11\n\tyuvStride\x18\t \x01(\x05\x12\x18\n\x10timestamp_ptp_ns\x18\n \x01(\x04\x12\x1a\n\x0epublish_ptp_ts\x18\xfb\xff\xff\xff\x01 \x01(\x04\x12\x18\n\x0cpublisher_id\x18\xfd\xff\xff\xff\x01 \x01(\t\x12\x13\n\x07\x63ounter\x18\xfe\xff\xff\xff\x01 \x01(\x04\x12\x16\n\npublish_ts\x18\xff\xff\xff\xff\x01 \x01(\x04')
  ,
  dependencies=[common_dot_sensors_dot_camera__data__pb2.DESCRIPTOR,])




_CAMERACOMPRESSDATA = _descriptor.Descriptor(
  name='CameraCompressData',
  full_name='nio.ad.messages.CameraCompressData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='nio.ad.messages.CameraCompressData.header', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sys_time_us', full_name='nio.ad.messages.CameraCompressData.sys_time_us', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='height', full_name='nio.ad.messages.CameraCompressData.height', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='width', full_name='nio.ad.messages.CameraCompressData.width', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='channel', full_name='nio.ad.messages.CameraCompressData.channel', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='nio.ad.messages.CameraCompressData.data', index=5,
      number=6, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='color_space', full_name='nio.ad.messages.CameraCompressData.color_space', index=6,
      number=7, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='compress_type', full_name='nio.ad.messages.CameraCompressData.compress_type', index=7,
      number=8, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='yuvStride', full_name='nio.ad.messages.CameraCompressData.yuvStride', index=8,
      number=9, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timestamp_ptp_ns', full_name='nio.ad.messages.CameraCompressData.timestamp_ptp_ns', index=9,
      number=10, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='publish_ptp_ts', full_name='nio.ad.messages.CameraCompressData.publish_ptp_ts', index=10,
      number=536870907, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='publisher_id', full_name='nio.ad.messages.CameraCompressData.publisher_id', index=11,
      number=536870909, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='counter', full_name='nio.ad.messages.CameraCompressData.counter', index=12,
      number=536870910, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='publish_ts', full_name='nio.ad.messages.CameraCompressData.publish_ts', index=13,
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
  serialized_start=97,
  serialized_end=489,
)

_CAMERACOMPRESSDATA.fields_by_name['header'].message_type = common_dot_sensors_dot_camera__data__pb2._HEADER
_CAMERACOMPRESSDATA.fields_by_name['color_space'].enum_type = common_dot_sensors_dot_camera__data__pb2._COLORSPACE
_CAMERACOMPRESSDATA.fields_by_name['compress_type'].enum_type = common_dot_sensors_dot_camera__data__pb2._COMPRESSTYPE
DESCRIPTOR.message_types_by_name['CameraCompressData'] = _CAMERACOMPRESSDATA
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CameraCompressData = _reflection.GeneratedProtocolMessageType('CameraCompressData', (_message.Message,), {
  'DESCRIPTOR' : _CAMERACOMPRESSDATA,
  '__module__' : 'common.sensors.camera_compress_data_pb2'
  # @@protoc_insertion_point(class_scope:nio.ad.messages.CameraCompressData)
  })
_sym_db.RegisterMessage(CameraCompressData)


# @@protoc_insertion_point(module_scope)

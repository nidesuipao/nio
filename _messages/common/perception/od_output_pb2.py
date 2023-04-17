# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: common/perception/od_output.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='common/perception/od_output.proto',
  package='nio.ad.messages',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n!common/perception/od_output.proto\x12\x0fnio.ad.messages\"7\n\x0cSensorHeader\x12\x11\n\tsensor_id\x18\x01 \x01(\r\x12\x14\n\x0cmeasuring_ts\x18\x02 \x01(\x04\"\x8d\x02\n\x0bLidarObject\x12\x11\n\tsensor_id\x18\x01 \x01(\r\x12\x11\n\tobject_id\x18\x02 \x01(\r\x12\x12\n\nclass_type\x18\x03 \x01(\x05\x12\t\n\x01x\x18\x04 \x01(\x02\x12\t\n\x01y\x18\x05 \x01(\x02\x12\t\n\x01z\x18\x06 \x01(\x02\x12\r\n\x05width\x18\x07 \x01(\x02\x12\x0e\n\x06height\x18\x08 \x01(\x02\x12\x0e\n\x06length\x18\t \x01(\x02\x12\x0b\n\x03yaw\x18\n \x01(\x02\x12\r\n\x05score\x18\x0b \x01(\x02\x12\x1c\n\x14second_return_ration\x18\x0c \x01(\x02\x12\x1e\n\x16high_reflection_ration\x18\r \x01(\x02\x12\x1a\n\x12statistics_feature\x18\x0e \x03(\x02\"g\n\x06Mono3D\x12\t\n\x01x\x18\x01 \x01(\x02\x12\t\n\x01y\x18\x02 \x01(\x02\x12\t\n\x01z\x18\x03 \x01(\x02\x12\r\n\x05width\x18\x04 \x01(\x02\x12\x0e\n\x06height\x18\x05 \x01(\x02\x12\x0e\n\x06length\x18\x06 \x01(\x02\x12\r\n\x05theta\x18\x07 \x01(\x02\"\xe8\x02\n\x0c\x43\x61meraObject\x12\x11\n\tsensor_id\x18\x01 \x01(\r\x12\x11\n\tobject_id\x18\x02 \x01(\r\x12\r\n\x05score\x18\x03 \x01(\x02\x12\x12\n\nclass_type\x18\x04 \x01(\x05\x12\'\n\x06mono3d\x18\x05 \x01(\x0b\x32\x17.nio.ad.messages.Mono3D\x12\x10\n\x08\x62\x61tch_id\x18\x06 \x01(\x02\x12\x0f\n\x07subtype\x18\x07 \x01(\x02\x12\x16\n\x0esubtype_scores\x18\x08 \x03(\x02\x12\x11\n\tocclusion\x18\t \x03(\x02\x12\x0b\n\x03\x62ox\x18\n \x03(\x02\x12\x0c\n\x04kpts\x18\x0b \x03(\x02\x12\x12\n\nkpts_score\x18\x0c \x03(\x02\x12\x16\n\x0euncertainty_2d\x18\r \x03(\x02\x12\x16\n\x0euncertainty_3d\x18\x0e \x03(\x02\x12\x14\n\x0creid_feature\x18\x0f \x03(\x02\x12\x0f\n\x07theta2d\x18\x10 \x03(\x02\x12\x12\n\nhas_person\x18\x11 \x01(\x02\"\x91\x02\n\x12StaticCameraObject\x12\x11\n\tsensor_id\x18\x01 \x01(\r\x12\x11\n\tobject_id\x18\x02 \x01(\r\x12\r\n\x05score\x18\x03 \x01(\x02\x12\x12\n\nclass_type\x18\x04 \x01(\x05\x12\'\n\x06mono3d\x18\x05 \x01(\x0b\x32\x17.nio.ad.messages.Mono3D\x12\x10\n\x08\x62\x61tch_id\x18\x06 \x01(\x02\x12\x0f\n\x07subtype\x18\x07 \x01(\x02\x12\x16\n\x0esubtype_scores\x18\x08 \x03(\x02\x12\x11\n\tocclusion\x18\t \x03(\x02\x12\x0b\n\x03\x62ox\x18\n \x03(\x02\x12\x16\n\x0euncertainty_2d\x18\x0b \x03(\x02\x12\x16\n\x0euncertainty_3d\x18\x0c \x03(\x02\"\x9d\x02\n\x0e\x46\x61ilsafeObject\x12\x1a\n\x12\x66ull_blockage_pred\x18\x01 \x01(\r\x12\x1b\n\x13\x66ull_blockage_score\x18\x02 \x01(\x02\x12\x14\n\x0clow_sun_pred\x18\x03 \x01(\r\x12\x15\n\rlow_sun_score\x18\x04 \x01(\x02\x12\x1d\n\x15partial_blockage_pred\x18\x05 \x01(\r\x12\x1e\n\x16partial_blockage_score\x18\x06 \x01(\x02\x12\x11\n\train_pred\x18\x07 \x01(\r\x12\x12\n\nrain_score\x18\x08 \x01(\x02\x12\x1e\n\x16windshield_frozen_pred\x18\t \x01(\r\x12\x1f\n\x17windshield_frozen_score\x18\n \x01(\x02\"\xb8\x03\n\nODOutputPb\x12.\n\x07sensors\x18\x01 \x03(\x0b\x32\x1d.nio.ad.messages.SensorHeader\x12\x12\n\ncooking_ts\x18\x02 \x01(\x04\x12\x0f\n\x07send_ts\x18\x03 \x01(\x04\x12\x32\n\x0clidar_result\x18\x04 \x03(\x0b\x32\x1c.nio.ad.messages.LidarObject\x12\x31\n\ncam_result\x18\x05 \x03(\x0b\x32\x1d.nio.ad.messages.CameraObject\x12>\n\x11static_cam_result\x18\x06 \x03(\x0b\x32#.nio.ad.messages.StaticCameraObject\x12\x38\n\x0f\x66\x61ilsafe_result\x18\x07 \x03(\x0b\x32\x1f.nio.ad.messages.FailsafeObject\x12\x11\n\x08reserved\x18\xc8\x01 \x01(\t\x12\x1a\n\x0epublish_ptp_ts\x18\xfb\xff\xff\xff\x01 \x01(\x04\x12\x18\n\x0cpublisher_id\x18\xfd\xff\xff\xff\x01 \x01(\t\x12\x13\n\x07\x63ounter\x18\xfe\xff\xff\xff\x01 \x01(\x04\x12\x16\n\npublish_ts\x18\xff\xff\xff\xff\x01 \x01(\x04')
)




_SENSORHEADER = _descriptor.Descriptor(
  name='SensorHeader',
  full_name='nio.ad.messages.SensorHeader',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='sensor_id', full_name='nio.ad.messages.SensorHeader.sensor_id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='measuring_ts', full_name='nio.ad.messages.SensorHeader.measuring_ts', index=1,
      number=2, type=4, cpp_type=4, label=1,
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
  serialized_start=54,
  serialized_end=109,
)


_LIDAROBJECT = _descriptor.Descriptor(
  name='LidarObject',
  full_name='nio.ad.messages.LidarObject',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='sensor_id', full_name='nio.ad.messages.LidarObject.sensor_id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='object_id', full_name='nio.ad.messages.LidarObject.object_id', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='class_type', full_name='nio.ad.messages.LidarObject.class_type', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='x', full_name='nio.ad.messages.LidarObject.x', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='y', full_name='nio.ad.messages.LidarObject.y', index=4,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='z', full_name='nio.ad.messages.LidarObject.z', index=5,
      number=6, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='width', full_name='nio.ad.messages.LidarObject.width', index=6,
      number=7, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='height', full_name='nio.ad.messages.LidarObject.height', index=7,
      number=8, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='length', full_name='nio.ad.messages.LidarObject.length', index=8,
      number=9, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='yaw', full_name='nio.ad.messages.LidarObject.yaw', index=9,
      number=10, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='score', full_name='nio.ad.messages.LidarObject.score', index=10,
      number=11, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='second_return_ration', full_name='nio.ad.messages.LidarObject.second_return_ration', index=11,
      number=12, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='high_reflection_ration', full_name='nio.ad.messages.LidarObject.high_reflection_ration', index=12,
      number=13, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='statistics_feature', full_name='nio.ad.messages.LidarObject.statistics_feature', index=13,
      number=14, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=112,
  serialized_end=381,
)


_MONO3D = _descriptor.Descriptor(
  name='Mono3D',
  full_name='nio.ad.messages.Mono3D',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='x', full_name='nio.ad.messages.Mono3D.x', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='y', full_name='nio.ad.messages.Mono3D.y', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='z', full_name='nio.ad.messages.Mono3D.z', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='width', full_name='nio.ad.messages.Mono3D.width', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='height', full_name='nio.ad.messages.Mono3D.height', index=4,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='length', full_name='nio.ad.messages.Mono3D.length', index=5,
      number=6, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='theta', full_name='nio.ad.messages.Mono3D.theta', index=6,
      number=7, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=383,
  serialized_end=486,
)


_CAMERAOBJECT = _descriptor.Descriptor(
  name='CameraObject',
  full_name='nio.ad.messages.CameraObject',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='sensor_id', full_name='nio.ad.messages.CameraObject.sensor_id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='object_id', full_name='nio.ad.messages.CameraObject.object_id', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='score', full_name='nio.ad.messages.CameraObject.score', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='class_type', full_name='nio.ad.messages.CameraObject.class_type', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mono3d', full_name='nio.ad.messages.CameraObject.mono3d', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='batch_id', full_name='nio.ad.messages.CameraObject.batch_id', index=5,
      number=6, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='subtype', full_name='nio.ad.messages.CameraObject.subtype', index=6,
      number=7, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='subtype_scores', full_name='nio.ad.messages.CameraObject.subtype_scores', index=7,
      number=8, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='occlusion', full_name='nio.ad.messages.CameraObject.occlusion', index=8,
      number=9, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='box', full_name='nio.ad.messages.CameraObject.box', index=9,
      number=10, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='kpts', full_name='nio.ad.messages.CameraObject.kpts', index=10,
      number=11, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='kpts_score', full_name='nio.ad.messages.CameraObject.kpts_score', index=11,
      number=12, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='uncertainty_2d', full_name='nio.ad.messages.CameraObject.uncertainty_2d', index=12,
      number=13, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='uncertainty_3d', full_name='nio.ad.messages.CameraObject.uncertainty_3d', index=13,
      number=14, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='reid_feature', full_name='nio.ad.messages.CameraObject.reid_feature', index=14,
      number=15, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='theta2d', full_name='nio.ad.messages.CameraObject.theta2d', index=15,
      number=16, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='has_person', full_name='nio.ad.messages.CameraObject.has_person', index=16,
      number=17, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=489,
  serialized_end=849,
)


_STATICCAMERAOBJECT = _descriptor.Descriptor(
  name='StaticCameraObject',
  full_name='nio.ad.messages.StaticCameraObject',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='sensor_id', full_name='nio.ad.messages.StaticCameraObject.sensor_id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='object_id', full_name='nio.ad.messages.StaticCameraObject.object_id', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='score', full_name='nio.ad.messages.StaticCameraObject.score', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='class_type', full_name='nio.ad.messages.StaticCameraObject.class_type', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mono3d', full_name='nio.ad.messages.StaticCameraObject.mono3d', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='batch_id', full_name='nio.ad.messages.StaticCameraObject.batch_id', index=5,
      number=6, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='subtype', full_name='nio.ad.messages.StaticCameraObject.subtype', index=6,
      number=7, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='subtype_scores', full_name='nio.ad.messages.StaticCameraObject.subtype_scores', index=7,
      number=8, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='occlusion', full_name='nio.ad.messages.StaticCameraObject.occlusion', index=8,
      number=9, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='box', full_name='nio.ad.messages.StaticCameraObject.box', index=9,
      number=10, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='uncertainty_2d', full_name='nio.ad.messages.StaticCameraObject.uncertainty_2d', index=10,
      number=11, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='uncertainty_3d', full_name='nio.ad.messages.StaticCameraObject.uncertainty_3d', index=11,
      number=12, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=852,
  serialized_end=1125,
)


_FAILSAFEOBJECT = _descriptor.Descriptor(
  name='FailsafeObject',
  full_name='nio.ad.messages.FailsafeObject',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='full_blockage_pred', full_name='nio.ad.messages.FailsafeObject.full_blockage_pred', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='full_blockage_score', full_name='nio.ad.messages.FailsafeObject.full_blockage_score', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='low_sun_pred', full_name='nio.ad.messages.FailsafeObject.low_sun_pred', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='low_sun_score', full_name='nio.ad.messages.FailsafeObject.low_sun_score', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='partial_blockage_pred', full_name='nio.ad.messages.FailsafeObject.partial_blockage_pred', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='partial_blockage_score', full_name='nio.ad.messages.FailsafeObject.partial_blockage_score', index=5,
      number=6, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rain_pred', full_name='nio.ad.messages.FailsafeObject.rain_pred', index=6,
      number=7, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rain_score', full_name='nio.ad.messages.FailsafeObject.rain_score', index=7,
      number=8, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='windshield_frozen_pred', full_name='nio.ad.messages.FailsafeObject.windshield_frozen_pred', index=8,
      number=9, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='windshield_frozen_score', full_name='nio.ad.messages.FailsafeObject.windshield_frozen_score', index=9,
      number=10, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=1128,
  serialized_end=1413,
)


_ODOUTPUTPB = _descriptor.Descriptor(
  name='ODOutputPb',
  full_name='nio.ad.messages.ODOutputPb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='sensors', full_name='nio.ad.messages.ODOutputPb.sensors', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cooking_ts', full_name='nio.ad.messages.ODOutputPb.cooking_ts', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='send_ts', full_name='nio.ad.messages.ODOutputPb.send_ts', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lidar_result', full_name='nio.ad.messages.ODOutputPb.lidar_result', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cam_result', full_name='nio.ad.messages.ODOutputPb.cam_result', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='static_cam_result', full_name='nio.ad.messages.ODOutputPb.static_cam_result', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='failsafe_result', full_name='nio.ad.messages.ODOutputPb.failsafe_result', index=6,
      number=7, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='reserved', full_name='nio.ad.messages.ODOutputPb.reserved', index=7,
      number=200, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='publish_ptp_ts', full_name='nio.ad.messages.ODOutputPb.publish_ptp_ts', index=8,
      number=536870907, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='publisher_id', full_name='nio.ad.messages.ODOutputPb.publisher_id', index=9,
      number=536870909, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='counter', full_name='nio.ad.messages.ODOutputPb.counter', index=10,
      number=536870910, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='publish_ts', full_name='nio.ad.messages.ODOutputPb.publish_ts', index=11,
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
  serialized_start=1416,
  serialized_end=1856,
)

_CAMERAOBJECT.fields_by_name['mono3d'].message_type = _MONO3D
_STATICCAMERAOBJECT.fields_by_name['mono3d'].message_type = _MONO3D
_ODOUTPUTPB.fields_by_name['sensors'].message_type = _SENSORHEADER
_ODOUTPUTPB.fields_by_name['lidar_result'].message_type = _LIDAROBJECT
_ODOUTPUTPB.fields_by_name['cam_result'].message_type = _CAMERAOBJECT
_ODOUTPUTPB.fields_by_name['static_cam_result'].message_type = _STATICCAMERAOBJECT
_ODOUTPUTPB.fields_by_name['failsafe_result'].message_type = _FAILSAFEOBJECT
DESCRIPTOR.message_types_by_name['SensorHeader'] = _SENSORHEADER
DESCRIPTOR.message_types_by_name['LidarObject'] = _LIDAROBJECT
DESCRIPTOR.message_types_by_name['Mono3D'] = _MONO3D
DESCRIPTOR.message_types_by_name['CameraObject'] = _CAMERAOBJECT
DESCRIPTOR.message_types_by_name['StaticCameraObject'] = _STATICCAMERAOBJECT
DESCRIPTOR.message_types_by_name['FailsafeObject'] = _FAILSAFEOBJECT
DESCRIPTOR.message_types_by_name['ODOutputPb'] = _ODOUTPUTPB
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SensorHeader = _reflection.GeneratedProtocolMessageType('SensorHeader', (_message.Message,), {
  'DESCRIPTOR' : _SENSORHEADER,
  '__module__' : 'common.perception.od_output_pb2'
  # @@protoc_insertion_point(class_scope:nio.ad.messages.SensorHeader)
  })
_sym_db.RegisterMessage(SensorHeader)

LidarObject = _reflection.GeneratedProtocolMessageType('LidarObject', (_message.Message,), {
  'DESCRIPTOR' : _LIDAROBJECT,
  '__module__' : 'common.perception.od_output_pb2'
  # @@protoc_insertion_point(class_scope:nio.ad.messages.LidarObject)
  })
_sym_db.RegisterMessage(LidarObject)

Mono3D = _reflection.GeneratedProtocolMessageType('Mono3D', (_message.Message,), {
  'DESCRIPTOR' : _MONO3D,
  '__module__' : 'common.perception.od_output_pb2'
  # @@protoc_insertion_point(class_scope:nio.ad.messages.Mono3D)
  })
_sym_db.RegisterMessage(Mono3D)

CameraObject = _reflection.GeneratedProtocolMessageType('CameraObject', (_message.Message,), {
  'DESCRIPTOR' : _CAMERAOBJECT,
  '__module__' : 'common.perception.od_output_pb2'
  # @@protoc_insertion_point(class_scope:nio.ad.messages.CameraObject)
  })
_sym_db.RegisterMessage(CameraObject)

StaticCameraObject = _reflection.GeneratedProtocolMessageType('StaticCameraObject', (_message.Message,), {
  'DESCRIPTOR' : _STATICCAMERAOBJECT,
  '__module__' : 'common.perception.od_output_pb2'
  # @@protoc_insertion_point(class_scope:nio.ad.messages.StaticCameraObject)
  })
_sym_db.RegisterMessage(StaticCameraObject)

FailsafeObject = _reflection.GeneratedProtocolMessageType('FailsafeObject', (_message.Message,), {
  'DESCRIPTOR' : _FAILSAFEOBJECT,
  '__module__' : 'common.perception.od_output_pb2'
  # @@protoc_insertion_point(class_scope:nio.ad.messages.FailsafeObject)
  })
_sym_db.RegisterMessage(FailsafeObject)

ODOutputPb = _reflection.GeneratedProtocolMessageType('ODOutputPb', (_message.Message,), {
  'DESCRIPTOR' : _ODOUTPUTPB,
  '__module__' : 'common.perception.od_output_pb2'
  # @@protoc_insertion_point(class_scope:nio.ad.messages.ODOutputPb)
  })
_sym_db.RegisterMessage(ODOutputPb)


# @@protoc_insertion_point(module_scope)

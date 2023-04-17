# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: perception_object.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import geometry_pb2 as geometry__pb2
import prediction_pb2 as prediction__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='perception_object.proto',
  package='nio.proto',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n\x17perception_object.proto\x12\tnio.proto\x1a\x0egeometry.proto\x1a\x10prediction.proto\"\xc2\x06\n\x10PerceptionObject\x12\n\n\x02id\x18\x01 \x01(\x05\x12%\n\x08position\x18\x02 \x01(\x0b\x32\x13.nio.proto.Vector3d\x12%\n\x08velocity\x18\x03 \x01(\x0b\x32\x13.nio.proto.Vector3d\x12)\n\x0c\x61\x63\x63\x65leration\x18\x04 \x01(\x0b\x32\x13.nio.proto.Vector3d\x12\x0f\n\x07heading\x18\x05 \x01(\x01\x12)\n\x0c\x62ounding_box\x18\x06 \x01(\x0b\x32\x13.nio.proto.Vector3d\x12#\n\x07polygon\x18\x07 \x01(\x0b\x32\x12.nio.proto.Polygon\x12\x15\n\rtracking_time\x18\x08 \x01(\x06\x12.\n\x04type\x18\t \x01(\x0e\x32 .nio.proto.PerceptionObject.Type\x12)\n\nprediction\x18\n \x03(\x0b\x32\x15.nio.proto.Prediction\x12\x32\n\x06source\x18\x0b \x01(\x0e\x32\".nio.proto.PerceptionObject.Source\x12\x18\n\x10point_cloud_size\x18\x0c \x01(\x05\x12\x15\n\rcluster_index\x18\r \x03(\r\x12:\n\ncoordinate\x18\x0e \x01(\x0e\x32&.nio.proto.PerceptionObject.Coordinate\"t\n\x04Type\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x12\n\x0eUNKNOWN_STATIC\x10\x01\x12\x13\n\x0fUNKNOWN_DYNAMIC\x10\x02\x12\x0e\n\nPEDESTRIAN\x10\x03\x12\x08\n\x04\x42IKE\x10\x04\x12\x07\n\x03\x43\x41R\x10\x05\x12\t\n\x05TRUCK\x10\x06\x12\x08\n\x04\x43ONE\x10\x07\"\x96\x01\n\x06Source\x12\r\n\x05RAVEN\x10\x00\x1a\x02\x08\x01\x12\x0e\n\x06ZEALOT\x10\x01\x1a\x02\x08\x01\x12\t\n\x05LIDAR\x10\x02\x12\n\n\x06\x43\x41MERA\x10\x03\x12\t\n\x05RADAR\x10\x04\x12\x10\n\x0cLIDAR_CAMERA\x10\x05\x12\x10\n\x0cRADAR_CAMERA\x10\x06\x12\x0f\n\x0bLIDAR_RADAR\x10\x07\x12\x16\n\x12LIDAR_RADAR_CAMERA\x10\x08\"&\n\nCoordinate\x12\x0c\n\x08RELATIVE\x10\x00\x12\n\n\x06GLOBAL\x10\x01\"v\n\x11PerceptionObjects\x12\x11\n\ttime_meas\x18\x01 \x01(\x04\x12\x10\n\x08time_pub\x18\x02 \x01(\x04\x12,\n\x07objects\x18\x03 \x03(\x0b\x32\x1b.nio.proto.PerceptionObject\x12\x0e\n\x06images\x18\x04 \x03(\t\"?\n\x18PerceptionObjectsRequest\x12#\n\x07polygon\x18\x01 \x01(\x0b\x32\x12.nio.proto.Polygon')
  ,
  dependencies=[geometry__pb2.DESCRIPTOR,prediction__pb2.DESCRIPTOR,])



_PERCEPTIONOBJECT_TYPE = _descriptor.EnumDescriptor(
  name='Type',
  full_name='nio.proto.PerceptionObject.Type',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN_STATIC', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN_DYNAMIC', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PEDESTRIAN', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BIKE', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CAR', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TRUCK', index=6, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CONE', index=7, number=7,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=598,
  serialized_end=714,
)
_sym_db.RegisterEnumDescriptor(_PERCEPTIONOBJECT_TYPE)

_PERCEPTIONOBJECT_SOURCE = _descriptor.EnumDescriptor(
  name='Source',
  full_name='nio.proto.PerceptionObject.Source',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='RAVEN', index=0, number=0,
      serialized_options=_b('\010\001'),
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ZEALOT', index=1, number=1,
      serialized_options=_b('\010\001'),
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LIDAR', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CAMERA', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RADAR', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LIDAR_CAMERA', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RADAR_CAMERA', index=6, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LIDAR_RADAR', index=7, number=7,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LIDAR_RADAR_CAMERA', index=8, number=8,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=717,
  serialized_end=867,
)
_sym_db.RegisterEnumDescriptor(_PERCEPTIONOBJECT_SOURCE)

_PERCEPTIONOBJECT_COORDINATE = _descriptor.EnumDescriptor(
  name='Coordinate',
  full_name='nio.proto.PerceptionObject.Coordinate',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='RELATIVE', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GLOBAL', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=869,
  serialized_end=907,
)
_sym_db.RegisterEnumDescriptor(_PERCEPTIONOBJECT_COORDINATE)


_PERCEPTIONOBJECT = _descriptor.Descriptor(
  name='PerceptionObject',
  full_name='nio.proto.PerceptionObject',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='nio.proto.PerceptionObject.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='position', full_name='nio.proto.PerceptionObject.position', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='velocity', full_name='nio.proto.PerceptionObject.velocity', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='acceleration', full_name='nio.proto.PerceptionObject.acceleration', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='heading', full_name='nio.proto.PerceptionObject.heading', index=4,
      number=5, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bounding_box', full_name='nio.proto.PerceptionObject.bounding_box', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='polygon', full_name='nio.proto.PerceptionObject.polygon', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tracking_time', full_name='nio.proto.PerceptionObject.tracking_time', index=7,
      number=8, type=6, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='nio.proto.PerceptionObject.type', index=8,
      number=9, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='prediction', full_name='nio.proto.PerceptionObject.prediction', index=9,
      number=10, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='source', full_name='nio.proto.PerceptionObject.source', index=10,
      number=11, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='point_cloud_size', full_name='nio.proto.PerceptionObject.point_cloud_size', index=11,
      number=12, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cluster_index', full_name='nio.proto.PerceptionObject.cluster_index', index=12,
      number=13, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='coordinate', full_name='nio.proto.PerceptionObject.coordinate', index=13,
      number=14, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _PERCEPTIONOBJECT_TYPE,
    _PERCEPTIONOBJECT_SOURCE,
    _PERCEPTIONOBJECT_COORDINATE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=73,
  serialized_end=907,
)


_PERCEPTIONOBJECTS = _descriptor.Descriptor(
  name='PerceptionObjects',
  full_name='nio.proto.PerceptionObjects',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='time_meas', full_name='nio.proto.PerceptionObjects.time_meas', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='time_pub', full_name='nio.proto.PerceptionObjects.time_pub', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='objects', full_name='nio.proto.PerceptionObjects.objects', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='images', full_name='nio.proto.PerceptionObjects.images', index=3,
      number=4, type=9, cpp_type=9, label=3,
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
  serialized_start=909,
  serialized_end=1027,
)


_PERCEPTIONOBJECTSREQUEST = _descriptor.Descriptor(
  name='PerceptionObjectsRequest',
  full_name='nio.proto.PerceptionObjectsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='polygon', full_name='nio.proto.PerceptionObjectsRequest.polygon', index=0,
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
  serialized_start=1029,
  serialized_end=1092,
)

_PERCEPTIONOBJECT.fields_by_name['position'].message_type = geometry__pb2._VECTOR3D
_PERCEPTIONOBJECT.fields_by_name['velocity'].message_type = geometry__pb2._VECTOR3D
_PERCEPTIONOBJECT.fields_by_name['acceleration'].message_type = geometry__pb2._VECTOR3D
_PERCEPTIONOBJECT.fields_by_name['bounding_box'].message_type = geometry__pb2._VECTOR3D
_PERCEPTIONOBJECT.fields_by_name['polygon'].message_type = geometry__pb2._POLYGON
_PERCEPTIONOBJECT.fields_by_name['type'].enum_type = _PERCEPTIONOBJECT_TYPE
_PERCEPTIONOBJECT.fields_by_name['prediction'].message_type = prediction__pb2._PREDICTION
_PERCEPTIONOBJECT.fields_by_name['source'].enum_type = _PERCEPTIONOBJECT_SOURCE
_PERCEPTIONOBJECT.fields_by_name['coordinate'].enum_type = _PERCEPTIONOBJECT_COORDINATE
_PERCEPTIONOBJECT_TYPE.containing_type = _PERCEPTIONOBJECT
_PERCEPTIONOBJECT_SOURCE.containing_type = _PERCEPTIONOBJECT
_PERCEPTIONOBJECT_COORDINATE.containing_type = _PERCEPTIONOBJECT
_PERCEPTIONOBJECTS.fields_by_name['objects'].message_type = _PERCEPTIONOBJECT
_PERCEPTIONOBJECTSREQUEST.fields_by_name['polygon'].message_type = geometry__pb2._POLYGON
DESCRIPTOR.message_types_by_name['PerceptionObject'] = _PERCEPTIONOBJECT
DESCRIPTOR.message_types_by_name['PerceptionObjects'] = _PERCEPTIONOBJECTS
DESCRIPTOR.message_types_by_name['PerceptionObjectsRequest'] = _PERCEPTIONOBJECTSREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PerceptionObject = _reflection.GeneratedProtocolMessageType('PerceptionObject', (_message.Message,), {
  'DESCRIPTOR' : _PERCEPTIONOBJECT,
  '__module__' : 'perception_object_pb2'
  # @@protoc_insertion_point(class_scope:nio.proto.PerceptionObject)
  })
_sym_db.RegisterMessage(PerceptionObject)

PerceptionObjects = _reflection.GeneratedProtocolMessageType('PerceptionObjects', (_message.Message,), {
  'DESCRIPTOR' : _PERCEPTIONOBJECTS,
  '__module__' : 'perception_object_pb2'
  # @@protoc_insertion_point(class_scope:nio.proto.PerceptionObjects)
  })
_sym_db.RegisterMessage(PerceptionObjects)

PerceptionObjectsRequest = _reflection.GeneratedProtocolMessageType('PerceptionObjectsRequest', (_message.Message,), {
  'DESCRIPTOR' : _PERCEPTIONOBJECTSREQUEST,
  '__module__' : 'perception_object_pb2'
  # @@protoc_insertion_point(class_scope:nio.proto.PerceptionObjectsRequest)
  })
_sym_db.RegisterMessage(PerceptionObjectsRequest)


_PERCEPTIONOBJECT_SOURCE.values_by_name["RAVEN"]._options = None
_PERCEPTIONOBJECT_SOURCE.values_by_name["ZEALOT"]._options = None
# @@protoc_insertion_point(module_scope)

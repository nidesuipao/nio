# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: common/map_engine/hd_road_geo_line.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from common.map_engine import map_geometry_pb2 as common_dot_map__engine_dot_map__geometry__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='common/map_engine/hd_road_geo_line.proto',
  package='nio.ad.messages',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n(common/map_engine/hd_road_geo_line.proto\x12\x0fnio.ad.messages\x1a$common/map_engine/map_geometry.proto\"\xb2\x01\n\rHdRoadGeoLine\x12\n\n\x02id\x18\x01 \x01(\x04\x12\x0f\n\x07link_id\x18\x02 \x01(\x04\x12\x31\n\x0bshape_point\x18\x03 \x01(\x0b\x32\x1c.nio.ad.messages.MapPolyline\x12\x11\n\tcurvature\x18\x04 \x03(\x01\x12\r\n\x05slope\x18\x05 \x03(\x01\x12\x0f\n\x07heading\x18\x06 \x03(\x01\x12\x1e\n\x12shape_point_offset\x18\x07 \x03(\x01\x42\x02\x10\x01\"O\n\x11HdRoadGeoLineList\x12:\n\x12road_geo_line_list\x18\x01 \x03(\x0b\x32\x1e.nio.ad.messages.HdRoadGeoLine')
  ,
  dependencies=[common_dot_map__engine_dot_map__geometry__pb2.DESCRIPTOR,])




_HDROADGEOLINE = _descriptor.Descriptor(
  name='HdRoadGeoLine',
  full_name='nio.ad.messages.HdRoadGeoLine',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='nio.ad.messages.HdRoadGeoLine.id', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='link_id', full_name='nio.ad.messages.HdRoadGeoLine.link_id', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='shape_point', full_name='nio.ad.messages.HdRoadGeoLine.shape_point', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='curvature', full_name='nio.ad.messages.HdRoadGeoLine.curvature', index=3,
      number=4, type=1, cpp_type=5, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='slope', full_name='nio.ad.messages.HdRoadGeoLine.slope', index=4,
      number=5, type=1, cpp_type=5, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='heading', full_name='nio.ad.messages.HdRoadGeoLine.heading', index=5,
      number=6, type=1, cpp_type=5, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='shape_point_offset', full_name='nio.ad.messages.HdRoadGeoLine.shape_point_offset', index=6,
      number=7, type=1, cpp_type=5, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\020\001'), file=DESCRIPTOR),
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
  serialized_start=100,
  serialized_end=278,
)


_HDROADGEOLINELIST = _descriptor.Descriptor(
  name='HdRoadGeoLineList',
  full_name='nio.ad.messages.HdRoadGeoLineList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='road_geo_line_list', full_name='nio.ad.messages.HdRoadGeoLineList.road_geo_line_list', index=0,
      number=1, type=11, cpp_type=10, label=3,
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
  serialized_start=280,
  serialized_end=359,
)

_HDROADGEOLINE.fields_by_name['shape_point'].message_type = common_dot_map__engine_dot_map__geometry__pb2._MAPPOLYLINE
_HDROADGEOLINELIST.fields_by_name['road_geo_line_list'].message_type = _HDROADGEOLINE
DESCRIPTOR.message_types_by_name['HdRoadGeoLine'] = _HDROADGEOLINE
DESCRIPTOR.message_types_by_name['HdRoadGeoLineList'] = _HDROADGEOLINELIST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

HdRoadGeoLine = _reflection.GeneratedProtocolMessageType('HdRoadGeoLine', (_message.Message,), {
  'DESCRIPTOR' : _HDROADGEOLINE,
  '__module__' : 'common.map_engine.hd_road_geo_line_pb2'
  # @@protoc_insertion_point(class_scope:nio.ad.messages.HdRoadGeoLine)
  })
_sym_db.RegisterMessage(HdRoadGeoLine)

HdRoadGeoLineList = _reflection.GeneratedProtocolMessageType('HdRoadGeoLineList', (_message.Message,), {
  'DESCRIPTOR' : _HDROADGEOLINELIST,
  '__module__' : 'common.map_engine.hd_road_geo_line_pb2'
  # @@protoc_insertion_point(class_scope:nio.ad.messages.HdRoadGeoLineList)
  })
_sym_db.RegisterMessage(HdRoadGeoLineList)


_HDROADGEOLINE.fields_by_name['shape_point_offset']._options = None
# @@protoc_insertion_point(module_scope)

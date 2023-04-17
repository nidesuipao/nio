# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: common/map_engine/hd_traffic_sign.proto

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
  name='common/map_engine/hd_traffic_sign.proto',
  package='nio.ad.messages',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n\'common/map_engine/hd_traffic_sign.proto\x12\x0fnio.ad.messages\x1a$common/map_engine/map_geometry.proto\"\xcc\x03\n\rHdTrafficSign\x12\n\n\x02id\x18\x01 \x01(\x04\x12,\n\x07surface\x18\x02 \x01(\x0b\x32\x1b.nio.ad.messages.MapPolygon\x12\x31\n\x04type\x18\x03 \x01(\x0e\x32#.nio.ad.messages.HdTrafficSign.Type\x12\x0f\n\x07heading\x18\x04 \x01(\x01\x12\x0f\n\x07lane_id\x18\x05 \x03(\x04\x12)\n\x06\x63\x65nter\x18\x06 \x01(\x0b\x32\x19.nio.ad.messages.MapPoint\"\x80\x02\n\x04Type\x12\x12\n\x0eGENERAL_HAZARD\x10\x00\x12\x0e\n\nROAD_WORKS\x10\x06\x12\t\n\x05YIELD\x10 \x12\x08\n\x04STOP\x10!\x12\x11\n\rNO_OVERTAKING\x10.\x12\x15\n\x11NO_OVERTAKING_END\x10/\x12\x1a\n\x16PRIORITY_OVER_ONCOMING\x10Q\x12\x0f\n\x0bSPEED_LIMIT\x10W\x12\x13\n\x0fSPEED_LIMIT_END\x10X\x12\x18\n\x14\x41\x44VISORY_SPEED_LIMIT\x10h\x12\x18\n\x14VARIABLE_SPEED_LIMIT\x10k\x12\x0c\n\x08VARIABLE\x10l\x12\x11\n\x0c\x44O_NOT_ENTER\x10\x8b\x01\"N\n\x11HdTrafficSignList\x12\x39\n\x11traffic_sign_list\x18\x01 \x03(\x0b\x32\x1e.nio.ad.messages.HdTrafficSign')
  ,
  dependencies=[common_dot_map__engine_dot_map__geometry__pb2.DESCRIPTOR,])



_HDTRAFFICSIGN_TYPE = _descriptor.EnumDescriptor(
  name='Type',
  full_name='nio.ad.messages.HdTrafficSign.Type',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='GENERAL_HAZARD', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ROAD_WORKS', index=1, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='YIELD', index=2, number=32,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STOP', index=3, number=33,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NO_OVERTAKING', index=4, number=46,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NO_OVERTAKING_END', index=5, number=47,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PRIORITY_OVER_ONCOMING', index=6, number=81,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SPEED_LIMIT', index=7, number=87,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SPEED_LIMIT_END', index=8, number=88,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ADVISORY_SPEED_LIMIT', index=9, number=104,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VARIABLE_SPEED_LIMIT', index=10, number=107,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VARIABLE', index=11, number=108,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DO_NOT_ENTER', index=12, number=139,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=303,
  serialized_end=559,
)
_sym_db.RegisterEnumDescriptor(_HDTRAFFICSIGN_TYPE)


_HDTRAFFICSIGN = _descriptor.Descriptor(
  name='HdTrafficSign',
  full_name='nio.ad.messages.HdTrafficSign',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='nio.ad.messages.HdTrafficSign.id', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='surface', full_name='nio.ad.messages.HdTrafficSign.surface', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='nio.ad.messages.HdTrafficSign.type', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='heading', full_name='nio.ad.messages.HdTrafficSign.heading', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lane_id', full_name='nio.ad.messages.HdTrafficSign.lane_id', index=4,
      number=5, type=4, cpp_type=4, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='center', full_name='nio.ad.messages.HdTrafficSign.center', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _HDTRAFFICSIGN_TYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=99,
  serialized_end=559,
)


_HDTRAFFICSIGNLIST = _descriptor.Descriptor(
  name='HdTrafficSignList',
  full_name='nio.ad.messages.HdTrafficSignList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='traffic_sign_list', full_name='nio.ad.messages.HdTrafficSignList.traffic_sign_list', index=0,
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
  serialized_start=561,
  serialized_end=639,
)

_HDTRAFFICSIGN.fields_by_name['surface'].message_type = common_dot_map__engine_dot_map__geometry__pb2._MAPPOLYGON
_HDTRAFFICSIGN.fields_by_name['type'].enum_type = _HDTRAFFICSIGN_TYPE
_HDTRAFFICSIGN.fields_by_name['center'].message_type = common_dot_map__engine_dot_map__geometry__pb2._MAPPOINT
_HDTRAFFICSIGN_TYPE.containing_type = _HDTRAFFICSIGN
_HDTRAFFICSIGNLIST.fields_by_name['traffic_sign_list'].message_type = _HDTRAFFICSIGN
DESCRIPTOR.message_types_by_name['HdTrafficSign'] = _HDTRAFFICSIGN
DESCRIPTOR.message_types_by_name['HdTrafficSignList'] = _HDTRAFFICSIGNLIST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

HdTrafficSign = _reflection.GeneratedProtocolMessageType('HdTrafficSign', (_message.Message,), {
  'DESCRIPTOR' : _HDTRAFFICSIGN,
  '__module__' : 'common.map_engine.hd_traffic_sign_pb2'
  # @@protoc_insertion_point(class_scope:nio.ad.messages.HdTrafficSign)
  })
_sym_db.RegisterMessage(HdTrafficSign)

HdTrafficSignList = _reflection.GeneratedProtocolMessageType('HdTrafficSignList', (_message.Message,), {
  'DESCRIPTOR' : _HDTRAFFICSIGNLIST,
  '__module__' : 'common.map_engine.hd_traffic_sign_pb2'
  # @@protoc_insertion_point(class_scope:nio.ad.messages.HdTrafficSignList)
  })
_sym_db.RegisterMessage(HdTrafficSignList)


# @@protoc_insertion_point(module_scope)

# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: common/map_engine/hd_map.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from common.map_engine import hd_lane_pb2 as common_dot_map__engine_dot_hd__lane__pb2
from common.map_engine import hd_lane_boundary_pb2 as common_dot_map__engine_dot_hd__lane__boundary__pb2
from common.map_engine import hd_lane_group_pb2 as common_dot_map__engine_dot_hd__lane__group__pb2
from common.map_engine import hd_link_info_pb2 as common_dot_map__engine_dot_hd__link__info__pb2
from common.map_engine import hd_crosswalk_pb2 as common_dot_map__engine_dot_hd__crosswalk__pb2
from common.map_engine import hd_junction_pb2 as common_dot_map__engine_dot_hd__junction__pb2
from common.map_engine import hd_pole_pb2 as common_dot_map__engine_dot_hd__pole__pb2
from common.map_engine import hd_road_geo_line_pb2 as common_dot_map__engine_dot_hd__road__geo__line__pb2
from common.map_engine import hd_traffic_light_pb2 as common_dot_map__engine_dot_hd__traffic__light__pb2
from common.map_engine import hd_traffic_sign_pb2 as common_dot_map__engine_dot_hd__traffic__sign__pb2
from common.map_engine import hd_stop_line_pb2 as common_dot_map__engine_dot_hd__stop__line__pb2
from common.map_engine import hd_parking_area_pb2 as common_dot_map__engine_dot_hd__parking__area__pb2
from common.map_engine import hd_waiting_zone_pb2 as common_dot_map__engine_dot_hd__waiting__zone__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='common/map_engine/hd_map.proto',
  package='nio.ad.messages',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n\x1e\x63ommon/map_engine/hd_map.proto\x12\x0fnio.ad.messages\x1a\x1f\x63ommon/map_engine/hd_lane.proto\x1a(common/map_engine/hd_lane_boundary.proto\x1a%common/map_engine/hd_lane_group.proto\x1a$common/map_engine/hd_link_info.proto\x1a$common/map_engine/hd_crosswalk.proto\x1a#common/map_engine/hd_junction.proto\x1a\x1f\x63ommon/map_engine/hd_pole.proto\x1a(common/map_engine/hd_road_geo_line.proto\x1a(common/map_engine/hd_traffic_light.proto\x1a\'common/map_engine/hd_traffic_sign.proto\x1a$common/map_engine/hd_stop_line.proto\x1a\'common/map_engine/hd_parking_area.proto\x1a\'common/map_engine/hd_waiting_zone.proto\"\xfd\x06\n\x05HdMap\x12\x35\n\x0flane_group_list\x18\x01 \x03(\x0b\x32\x1c.nio.ad.messages.HdLaneGroup\x12*\n\tlane_list\x18\x02 \x03(\x0b\x32\x17.nio.ad.messages.HdLane\x12;\n\x12lane_boundary_list\x18\x03 \x03(\x0b\x32\x1f.nio.ad.messages.HdLaneBoundary\x12.\n\tlink_list\x18\x04 \x03(\x0b\x32\x1b.nio.ad.messages.HdLinkInfo\x12\x34\n\x0e\x63rosswalk_list\x18\x05 \x03(\x0b\x32\x1c.nio.ad.messages.HdCrosswalk\x12\x32\n\rjunction_list\x18\x06 \x03(\x0b\x32\x1b.nio.ad.messages.HdJunction\x12*\n\tpole_list\x18\x07 \x03(\x0b\x32\x17.nio.ad.messages.HdPole\x12;\n\x12traffic_light_list\x18\x08 \x03(\x0b\x32\x1f.nio.ad.messages.HdTrafficLight\x12\x39\n\x11traffic_sign_list\x18\t \x03(\x0b\x32\x1e.nio.ad.messages.HdTrafficSign\x12:\n\x12road_geo_line_list\x18\n \x03(\x0b\x32\x1e.nio.ad.messages.HdRoadGeoLine\x12\x33\n\x0estop_line_list\x18\x0b \x03(\x0b\x32\x1b.nio.ad.messages.HdStopLine\x12\x15\n\rmap_tile_hash\x18\x0c \x01(\t\x12\x13\n\x0bmap_version\x18\r \x01(\x05\x12 \n\x18\x64ynamic_map_info_counter\x18\x10 \x01(\t\x12\x39\n\x11parking_area_list\x18\x0e \x03(\x0b\x32\x1e.nio.ad.messages.HdParkingArea\x12\x39\n\x11waiting_zone_list\x18\x0f \x03(\x0b\x32\x1e.nio.ad.messages.HdWaitingZone\x12\x1a\n\x0epublish_ptp_ts\x18\xfb\xff\xff\xff\x01 \x01(\x04\x12\x18\n\x0cpublisher_id\x18\xfd\xff\xff\xff\x01 \x01(\t\x12\x13\n\x07\x63ounter\x18\xfe\xff\xff\xff\x01 \x01(\x04\x12\x16\n\npublish_ts\x18\xff\xff\xff\xff\x01 \x01(\x04')
  ,
  dependencies=[common_dot_map__engine_dot_hd__lane__pb2.DESCRIPTOR,common_dot_map__engine_dot_hd__lane__boundary__pb2.DESCRIPTOR,common_dot_map__engine_dot_hd__lane__group__pb2.DESCRIPTOR,common_dot_map__engine_dot_hd__link__info__pb2.DESCRIPTOR,common_dot_map__engine_dot_hd__crosswalk__pb2.DESCRIPTOR,common_dot_map__engine_dot_hd__junction__pb2.DESCRIPTOR,common_dot_map__engine_dot_hd__pole__pb2.DESCRIPTOR,common_dot_map__engine_dot_hd__road__geo__line__pb2.DESCRIPTOR,common_dot_map__engine_dot_hd__traffic__light__pb2.DESCRIPTOR,common_dot_map__engine_dot_hd__traffic__sign__pb2.DESCRIPTOR,common_dot_map__engine_dot_hd__stop__line__pb2.DESCRIPTOR,common_dot_map__engine_dot_hd__parking__area__pb2.DESCRIPTOR,common_dot_map__engine_dot_hd__waiting__zone__pb2.DESCRIPTOR,])




_HDMAP = _descriptor.Descriptor(
  name='HdMap',
  full_name='nio.ad.messages.HdMap',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='lane_group_list', full_name='nio.ad.messages.HdMap.lane_group_list', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lane_list', full_name='nio.ad.messages.HdMap.lane_list', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lane_boundary_list', full_name='nio.ad.messages.HdMap.lane_boundary_list', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='link_list', full_name='nio.ad.messages.HdMap.link_list', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='crosswalk_list', full_name='nio.ad.messages.HdMap.crosswalk_list', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='junction_list', full_name='nio.ad.messages.HdMap.junction_list', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pole_list', full_name='nio.ad.messages.HdMap.pole_list', index=6,
      number=7, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='traffic_light_list', full_name='nio.ad.messages.HdMap.traffic_light_list', index=7,
      number=8, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='traffic_sign_list', full_name='nio.ad.messages.HdMap.traffic_sign_list', index=8,
      number=9, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='road_geo_line_list', full_name='nio.ad.messages.HdMap.road_geo_line_list', index=9,
      number=10, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='stop_line_list', full_name='nio.ad.messages.HdMap.stop_line_list', index=10,
      number=11, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='map_tile_hash', full_name='nio.ad.messages.HdMap.map_tile_hash', index=11,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='map_version', full_name='nio.ad.messages.HdMap.map_version', index=12,
      number=13, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dynamic_map_info_counter', full_name='nio.ad.messages.HdMap.dynamic_map_info_counter', index=13,
      number=16, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='parking_area_list', full_name='nio.ad.messages.HdMap.parking_area_list', index=14,
      number=14, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='waiting_zone_list', full_name='nio.ad.messages.HdMap.waiting_zone_list', index=15,
      number=15, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='publish_ptp_ts', full_name='nio.ad.messages.HdMap.publish_ptp_ts', index=16,
      number=536870907, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='publisher_id', full_name='nio.ad.messages.HdMap.publisher_id', index=17,
      number=536870909, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='counter', full_name='nio.ad.messages.HdMap.counter', index=18,
      number=536870910, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='publish_ts', full_name='nio.ad.messages.HdMap.publish_ts', index=19,
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
  serialized_start=557,
  serialized_end=1450,
)

_HDMAP.fields_by_name['lane_group_list'].message_type = common_dot_map__engine_dot_hd__lane__group__pb2._HDLANEGROUP
_HDMAP.fields_by_name['lane_list'].message_type = common_dot_map__engine_dot_hd__lane__pb2._HDLANE
_HDMAP.fields_by_name['lane_boundary_list'].message_type = common_dot_map__engine_dot_hd__lane__boundary__pb2._HDLANEBOUNDARY
_HDMAP.fields_by_name['link_list'].message_type = common_dot_map__engine_dot_hd__link__info__pb2._HDLINKINFO
_HDMAP.fields_by_name['crosswalk_list'].message_type = common_dot_map__engine_dot_hd__crosswalk__pb2._HDCROSSWALK
_HDMAP.fields_by_name['junction_list'].message_type = common_dot_map__engine_dot_hd__junction__pb2._HDJUNCTION
_HDMAP.fields_by_name['pole_list'].message_type = common_dot_map__engine_dot_hd__pole__pb2._HDPOLE
_HDMAP.fields_by_name['traffic_light_list'].message_type = common_dot_map__engine_dot_hd__traffic__light__pb2._HDTRAFFICLIGHT
_HDMAP.fields_by_name['traffic_sign_list'].message_type = common_dot_map__engine_dot_hd__traffic__sign__pb2._HDTRAFFICSIGN
_HDMAP.fields_by_name['road_geo_line_list'].message_type = common_dot_map__engine_dot_hd__road__geo__line__pb2._HDROADGEOLINE
_HDMAP.fields_by_name['stop_line_list'].message_type = common_dot_map__engine_dot_hd__stop__line__pb2._HDSTOPLINE
_HDMAP.fields_by_name['parking_area_list'].message_type = common_dot_map__engine_dot_hd__parking__area__pb2._HDPARKINGAREA
_HDMAP.fields_by_name['waiting_zone_list'].message_type = common_dot_map__engine_dot_hd__waiting__zone__pb2._HDWAITINGZONE
DESCRIPTOR.message_types_by_name['HdMap'] = _HDMAP
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

HdMap = _reflection.GeneratedProtocolMessageType('HdMap', (_message.Message,), {
  'DESCRIPTOR' : _HDMAP,
  '__module__' : 'common.map_engine.hd_map_pb2'
  # @@protoc_insertion_point(class_scope:nio.ad.messages.HdMap)
  })
_sym_db.RegisterMessage(HdMap)


# @@protoc_insertion_point(module_scope)

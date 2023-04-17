# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: common/sensors/radar.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from common.sensors import radar_u360_tracker_pb2 as common_dot_sensors_dot_radar__u360__tracker__pb2
from common.sensors import radar_road_boundary_pb2 as common_dot_sensors_dot_radar__road__boundary__pb2
from common.sensors import radar_status_pb2 as common_dot_sensors_dot_radar__status__pb2
from common.sensors import radar_detection_pb2 as common_dot_sensors_dot_radar__detection__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='common/sensors/radar.proto',
  package='nio.ad.messages',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n\x1a\x63ommon/sensors/radar.proto\x12\x0fnio.ad.messages\x1a\'common/sensors/radar_u360_tracker.proto\x1a(common/sensors/radar_road_boundary.proto\x1a!common/sensors/radar_status.proto\x1a$common/sensors/radar_detection.proto\"n\n\nHeaderInfo\x12\x18\n\x10\x66usion_timestamp\x18\x01 \x02(\x04\x12\x14\n\x0c\x66usion_index\x18\x02 \x02(\r\x12\x17\n\x0fradar_timestamp\x18\x03 \x03(\x04\x12\x17\n\x0fradar_lookIndex\x18\x04 \x03(\r\"\xff\x03\n\x04View\x12+\n\x06header\x18\x01 \x02(\x0b\x32\x1b.nio.ad.messages.HeaderInfo\x12\x30\n\x06source\x18\x02 \x02(\x0e\x32 .nio.ad.messages.View.ViewSource\x12\x34\n\x0e\x66usion_tracker\x18\x03 \x02(\x0b\x32\x1c.nio.ad.messages.FusionTrack\x12\x31\n\x07sel_tar\x18\x04 \x02(\x0b\x32 .nio.ad.messages.TargetSelection\x12\x34\n\rroad_boundary\x18\x05 \x02(\x0b\x32\x1d.nio.ad.messages.RoadBoundary\x12\x32\n\x08rad_dets\x18\x06 \x02(\x0b\x32 .nio.ad.messages.RadarDetections\x12\x34\n\trads_fail\x18\x07 \x02(\x0b\x32!.nio.ad.messages.RadarFaultStatus\"\x8e\x01\n\nViewSource\x12\x15\n\x11VIEWSOURCE_VISION\x10\x00\x12\x14\n\x10VIEWSOURCE_LIDAR\x10\x01\x12\x14\n\x10VIEWSOURCE_RADAR\x10\x02\x12\x12\n\x0eVIEWSOURCE_USS\x10\x03\x12\x12\n\x0eVIEWSOURCE_SVC\x10\x04\x12\x15\n\x11VIEWSOURCE_FUSION\x10\x05')
  ,
  dependencies=[common_dot_sensors_dot_radar__u360__tracker__pb2.DESCRIPTOR,common_dot_sensors_dot_radar__road__boundary__pb2.DESCRIPTOR,common_dot_sensors_dot_radar__status__pb2.DESCRIPTOR,common_dot_sensors_dot_radar__detection__pb2.DESCRIPTOR,])



_VIEW_VIEWSOURCE = _descriptor.EnumDescriptor(
  name='ViewSource',
  full_name='nio.ad.messages.View.ViewSource',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='VIEWSOURCE_VISION', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VIEWSOURCE_LIDAR', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VIEWSOURCE_RADAR', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VIEWSOURCE_USS', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VIEWSOURCE_SVC', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VIEWSOURCE_FUSION', index=5, number=5,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=685,
  serialized_end=827,
)
_sym_db.RegisterEnumDescriptor(_VIEW_VIEWSOURCE)


_HEADERINFO = _descriptor.Descriptor(
  name='HeaderInfo',
  full_name='nio.ad.messages.HeaderInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='fusion_timestamp', full_name='nio.ad.messages.HeaderInfo.fusion_timestamp', index=0,
      number=1, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fusion_index', full_name='nio.ad.messages.HeaderInfo.fusion_index', index=1,
      number=2, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='radar_timestamp', full_name='nio.ad.messages.HeaderInfo.radar_timestamp', index=2,
      number=3, type=4, cpp_type=4, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='radar_lookIndex', full_name='nio.ad.messages.HeaderInfo.radar_lookIndex', index=3,
      number=4, type=13, cpp_type=3, label=3,
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
  serialized_start=203,
  serialized_end=313,
)


_VIEW = _descriptor.Descriptor(
  name='View',
  full_name='nio.ad.messages.View',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='nio.ad.messages.View.header', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='source', full_name='nio.ad.messages.View.source', index=1,
      number=2, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fusion_tracker', full_name='nio.ad.messages.View.fusion_tracker', index=2,
      number=3, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sel_tar', full_name='nio.ad.messages.View.sel_tar', index=3,
      number=4, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='road_boundary', full_name='nio.ad.messages.View.road_boundary', index=4,
      number=5, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rad_dets', full_name='nio.ad.messages.View.rad_dets', index=5,
      number=6, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rads_fail', full_name='nio.ad.messages.View.rads_fail', index=6,
      number=7, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _VIEW_VIEWSOURCE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=316,
  serialized_end=827,
)

_VIEW.fields_by_name['header'].message_type = _HEADERINFO
_VIEW.fields_by_name['source'].enum_type = _VIEW_VIEWSOURCE
_VIEW.fields_by_name['fusion_tracker'].message_type = common_dot_sensors_dot_radar__u360__tracker__pb2._FUSIONTRACK
_VIEW.fields_by_name['sel_tar'].message_type = common_dot_sensors_dot_radar__u360__tracker__pb2._TARGETSELECTION
_VIEW.fields_by_name['road_boundary'].message_type = common_dot_sensors_dot_radar__road__boundary__pb2._ROADBOUNDARY
_VIEW.fields_by_name['rad_dets'].message_type = common_dot_sensors_dot_radar__detection__pb2._RADARDETECTIONS
_VIEW.fields_by_name['rads_fail'].message_type = common_dot_sensors_dot_radar__status__pb2._RADARFAULTSTATUS
_VIEW_VIEWSOURCE.containing_type = _VIEW
DESCRIPTOR.message_types_by_name['HeaderInfo'] = _HEADERINFO
DESCRIPTOR.message_types_by_name['View'] = _VIEW
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

HeaderInfo = _reflection.GeneratedProtocolMessageType('HeaderInfo', (_message.Message,), {
  'DESCRIPTOR' : _HEADERINFO,
  '__module__' : 'common.sensors.radar_pb2'
  # @@protoc_insertion_point(class_scope:nio.ad.messages.HeaderInfo)
  })
_sym_db.RegisterMessage(HeaderInfo)

View = _reflection.GeneratedProtocolMessageType('View', (_message.Message,), {
  'DESCRIPTOR' : _VIEW,
  '__module__' : 'common.sensors.radar_pb2'
  # @@protoc_insertion_point(class_scope:nio.ad.messages.View)
  })
_sym_db.RegisterMessage(View)


# @@protoc_insertion_point(module_scope)

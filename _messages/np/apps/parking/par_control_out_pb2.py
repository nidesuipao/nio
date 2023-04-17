# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: np/apps/parking/par_control_out.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from common.vehicle_out import ads_actu_pb2 as common_dot_vehicle__out_dot_ads__actu__pb2
from np.apps.parking import par_base_pb2 as np_dot_apps_dot_parking_dot_par__base__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='np/apps/parking/par_control_out.proto',
  package='nio.ad.messages',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n%np/apps/parking/par_control_out.proto\x12\x0fnio.ad.messages\x1a!common/vehicle_out/ads_actu.proto\x1a\x1enp/apps/parking/par_base.proto\"\xdf\x02\n\x11ParkingControlSts\x12\x36\n\x0e\x63ontrol_status\x18\x01 \x01(\x0e\x32\x1e.nio.ad.messages.ControlStatus\x12\x39\n\x10long_control_out\x18\x02 \x01(\x0b\x32\x1f.nio.ad.messages.LngLwSpdCtrlIf\x12\x33\n\x0flat_control_out\x18\x03 \x01(\x0b\x32\x1a.nio.ad.messages.LatCtrlIf\x12,\n\tnode_info\x18\x04 \x01(\x0b\x32\x19.nio.ad.messages.NodeInfo\x12\x11\n\ttimestamp\x18\x05 \x01(\x04\x12\x1a\n\x0epublish_ptp_ts\x18\xfb\xff\xff\xff\x01 \x01(\x04\x12\x18\n\x0cpublisher_id\x18\xfd\xff\xff\xff\x01 \x01(\t\x12\x13\n\x07\x63ounter\x18\xfe\xff\xff\xff\x01 \x01(\x04\x12\x16\n\npublish_ts\x18\xff\xff\xff\xff\x01 \x01(\x04*\xd7\x01\n\rControlStatus\x12\x10\n\x0c\x43ONTROL_NONE\x10\x00\x12\x0e\n\nCONTROL_OK\x10\x01\x12\x11\n\rCONTROL_ERROR\x10\x02\x12\x16\n\x12\x43ONTROL_INIT_ERROR\x10\x03\x12\x19\n\x15\x43ONTROL_COMPUTE_ERROR\x10\x04\x12\x14\n\x10\x43ONTROL_FINISHED\x10\x05\x12\x13\n\x0f\x43ONTROL_PSAP_OK\x10\x06\x12\x18\n\x14\x43ONTROL_PSAP_FORWARD\x10\x07\x12\x19\n\x15\x43ONTROL_PSAP_BACKWARD\x10\x08')
  ,
  dependencies=[common_dot_vehicle__out_dot_ads__actu__pb2.DESCRIPTOR,np_dot_apps_dot_parking_dot_par__base__pb2.DESCRIPTOR,])

_CONTROLSTATUS = _descriptor.EnumDescriptor(
  name='ControlStatus',
  full_name='nio.ad.messages.ControlStatus',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='CONTROL_NONE', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CONTROL_OK', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CONTROL_ERROR', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CONTROL_INIT_ERROR', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CONTROL_COMPUTE_ERROR', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CONTROL_FINISHED', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CONTROL_PSAP_OK', index=6, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CONTROL_PSAP_FORWARD', index=7, number=7,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CONTROL_PSAP_BACKWARD', index=8, number=8,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=480,
  serialized_end=695,
)
_sym_db.RegisterEnumDescriptor(_CONTROLSTATUS)

ControlStatus = enum_type_wrapper.EnumTypeWrapper(_CONTROLSTATUS)
CONTROL_NONE = 0
CONTROL_OK = 1
CONTROL_ERROR = 2
CONTROL_INIT_ERROR = 3
CONTROL_COMPUTE_ERROR = 4
CONTROL_FINISHED = 5
CONTROL_PSAP_OK = 6
CONTROL_PSAP_FORWARD = 7
CONTROL_PSAP_BACKWARD = 8



_PARKINGCONTROLSTS = _descriptor.Descriptor(
  name='ParkingControlSts',
  full_name='nio.ad.messages.ParkingControlSts',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='control_status', full_name='nio.ad.messages.ParkingControlSts.control_status', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='long_control_out', full_name='nio.ad.messages.ParkingControlSts.long_control_out', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lat_control_out', full_name='nio.ad.messages.ParkingControlSts.lat_control_out', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='node_info', full_name='nio.ad.messages.ParkingControlSts.node_info', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='nio.ad.messages.ParkingControlSts.timestamp', index=4,
      number=5, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='publish_ptp_ts', full_name='nio.ad.messages.ParkingControlSts.publish_ptp_ts', index=5,
      number=536870907, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='publisher_id', full_name='nio.ad.messages.ParkingControlSts.publisher_id', index=6,
      number=536870909, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='counter', full_name='nio.ad.messages.ParkingControlSts.counter', index=7,
      number=536870910, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='publish_ts', full_name='nio.ad.messages.ParkingControlSts.publish_ts', index=8,
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
  serialized_start=126,
  serialized_end=477,
)

_PARKINGCONTROLSTS.fields_by_name['control_status'].enum_type = _CONTROLSTATUS
_PARKINGCONTROLSTS.fields_by_name['long_control_out'].message_type = common_dot_vehicle__out_dot_ads__actu__pb2._LNGLWSPDCTRLIF
_PARKINGCONTROLSTS.fields_by_name['lat_control_out'].message_type = common_dot_vehicle__out_dot_ads__actu__pb2._LATCTRLIF
_PARKINGCONTROLSTS.fields_by_name['node_info'].message_type = np_dot_apps_dot_parking_dot_par__base__pb2._NODEINFO
DESCRIPTOR.message_types_by_name['ParkingControlSts'] = _PARKINGCONTROLSTS
DESCRIPTOR.enum_types_by_name['ControlStatus'] = _CONTROLSTATUS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ParkingControlSts = _reflection.GeneratedProtocolMessageType('ParkingControlSts', (_message.Message,), {
  'DESCRIPTOR' : _PARKINGCONTROLSTS,
  '__module__' : 'np.apps.parking.par_control_out_pb2'
  # @@protoc_insertion_point(class_scope:nio.ad.messages.ParkingControlSts)
  })
_sym_db.RegisterMessage(ParkingControlSts)


# @@protoc_insertion_point(module_scope)

# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: np/apps/parking_perception_command.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from common.perception import svc_exceptions_pb2 as common_dot_perception_dot_svc__exceptions__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='np/apps/parking_perception_command.proto',
  package='nio.ad.messages',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n(np/apps/parking_perception_command.proto\x12\x0fnio.ad.messages\x1a&common/perception/svc_exceptions.proto\"\xba\x05\n\x18ParkingPerceptionCommand\x12V\n\rpark_cmd_type\x18\x01 \x01(\x0e\x32?.nio.ad.messages.ParkingPerceptionCommand.ParkingPerceptionType\x12\x18\n\x10slot_track_index\x18\x02 \x01(\x05\x12\x15\n\rpsap_vehpos_x\x18\x03 \x01(\x02\x12\x15\n\rpsap_vehpos_y\x18\x04 \x01(\x02\x12\x15\n\rpsap_vehpos_z\x18\x05 \x01(\x02\x12\x14\n\x0cpsap_veh_psi\x18\x06 \x01(\x02\x12Q\n\x10svc_fault_clears\x18\x07 \x03(\x0b\x32\x37.nio.ad.messages.ParkingPerceptionCommand.SVCFaultClear\x12\x1a\n\x0epublish_ptp_ts\x18\xfb\xff\xff\xff\x01 \x01(\x04\x12\x18\n\x0cpublisher_id\x18\xfd\xff\xff\xff\x01 \x01(\t\x12\x13\n\x07\x63ounter\x18\xfe\xff\xff\xff\x01 \x01(\x04\x12\x16\n\npublish_ts\x18\xff\xff\xff\xff\x01 \x01(\x04\x1ar\n\rSVCFaultClear\x12;\n\nfault_type\x18\x01 \x02(\x0e\x32\'.nio.ad.messages.SVCPerceptionFaultType\x12\x12\n\nfault_code\x18\x02 \x02(\x05\x12\x10\n\x08reserved\x18\x03 \x01(\x05\"\xa6\x01\n\x15ParkingPerceptionType\x12\x0c\n\x08TYPE_OFF\x10\x00\x12\x14\n\x10TYPE_SLOT_SEARCH\x10\x01\x12\x13\n\x0fTYPE_SLOT_TRACK\x10\x02\x12\x13\n\x0fTYPE_POWER_SWAP\x10\x03\x12\x19\n\x15TYPE_POWER_SWAP_TRACK\x10\x04\x12\x11\n\rTYPE_RESERED1\x10\x05\x12\x11\n\rTYPE_RESERED2\x10\x06')
  ,
  dependencies=[common_dot_perception_dot_svc__exceptions__pb2.DESCRIPTOR,])



_PARKINGPERCEPTIONCOMMAND_PARKINGPERCEPTIONTYPE = _descriptor.EnumDescriptor(
  name='ParkingPerceptionType',
  full_name='nio.ad.messages.ParkingPerceptionCommand.ParkingPerceptionType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='TYPE_OFF', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TYPE_SLOT_SEARCH', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TYPE_SLOT_TRACK', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TYPE_POWER_SWAP', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TYPE_POWER_SWAP_TRACK', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TYPE_RESERED1', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TYPE_RESERED2', index=6, number=6,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=634,
  serialized_end=800,
)
_sym_db.RegisterEnumDescriptor(_PARKINGPERCEPTIONCOMMAND_PARKINGPERCEPTIONTYPE)


_PARKINGPERCEPTIONCOMMAND_SVCFAULTCLEAR = _descriptor.Descriptor(
  name='SVCFaultClear',
  full_name='nio.ad.messages.ParkingPerceptionCommand.SVCFaultClear',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='fault_type', full_name='nio.ad.messages.ParkingPerceptionCommand.SVCFaultClear.fault_type', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fault_code', full_name='nio.ad.messages.ParkingPerceptionCommand.SVCFaultClear.fault_code', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='reserved', full_name='nio.ad.messages.ParkingPerceptionCommand.SVCFaultClear.reserved', index=2,
      number=3, type=5, cpp_type=1, label=1,
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
  serialized_start=517,
  serialized_end=631,
)

_PARKINGPERCEPTIONCOMMAND = _descriptor.Descriptor(
  name='ParkingPerceptionCommand',
  full_name='nio.ad.messages.ParkingPerceptionCommand',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='park_cmd_type', full_name='nio.ad.messages.ParkingPerceptionCommand.park_cmd_type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='slot_track_index', full_name='nio.ad.messages.ParkingPerceptionCommand.slot_track_index', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='psap_vehpos_x', full_name='nio.ad.messages.ParkingPerceptionCommand.psap_vehpos_x', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='psap_vehpos_y', full_name='nio.ad.messages.ParkingPerceptionCommand.psap_vehpos_y', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='psap_vehpos_z', full_name='nio.ad.messages.ParkingPerceptionCommand.psap_vehpos_z', index=4,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='psap_veh_psi', full_name='nio.ad.messages.ParkingPerceptionCommand.psap_veh_psi', index=5,
      number=6, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='svc_fault_clears', full_name='nio.ad.messages.ParkingPerceptionCommand.svc_fault_clears', index=6,
      number=7, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='publish_ptp_ts', full_name='nio.ad.messages.ParkingPerceptionCommand.publish_ptp_ts', index=7,
      number=536870907, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='publisher_id', full_name='nio.ad.messages.ParkingPerceptionCommand.publisher_id', index=8,
      number=536870909, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='counter', full_name='nio.ad.messages.ParkingPerceptionCommand.counter', index=9,
      number=536870910, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='publish_ts', full_name='nio.ad.messages.ParkingPerceptionCommand.publish_ts', index=10,
      number=536870911, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_PARKINGPERCEPTIONCOMMAND_SVCFAULTCLEAR, ],
  enum_types=[
    _PARKINGPERCEPTIONCOMMAND_PARKINGPERCEPTIONTYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=102,
  serialized_end=800,
)

_PARKINGPERCEPTIONCOMMAND_SVCFAULTCLEAR.fields_by_name['fault_type'].enum_type = common_dot_perception_dot_svc__exceptions__pb2._SVCPERCEPTIONFAULTTYPE
_PARKINGPERCEPTIONCOMMAND_SVCFAULTCLEAR.containing_type = _PARKINGPERCEPTIONCOMMAND
_PARKINGPERCEPTIONCOMMAND.fields_by_name['park_cmd_type'].enum_type = _PARKINGPERCEPTIONCOMMAND_PARKINGPERCEPTIONTYPE
_PARKINGPERCEPTIONCOMMAND.fields_by_name['svc_fault_clears'].message_type = _PARKINGPERCEPTIONCOMMAND_SVCFAULTCLEAR
_PARKINGPERCEPTIONCOMMAND_PARKINGPERCEPTIONTYPE.containing_type = _PARKINGPERCEPTIONCOMMAND
DESCRIPTOR.message_types_by_name['ParkingPerceptionCommand'] = _PARKINGPERCEPTIONCOMMAND
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ParkingPerceptionCommand = _reflection.GeneratedProtocolMessageType('ParkingPerceptionCommand', (_message.Message,), {

  'SVCFaultClear' : _reflection.GeneratedProtocolMessageType('SVCFaultClear', (_message.Message,), {
    'DESCRIPTOR' : _PARKINGPERCEPTIONCOMMAND_SVCFAULTCLEAR,
    '__module__' : 'np.apps.parking_perception_command_pb2'
    # @@protoc_insertion_point(class_scope:nio.ad.messages.ParkingPerceptionCommand.SVCFaultClear)
    })
  ,
  'DESCRIPTOR' : _PARKINGPERCEPTIONCOMMAND,
  '__module__' : 'np.apps.parking_perception_command_pb2'
  # @@protoc_insertion_point(class_scope:nio.ad.messages.ParkingPerceptionCommand)
  })
_sym_db.RegisterMessage(ParkingPerceptionCommand)
_sym_db.RegisterMessage(ParkingPerceptionCommand.SVCFaultClear)


# @@protoc_insertion_point(module_scope)

# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: common/nop/nop_vehicleout.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='common/nop/nop_vehicleout.proto',
  package='nio.ad.messages',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n\x1f\x63ommon/nop/nop_vehicleout.proto\x12\x0fnio.ad.messages\"\x96\x03\n\rNopVehicleOut\x12\x13\n\x0bnop_alc_sts\x18\x01 \x01(\r\x12\x1b\n\x13nop_colllision_risk\x18\x02 \x01(\r\x12-\n%nop_freeSpace_intrusion_at_standstill\x18\x03 \x01(\x08\x12+\n#nop_freeSpace_intrusion_go_notifier\x18\x04 \x01(\x08\x12\x1a\n\x12nop_lat_ctrl_tarLe\x18\x05 \x01(\r\x12\x1a\n\x12nop_lat_ctrl_tarRi\x18\x06 \x01(\r\x12\x19\n\x11nop_long_ctrl_tar\x18\x07 \x01(\r\x12\x1e\n\x16nop_turn_indicator_req\x18\x08 \x01(\r\x12\x0f\n\x07nop_wti\x18\t \x01(\r\x12\x10\n\x08reserved\x18\x63 \x03(\x02\x12\x1a\n\x0epublish_ptp_ts\x18\xfb\xff\xff\xff\x01 \x01(\x04\x12\x18\n\x0cpublisher_id\x18\xfd\xff\xff\xff\x01 \x01(\t\x12\x13\n\x07\x63ounter\x18\xfe\xff\xff\xff\x01 \x01(\x04\x12\x16\n\npublish_ts\x18\xff\xff\xff\xff\x01 \x01(\x04')
)




_NOPVEHICLEOUT = _descriptor.Descriptor(
  name='NopVehicleOut',
  full_name='nio.ad.messages.NopVehicleOut',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='nop_alc_sts', full_name='nio.ad.messages.NopVehicleOut.nop_alc_sts', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='nop_colllision_risk', full_name='nio.ad.messages.NopVehicleOut.nop_colllision_risk', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='nop_freeSpace_intrusion_at_standstill', full_name='nio.ad.messages.NopVehicleOut.nop_freeSpace_intrusion_at_standstill', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='nop_freeSpace_intrusion_go_notifier', full_name='nio.ad.messages.NopVehicleOut.nop_freeSpace_intrusion_go_notifier', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='nop_lat_ctrl_tarLe', full_name='nio.ad.messages.NopVehicleOut.nop_lat_ctrl_tarLe', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='nop_lat_ctrl_tarRi', full_name='nio.ad.messages.NopVehicleOut.nop_lat_ctrl_tarRi', index=5,
      number=6, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='nop_long_ctrl_tar', full_name='nio.ad.messages.NopVehicleOut.nop_long_ctrl_tar', index=6,
      number=7, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='nop_turn_indicator_req', full_name='nio.ad.messages.NopVehicleOut.nop_turn_indicator_req', index=7,
      number=8, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='nop_wti', full_name='nio.ad.messages.NopVehicleOut.nop_wti', index=8,
      number=9, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='reserved', full_name='nio.ad.messages.NopVehicleOut.reserved', index=9,
      number=99, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='publish_ptp_ts', full_name='nio.ad.messages.NopVehicleOut.publish_ptp_ts', index=10,
      number=536870907, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='publisher_id', full_name='nio.ad.messages.NopVehicleOut.publisher_id', index=11,
      number=536870909, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='counter', full_name='nio.ad.messages.NopVehicleOut.counter', index=12,
      number=536870910, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='publish_ts', full_name='nio.ad.messages.NopVehicleOut.publish_ts', index=13,
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
  serialized_start=53,
  serialized_end=459,
)

DESCRIPTOR.message_types_by_name['NopVehicleOut'] = _NOPVEHICLEOUT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

NopVehicleOut = _reflection.GeneratedProtocolMessageType('NopVehicleOut', (_message.Message,), {
  'DESCRIPTOR' : _NOPVEHICLEOUT,
  '__module__' : 'common.nop.nop_vehicleout_pb2'
  # @@protoc_insertion_point(class_scope:nio.ad.messages.NopVehicleOut)
  })
_sym_db.RegisterMessage(NopVehicleOut)


# @@protoc_insertion_point(module_scope)

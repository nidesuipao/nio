# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: common/perception/svc_slots.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from common.perception import svc_base_pb2 as common_dot_perception_dot_svc__base__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='common/perception/svc_slots.proto',
  package='nio.ad.messages',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n!common/perception/svc_slots.proto\x12\x0fnio.ad.messages\x1a common/perception/svc_base.proto\"\xc5\x07\n\x04Slot\x12\x12\n\nslot_index\x18\x01 \x01(\x05\x12&\n\x03pt1\x18\x02 \x01(\x0b\x32\x19.nio.ad.messages.SVCPoint\x12&\n\x03pt2\x18\x03 \x01(\x0b\x32\x19.nio.ad.messages.SVCPoint\x12&\n\x03pt3\x18\x04 \x01(\x0b\x32\x19.nio.ad.messages.SVCPoint\x12&\n\x03pt4\x18\x05 \x01(\x0b\x32\x19.nio.ad.messages.SVCPoint\x12*\n\x07veh_pos\x18\x06 \x01(\x0b\x32\x19.nio.ad.messages.SVCPoint\x12\x0f\n\x07veh_psi\x18\x07 \x01(\x02\x12\x11\n\tslot_prob\x18\x08 \x01(\x02\x12:\n\tslot_type\x18\t \x01(\x0e\x32\x1e.nio.ad.messages.Slot.SlotType:\x07UNKNOWN\x12@\n\x0bslot_status\x18\n \x01(\x0e\x32 .nio.ad.messages.Slot.SlotStatus:\tUNCERTAIN\x12\x12\n\nslot_angel\x18\x0b \x01(\x02\x12\x15\n\rslot_priority\x18\x0c \x01(\x05\x12\x15\n\rslot_distance\x18\r \x01(\x02\x12\x17\n\x0fslot_line_width\x18\x0e \x01(\x02\x12\x11\n\treserved1\x18\x0f \x01(\x05\x12\x11\n\treserved2\x18\x10 \x01(\x05\"\xce\x02\n\x08SlotType\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x11\n\rLEFT_PARALLEL\x10\x01\x12\x12\n\x0eRIGHT_PARALLEL\x10\x02\x12\x0e\n\nLEFT_CROSS\x10\x03\x12\x0f\n\x0bRIGHT_CROSS\x10\x04\x12\x11\n\rLEFT_PARK_OUT\x10\x05\x12\x12\n\x0eRIGHT_PARK_OUT\x10\x06\x12\x0f\n\x0bLEFT_ANGLED\x10\x07\x12\x10\n\x0cRIGHT_ANGLED\x10\x08\x12\x15\n\x11LEFT_USER_DEFINED\x10\t\x12\x16\n\x12RIGHT_USER_DEFINED\x10\n\x12\x13\n\x0fLEFT_MECHANICAL\x10\x0b\x12\x14\n\x10RIGHT_MECHANICAL\x10\x0c\x12\x17\n\x13SLOT_TYPE_RESERVED1\x10\r\x12\x17\n\x13SLOT_TYPE_RESERVED2\x10\x0e\x12\x17\n\x13SLOT_TYPE_RESERVED3\x10\x0f\"i\n\nSlotStatus\x12\r\n\tUNCERTAIN\x10\x00\x12\r\n\tAVAILABLE\x10\x01\x12\x11\n\rNOT_AVAILABLE\x10\x02\x12\x14\n\x10STATUS_RESERVED1\x10\x03\x12\x14\n\x10STATUS_RESERVED2\x10\x04\"r\n\nSlotResult\x12\x11\n\ttimestamp\x18\x01 \x01(\x04\x12$\n\x05slots\x18\x02 \x03(\x0b\x32\x15.nio.ad.messages.Slot\x12\x14\n\x0cpld_eserved1\x18\x03 \x01(\x05\x12\x15\n\rpld_Reserved2\x18\x04 \x01(\x05')
  ,
  dependencies=[common_dot_perception_dot_svc__base__pb2.DESCRIPTOR,])



_SLOT_SLOTTYPE = _descriptor.EnumDescriptor(
  name='SlotType',
  full_name='nio.ad.messages.Slot.SlotType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LEFT_PARALLEL', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RIGHT_PARALLEL', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LEFT_CROSS', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RIGHT_CROSS', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LEFT_PARK_OUT', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RIGHT_PARK_OUT', index=6, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LEFT_ANGLED', index=7, number=7,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RIGHT_ANGLED', index=8, number=8,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LEFT_USER_DEFINED', index=9, number=9,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RIGHT_USER_DEFINED', index=10, number=10,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LEFT_MECHANICAL', index=11, number=11,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RIGHT_MECHANICAL', index=12, number=12,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SLOT_TYPE_RESERVED1', index=13, number=13,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SLOT_TYPE_RESERVED2', index=14, number=14,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SLOT_TYPE_RESERVED3', index=15, number=15,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=613,
  serialized_end=947,
)
_sym_db.RegisterEnumDescriptor(_SLOT_SLOTTYPE)

_SLOT_SLOTSTATUS = _descriptor.EnumDescriptor(
  name='SlotStatus',
  full_name='nio.ad.messages.Slot.SlotStatus',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNCERTAIN', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AVAILABLE', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NOT_AVAILABLE', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STATUS_RESERVED1', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STATUS_RESERVED2', index=4, number=4,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=949,
  serialized_end=1054,
)
_sym_db.RegisterEnumDescriptor(_SLOT_SLOTSTATUS)


_SLOT = _descriptor.Descriptor(
  name='Slot',
  full_name='nio.ad.messages.Slot',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='slot_index', full_name='nio.ad.messages.Slot.slot_index', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pt1', full_name='nio.ad.messages.Slot.pt1', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pt2', full_name='nio.ad.messages.Slot.pt2', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pt3', full_name='nio.ad.messages.Slot.pt3', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pt4', full_name='nio.ad.messages.Slot.pt4', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='veh_pos', full_name='nio.ad.messages.Slot.veh_pos', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='veh_psi', full_name='nio.ad.messages.Slot.veh_psi', index=6,
      number=7, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='slot_prob', full_name='nio.ad.messages.Slot.slot_prob', index=7,
      number=8, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='slot_type', full_name='nio.ad.messages.Slot.slot_type', index=8,
      number=9, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='slot_status', full_name='nio.ad.messages.Slot.slot_status', index=9,
      number=10, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='slot_angel', full_name='nio.ad.messages.Slot.slot_angel', index=10,
      number=11, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='slot_priority', full_name='nio.ad.messages.Slot.slot_priority', index=11,
      number=12, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='slot_distance', full_name='nio.ad.messages.Slot.slot_distance', index=12,
      number=13, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='slot_line_width', full_name='nio.ad.messages.Slot.slot_line_width', index=13,
      number=14, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='reserved1', full_name='nio.ad.messages.Slot.reserved1', index=14,
      number=15, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='reserved2', full_name='nio.ad.messages.Slot.reserved2', index=15,
      number=16, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _SLOT_SLOTTYPE,
    _SLOT_SLOTSTATUS,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=89,
  serialized_end=1054,
)


_SLOTRESULT = _descriptor.Descriptor(
  name='SlotResult',
  full_name='nio.ad.messages.SlotResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='nio.ad.messages.SlotResult.timestamp', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='slots', full_name='nio.ad.messages.SlotResult.slots', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pld_eserved1', full_name='nio.ad.messages.SlotResult.pld_eserved1', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pld_Reserved2', full_name='nio.ad.messages.SlotResult.pld_Reserved2', index=3,
      number=4, type=5, cpp_type=1, label=1,
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
  serialized_start=1056,
  serialized_end=1170,
)

_SLOT.fields_by_name['pt1'].message_type = common_dot_perception_dot_svc__base__pb2._SVCPOINT
_SLOT.fields_by_name['pt2'].message_type = common_dot_perception_dot_svc__base__pb2._SVCPOINT
_SLOT.fields_by_name['pt3'].message_type = common_dot_perception_dot_svc__base__pb2._SVCPOINT
_SLOT.fields_by_name['pt4'].message_type = common_dot_perception_dot_svc__base__pb2._SVCPOINT
_SLOT.fields_by_name['veh_pos'].message_type = common_dot_perception_dot_svc__base__pb2._SVCPOINT
_SLOT.fields_by_name['slot_type'].enum_type = _SLOT_SLOTTYPE
_SLOT.fields_by_name['slot_status'].enum_type = _SLOT_SLOTSTATUS
_SLOT_SLOTTYPE.containing_type = _SLOT
_SLOT_SLOTSTATUS.containing_type = _SLOT
_SLOTRESULT.fields_by_name['slots'].message_type = _SLOT
DESCRIPTOR.message_types_by_name['Slot'] = _SLOT
DESCRIPTOR.message_types_by_name['SlotResult'] = _SLOTRESULT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Slot = _reflection.GeneratedProtocolMessageType('Slot', (_message.Message,), {
  'DESCRIPTOR' : _SLOT,
  '__module__' : 'common.perception.svc_slots_pb2'
  # @@protoc_insertion_point(class_scope:nio.ad.messages.Slot)
  })
_sym_db.RegisterMessage(Slot)

SlotResult = _reflection.GeneratedProtocolMessageType('SlotResult', (_message.Message,), {
  'DESCRIPTOR' : _SLOTRESULT,
  '__module__' : 'common.perception.svc_slots_pb2'
  # @@protoc_insertion_point(class_scope:nio.ad.messages.SlotResult)
  })
_sym_db.RegisterMessage(SlotResult)


# @@protoc_insertion_point(module_scope)

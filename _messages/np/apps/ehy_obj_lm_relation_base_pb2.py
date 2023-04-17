# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: np/apps/ehy_obj_lm_relation_base.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from common.perception import vision_road_detection_pb2 as common_dot_perception_dot_vision__road__detection__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='np/apps/ehy_obj_lm_relation_base.proto',
  package='nio.ad.messages',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n&np/apps/ehy_obj_lm_relation_base.proto\x12\x0fnio.ad.messages\x1a-common/perception/vision_road_detection.proto\"m\n\x08LMRelRes\x12\r\n\x05lm_id\x18\x01 \x01(\r\x12\x36\n\x0crelative_pos\x18\x02 \x01(\x0e\x32 .nio.ad.messages.ObjRelPosWithLM\x12\x0c\n\x04\x64ist\x18\x03 \x01(\x02\x12\x0c\n\x04\x63onf\x18\x04 \x01(\x02\"K\n\tObjRelRes\x12\x0e\n\x06obj_id\x18\x01 \x01(\r\x12.\n\x0blm_relation\x18\x02 \x03(\x0b\x32\x19.nio.ad.messages.LMRelRes\"t\n\x08ObjLMRel\x12\x36\n\x0eroad_detection\x18\x01 \x01(\x0b\x32\x1e.nio.ad.messages.RoadDetection\x12\x30\n\x0cpos_relation\x18\x02 \x03(\x0b\x32\x1a.nio.ad.messages.ObjRelRes*j\n\x0fObjRelPosWithLM\x12\x16\n\x12kObjRelPos_Unknown\x10\x00\x12\x13\n\x0fkObjRelPos_Left\x10\x01\x12\x14\n\x10kObjRelPos_Right\x10\x02\x12\x14\n\x10kObjRelPos_Cross\x10\x03')
  ,
  dependencies=[common_dot_perception_dot_vision__road__detection__pb2.DESCRIPTOR,])

_OBJRELPOSWITHLM = _descriptor.EnumDescriptor(
  name='ObjRelPosWithLM',
  full_name='nio.ad.messages.ObjRelPosWithLM',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='kObjRelPos_Unknown', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='kObjRelPos_Left', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='kObjRelPos_Right', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='kObjRelPos_Cross', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=412,
  serialized_end=518,
)
_sym_db.RegisterEnumDescriptor(_OBJRELPOSWITHLM)

ObjRelPosWithLM = enum_type_wrapper.EnumTypeWrapper(_OBJRELPOSWITHLM)
kObjRelPos_Unknown = 0
kObjRelPos_Left = 1
kObjRelPos_Right = 2
kObjRelPos_Cross = 3



_LMRELRES = _descriptor.Descriptor(
  name='LMRelRes',
  full_name='nio.ad.messages.LMRelRes',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='lm_id', full_name='nio.ad.messages.LMRelRes.lm_id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='relative_pos', full_name='nio.ad.messages.LMRelRes.relative_pos', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dist', full_name='nio.ad.messages.LMRelRes.dist', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='conf', full_name='nio.ad.messages.LMRelRes.conf', index=3,
      number=4, type=2, cpp_type=6, label=1,
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
  serialized_start=106,
  serialized_end=215,
)


_OBJRELRES = _descriptor.Descriptor(
  name='ObjRelRes',
  full_name='nio.ad.messages.ObjRelRes',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='obj_id', full_name='nio.ad.messages.ObjRelRes.obj_id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lm_relation', full_name='nio.ad.messages.ObjRelRes.lm_relation', index=1,
      number=2, type=11, cpp_type=10, label=3,
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
  serialized_start=217,
  serialized_end=292,
)


_OBJLMREL = _descriptor.Descriptor(
  name='ObjLMRel',
  full_name='nio.ad.messages.ObjLMRel',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='road_detection', full_name='nio.ad.messages.ObjLMRel.road_detection', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pos_relation', full_name='nio.ad.messages.ObjLMRel.pos_relation', index=1,
      number=2, type=11, cpp_type=10, label=3,
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
  serialized_start=294,
  serialized_end=410,
)

_LMRELRES.fields_by_name['relative_pos'].enum_type = _OBJRELPOSWITHLM
_OBJRELRES.fields_by_name['lm_relation'].message_type = _LMRELRES
_OBJLMREL.fields_by_name['road_detection'].message_type = common_dot_perception_dot_vision__road__detection__pb2._ROADDETECTION
_OBJLMREL.fields_by_name['pos_relation'].message_type = _OBJRELRES
DESCRIPTOR.message_types_by_name['LMRelRes'] = _LMRELRES
DESCRIPTOR.message_types_by_name['ObjRelRes'] = _OBJRELRES
DESCRIPTOR.message_types_by_name['ObjLMRel'] = _OBJLMREL
DESCRIPTOR.enum_types_by_name['ObjRelPosWithLM'] = _OBJRELPOSWITHLM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

LMRelRes = _reflection.GeneratedProtocolMessageType('LMRelRes', (_message.Message,), {
  'DESCRIPTOR' : _LMRELRES,
  '__module__' : 'np.apps.ehy_obj_lm_relation_base_pb2'
  # @@protoc_insertion_point(class_scope:nio.ad.messages.LMRelRes)
  })
_sym_db.RegisterMessage(LMRelRes)

ObjRelRes = _reflection.GeneratedProtocolMessageType('ObjRelRes', (_message.Message,), {
  'DESCRIPTOR' : _OBJRELRES,
  '__module__' : 'np.apps.ehy_obj_lm_relation_base_pb2'
  # @@protoc_insertion_point(class_scope:nio.ad.messages.ObjRelRes)
  })
_sym_db.RegisterMessage(ObjRelRes)

ObjLMRel = _reflection.GeneratedProtocolMessageType('ObjLMRel', (_message.Message,), {
  'DESCRIPTOR' : _OBJLMREL,
  '__module__' : 'np.apps.ehy_obj_lm_relation_base_pb2'
  # @@protoc_insertion_point(class_scope:nio.ad.messages.ObjLMRel)
  })
_sym_db.RegisterMessage(ObjLMRel)


# @@protoc_insertion_point(module_scope)

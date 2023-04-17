# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: np/apps/ehy_operation_outputs.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from common.lane_segment import lane_seg_event_pb2 as common_dot_lane__segment_dot_lane__seg__event__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='np/apps/ehy_operation_outputs.proto',
  package='nio.ad.messages',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n#np/apps/ehy_operation_outputs.proto\x12\x0fnio.ad.messages\x1a(common/lane_segment/lane_seg_event.proto\"\xd7\x01\n\x14\x46\x65\x61tureOperationInfo\x12G\n\x17\x66\x65\x61ture_operation_point\x18\x01 \x03(\x0b\x32&.nio.ad.messages.FeatureOperationPoint\x12\x13\n\x0braw_payload\x18\x02 \x01(\t\x12\x1a\n\x0epublish_ptp_ts\x18\xfb\xff\xff\xff\x01 \x01(\x04\x12\x18\n\x0cpublisher_id\x18\xfd\xff\xff\xff\x01 \x01(\t\x12\x13\n\x07\x63ounter\x18\xfe\xff\xff\xff\x01 \x01(\x04\x12\x16\n\npublish_ts\x18\xff\xff\xff\xff\x01 \x01(\x04\"\xf2\x01\n\x15\x46\x65\x61tureOperationPoint\x12\x10\n\x08is_valid\x18\x01 \x01(\x08\x12\x14\n\x0coffset_start\x18\x02 \x01(\x05\x12\x12\n\noffset_end\x18\x03 \x01(\x05\x12\x0e\n\x06linkid\x18\x04 \x01(\x04\x12\x14\n\x0c\x63urr_laneidx\x18\x05 \x01(\x05\x12\x38\n\x0f\x65vent_condition\x18\x06 \x01(\x0b\x32\x1f.nio.ad.messages.EventCondition\x12=\n\x0e\x61\x63tion_context\x18\x07 \x03(\x0b\x32%.nio.ad.messages.DrivingActionContext')
  ,
  dependencies=[common_dot_lane__segment_dot_lane__seg__event__pb2.DESCRIPTOR,])




_FEATUREOPERATIONINFO = _descriptor.Descriptor(
  name='FeatureOperationInfo',
  full_name='nio.ad.messages.FeatureOperationInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='feature_operation_point', full_name='nio.ad.messages.FeatureOperationInfo.feature_operation_point', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='raw_payload', full_name='nio.ad.messages.FeatureOperationInfo.raw_payload', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='publish_ptp_ts', full_name='nio.ad.messages.FeatureOperationInfo.publish_ptp_ts', index=2,
      number=536870907, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='publisher_id', full_name='nio.ad.messages.FeatureOperationInfo.publisher_id', index=3,
      number=536870909, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='counter', full_name='nio.ad.messages.FeatureOperationInfo.counter', index=4,
      number=536870910, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='publish_ts', full_name='nio.ad.messages.FeatureOperationInfo.publish_ts', index=5,
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
  serialized_start=99,
  serialized_end=314,
)


_FEATUREOPERATIONPOINT = _descriptor.Descriptor(
  name='FeatureOperationPoint',
  full_name='nio.ad.messages.FeatureOperationPoint',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='is_valid', full_name='nio.ad.messages.FeatureOperationPoint.is_valid', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='offset_start', full_name='nio.ad.messages.FeatureOperationPoint.offset_start', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='offset_end', full_name='nio.ad.messages.FeatureOperationPoint.offset_end', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='linkid', full_name='nio.ad.messages.FeatureOperationPoint.linkid', index=3,
      number=4, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='curr_laneidx', full_name='nio.ad.messages.FeatureOperationPoint.curr_laneidx', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='event_condition', full_name='nio.ad.messages.FeatureOperationPoint.event_condition', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='action_context', full_name='nio.ad.messages.FeatureOperationPoint.action_context', index=6,
      number=7, type=11, cpp_type=10, label=3,
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
  serialized_start=317,
  serialized_end=559,
)

_FEATUREOPERATIONINFO.fields_by_name['feature_operation_point'].message_type = _FEATUREOPERATIONPOINT
_FEATUREOPERATIONPOINT.fields_by_name['event_condition'].message_type = common_dot_lane__segment_dot_lane__seg__event__pb2._EVENTCONDITION
_FEATUREOPERATIONPOINT.fields_by_name['action_context'].message_type = common_dot_lane__segment_dot_lane__seg__event__pb2._DRIVINGACTIONCONTEXT
DESCRIPTOR.message_types_by_name['FeatureOperationInfo'] = _FEATUREOPERATIONINFO
DESCRIPTOR.message_types_by_name['FeatureOperationPoint'] = _FEATUREOPERATIONPOINT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

FeatureOperationInfo = _reflection.GeneratedProtocolMessageType('FeatureOperationInfo', (_message.Message,), {
  'DESCRIPTOR' : _FEATUREOPERATIONINFO,
  '__module__' : 'np.apps.ehy_operation_outputs_pb2'
  # @@protoc_insertion_point(class_scope:nio.ad.messages.FeatureOperationInfo)
  })
_sym_db.RegisterMessage(FeatureOperationInfo)

FeatureOperationPoint = _reflection.GeneratedProtocolMessageType('FeatureOperationPoint', (_message.Message,), {
  'DESCRIPTOR' : _FEATUREOPERATIONPOINT,
  '__module__' : 'np.apps.ehy_operation_outputs_pb2'
  # @@protoc_insertion_point(class_scope:nio.ad.messages.FeatureOperationPoint)
  })
_sym_db.RegisterMessage(FeatureOperationPoint)


# @@protoc_insertion_point(module_scope)

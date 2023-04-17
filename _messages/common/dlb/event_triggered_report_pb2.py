# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: common/dlb/event_triggered_report.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='common/dlb/event_triggered_report.proto',
  package='nio.ad.messages',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n\'common/dlb/event_triggered_report.proto\x12\x0fnio.ad.messages\"\xf6\x01\n\x11\x45ventTriggeredReq\x12\x17\n\x0ftriggered_event\x18\x01 \x01(\t\x12\x16\n\x0etriggered_time\x18\x02 \x01(\t\x12\x16\n\x0etriggered_uuid\x18\x03 \x01(\t\x12\x1b\n\x13triggered_missionid\x18\x04 \x01(\t\x12\x18\n\x10triggered_detail\x18\x05 \x01(\t\x12\x1a\n\x0epublish_ptp_ts\x18\xfb\xff\xff\xff\x01 \x01(\x04\x12\x18\n\x0cpublisher_id\x18\xfd\xff\xff\xff\x01 \x01(\t\x12\x13\n\x07\x63ounter\x18\xfe\xff\xff\xff\x01 \x01(\x04\x12\x16\n\npublish_ts\x18\xff\xff\xff\xff\x01 \x01(\x04')
)




_EVENTTRIGGEREDREQ = _descriptor.Descriptor(
  name='EventTriggeredReq',
  full_name='nio.ad.messages.EventTriggeredReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='triggered_event', full_name='nio.ad.messages.EventTriggeredReq.triggered_event', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='triggered_time', full_name='nio.ad.messages.EventTriggeredReq.triggered_time', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='triggered_uuid', full_name='nio.ad.messages.EventTriggeredReq.triggered_uuid', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='triggered_missionid', full_name='nio.ad.messages.EventTriggeredReq.triggered_missionid', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='triggered_detail', full_name='nio.ad.messages.EventTriggeredReq.triggered_detail', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='publish_ptp_ts', full_name='nio.ad.messages.EventTriggeredReq.publish_ptp_ts', index=5,
      number=536870907, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='publisher_id', full_name='nio.ad.messages.EventTriggeredReq.publisher_id', index=6,
      number=536870909, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='counter', full_name='nio.ad.messages.EventTriggeredReq.counter', index=7,
      number=536870910, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='publish_ts', full_name='nio.ad.messages.EventTriggeredReq.publish_ts', index=8,
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
  serialized_start=61,
  serialized_end=307,
)

DESCRIPTOR.message_types_by_name['EventTriggeredReq'] = _EVENTTRIGGEREDREQ
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

EventTriggeredReq = _reflection.GeneratedProtocolMessageType('EventTriggeredReq', (_message.Message,), {
  'DESCRIPTOR' : _EVENTTRIGGEREDREQ,
  '__module__' : 'common.dlb.event_triggered_report_pb2'
  # @@protoc_insertion_point(class_scope:nio.ad.messages.EventTriggeredReq)
  })
_sym_db.RegisterMessage(EventTriggeredReq)


# @@protoc_insertion_point(module_scope)

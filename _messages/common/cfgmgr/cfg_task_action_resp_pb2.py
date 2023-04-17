# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: common/cfgmgr/cfg_task_action_resp.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='common/cfgmgr/cfg_task_action_resp.proto',
  package='nio.ad.messages',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n(common/cfgmgr/cfg_task_action_resp.proto\x12\x0fnio.ad.messages\"\xeb\x01\n\x11\x43\x66gTaskActionResp\x12\x0c\n\x04uuid\x18\x01 \x01(\t\x12<\n\x05state\x18\x02 \x01(\x0e\x32-.nio.ad.messages.CfgTaskActionResp.ActionResp\x12\x1a\n\x0epublish_ptp_ts\x18\xfb\xff\xff\xff\x01 \x01(\x04\x12\x18\n\x0cpublisher_id\x18\xfd\xff\xff\xff\x01 \x01(\t\x12\x13\n\x07\x63ounter\x18\xfe\xff\xff\xff\x01 \x01(\x04\x12\x16\n\npublish_ts\x18\xff\xff\xff\xff\x01 \x01(\x04\"\'\n\nActionResp\x12\r\n\tSUCCEEDED\x10\x00\x12\n\n\x06\x46\x41ILED\x10\x01')
)



_CFGTASKACTIONRESP_ACTIONRESP = _descriptor.EnumDescriptor(
  name='ActionResp',
  full_name='nio.ad.messages.CfgTaskActionResp.ActionResp',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='SUCCEEDED', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAILED', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=258,
  serialized_end=297,
)
_sym_db.RegisterEnumDescriptor(_CFGTASKACTIONRESP_ACTIONRESP)


_CFGTASKACTIONRESP = _descriptor.Descriptor(
  name='CfgTaskActionResp',
  full_name='nio.ad.messages.CfgTaskActionResp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='uuid', full_name='nio.ad.messages.CfgTaskActionResp.uuid', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='state', full_name='nio.ad.messages.CfgTaskActionResp.state', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='publish_ptp_ts', full_name='nio.ad.messages.CfgTaskActionResp.publish_ptp_ts', index=2,
      number=536870907, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='publisher_id', full_name='nio.ad.messages.CfgTaskActionResp.publisher_id', index=3,
      number=536870909, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='counter', full_name='nio.ad.messages.CfgTaskActionResp.counter', index=4,
      number=536870910, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='publish_ts', full_name='nio.ad.messages.CfgTaskActionResp.publish_ts', index=5,
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
    _CFGTASKACTIONRESP_ACTIONRESP,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=62,
  serialized_end=297,
)

_CFGTASKACTIONRESP.fields_by_name['state'].enum_type = _CFGTASKACTIONRESP_ACTIONRESP
_CFGTASKACTIONRESP_ACTIONRESP.containing_type = _CFGTASKACTIONRESP
DESCRIPTOR.message_types_by_name['CfgTaskActionResp'] = _CFGTASKACTIONRESP
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CfgTaskActionResp = _reflection.GeneratedProtocolMessageType('CfgTaskActionResp', (_message.Message,), {
  'DESCRIPTOR' : _CFGTASKACTIONRESP,
  '__module__' : 'common.cfgmgr.cfg_task_action_resp_pb2'
  # @@protoc_insertion_point(class_scope:nio.ad.messages.CfgTaskActionResp)
  })
_sym_db.RegisterMessage(CfgTaskActionResp)


# @@protoc_insertion_point(module_scope)

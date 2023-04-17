# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: common/diagnostic/fim/fim_software.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='common/diagnostic/fim/fim_software.proto',
  package='nio.ad.messages',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n(common/diagnostic/fim/fim_software.proto\x12\x0fnio.ad.messages\"\xec\x02\n\x0f\x46imSoftwareInfo\x12<\n\x13s1_process_fim_info\x18\x01 \x01(\x0b\x32\x1f.nio.ad.messages.ProcessFimInfo\x12<\n\x13s2_process_fim_info\x18\x02 \x01(\x0b\x32\x1f.nio.ad.messages.ProcessFimInfo\x12<\n\x13s3_process_fim_info\x18\x03 \x01(\x0b\x32\x1f.nio.ad.messages.ProcessFimInfo\x12<\n\x13s4_process_fim_info\x18\x04 \x01(\x0b\x32\x1f.nio.ad.messages.ProcessFimInfo\x12\x1a\n\x0epublish_ptp_ts\x18\xfb\xff\xff\xff\x01 \x01(\x04\x12\x18\n\x0cpublisher_id\x18\xfd\xff\xff\xff\x01 \x01(\t\x12\x13\n\x07\x63ounter\x18\xfe\xff\xff\xff\x01 \x01(\x04\x12\x16\n\npublish_ts\x18\xff\xff\xff\xff\x01 \x01(\x04\"\x82\x06\n\x0eProcessFimInfo\x12\"\n\x1a\x46IM_CAN_RX_Exited_Abnormal\x18\x01 \x01(\x08\x12\"\n\x1a\x46IM_CAN_TX_Exited_Abnormal\x18\x02 \x01(\x08\x12%\n\x1d\x46IM_Radar_APP_Exited_Abnormal\x18\x03 \x01(\x08\x12&\n\x1e\x46IM_Camera_SAL_Exited_Abnormal\x18\x04 \x01(\x08\x12(\n FIM_Position_APP_Exited_Abnormal\x18\x05 \x01(\x08\x12\"\n\x1a\x46IM_AA_APP_Exited_Abnormal\x18\x06 \x01(\x08\x12#\n\x1b\x46IM_EHY_APP_Exited_Abnormal\x18\x07 \x01(\x08\x12#\n\x1b\x46IM_FCT_APP_Exited_Abnormal\x18\x08 \x01(\x08\x12$\n\x1c\x46IM_FCTs_APP_Exited_Abnormal\x18\t \x01(\x08\x12\x1f\n\x17\x46IM_FAM_Extied_Abnoraml\x18\n \x01(\x08\x12#\n\x1b\x46IM_CDM_APP_Exited_Abnormal\x18\x0b \x01(\x08\x12#\n\x1b\x46IM_DLB_APP_Exited_Abnormal\x18\x0c \x01(\x08\x12/\n\'FIM_Desensitization_APP_Exited_Abnoraml\x18\r \x01(\x08\x12$\n\x1c\x46IM_Launcher_Exited_Abnormal\x18\x0e \x01(\x08\x12\'\n\x1f\x46IM_Rel_Loc_APP_Exited_Abnoraml\x18\x0f \x01(\x08\x12,\n$FIM_NOPDelta_Planner_Exited_Abnoraml\x18\x10 \x01(\x08\x12,\n$FIM_NOPDelta_Control_Exited_Abnoraml\x18\x11 \x01(\x08\x12+\n#FIM_NOPDelta_Canbus_Exited_Abnoraml\x18\x12 \x01(\x08\x12\'\n\x1f\x46IM_NOPDelta_WM_Exited_Abnoraml\x18\x13 \x01(\x08')
)




_FIMSOFTWAREINFO = _descriptor.Descriptor(
  name='FimSoftwareInfo',
  full_name='nio.ad.messages.FimSoftwareInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='s1_process_fim_info', full_name='nio.ad.messages.FimSoftwareInfo.s1_process_fim_info', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='s2_process_fim_info', full_name='nio.ad.messages.FimSoftwareInfo.s2_process_fim_info', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='s3_process_fim_info', full_name='nio.ad.messages.FimSoftwareInfo.s3_process_fim_info', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='s4_process_fim_info', full_name='nio.ad.messages.FimSoftwareInfo.s4_process_fim_info', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='publish_ptp_ts', full_name='nio.ad.messages.FimSoftwareInfo.publish_ptp_ts', index=4,
      number=536870907, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='publisher_id', full_name='nio.ad.messages.FimSoftwareInfo.publisher_id', index=5,
      number=536870909, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='counter', full_name='nio.ad.messages.FimSoftwareInfo.counter', index=6,
      number=536870910, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='publish_ts', full_name='nio.ad.messages.FimSoftwareInfo.publish_ts', index=7,
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
  serialized_start=62,
  serialized_end=426,
)


_PROCESSFIMINFO = _descriptor.Descriptor(
  name='ProcessFimInfo',
  full_name='nio.ad.messages.ProcessFimInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='FIM_CAN_RX_Exited_Abnormal', full_name='nio.ad.messages.ProcessFimInfo.FIM_CAN_RX_Exited_Abnormal', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='FIM_CAN_TX_Exited_Abnormal', full_name='nio.ad.messages.ProcessFimInfo.FIM_CAN_TX_Exited_Abnormal', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='FIM_Radar_APP_Exited_Abnormal', full_name='nio.ad.messages.ProcessFimInfo.FIM_Radar_APP_Exited_Abnormal', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='FIM_Camera_SAL_Exited_Abnormal', full_name='nio.ad.messages.ProcessFimInfo.FIM_Camera_SAL_Exited_Abnormal', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='FIM_Position_APP_Exited_Abnormal', full_name='nio.ad.messages.ProcessFimInfo.FIM_Position_APP_Exited_Abnormal', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='FIM_AA_APP_Exited_Abnormal', full_name='nio.ad.messages.ProcessFimInfo.FIM_AA_APP_Exited_Abnormal', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='FIM_EHY_APP_Exited_Abnormal', full_name='nio.ad.messages.ProcessFimInfo.FIM_EHY_APP_Exited_Abnormal', index=6,
      number=7, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='FIM_FCT_APP_Exited_Abnormal', full_name='nio.ad.messages.ProcessFimInfo.FIM_FCT_APP_Exited_Abnormal', index=7,
      number=8, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='FIM_FCTs_APP_Exited_Abnormal', full_name='nio.ad.messages.ProcessFimInfo.FIM_FCTs_APP_Exited_Abnormal', index=8,
      number=9, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='FIM_FAM_Extied_Abnoraml', full_name='nio.ad.messages.ProcessFimInfo.FIM_FAM_Extied_Abnoraml', index=9,
      number=10, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='FIM_CDM_APP_Exited_Abnormal', full_name='nio.ad.messages.ProcessFimInfo.FIM_CDM_APP_Exited_Abnormal', index=10,
      number=11, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='FIM_DLB_APP_Exited_Abnormal', full_name='nio.ad.messages.ProcessFimInfo.FIM_DLB_APP_Exited_Abnormal', index=11,
      number=12, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='FIM_Desensitization_APP_Exited_Abnoraml', full_name='nio.ad.messages.ProcessFimInfo.FIM_Desensitization_APP_Exited_Abnoraml', index=12,
      number=13, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='FIM_Launcher_Exited_Abnormal', full_name='nio.ad.messages.ProcessFimInfo.FIM_Launcher_Exited_Abnormal', index=13,
      number=14, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='FIM_Rel_Loc_APP_Exited_Abnoraml', full_name='nio.ad.messages.ProcessFimInfo.FIM_Rel_Loc_APP_Exited_Abnoraml', index=14,
      number=15, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='FIM_NOPDelta_Planner_Exited_Abnoraml', full_name='nio.ad.messages.ProcessFimInfo.FIM_NOPDelta_Planner_Exited_Abnoraml', index=15,
      number=16, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='FIM_NOPDelta_Control_Exited_Abnoraml', full_name='nio.ad.messages.ProcessFimInfo.FIM_NOPDelta_Control_Exited_Abnoraml', index=16,
      number=17, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='FIM_NOPDelta_Canbus_Exited_Abnoraml', full_name='nio.ad.messages.ProcessFimInfo.FIM_NOPDelta_Canbus_Exited_Abnoraml', index=17,
      number=18, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='FIM_NOPDelta_WM_Exited_Abnoraml', full_name='nio.ad.messages.ProcessFimInfo.FIM_NOPDelta_WM_Exited_Abnoraml', index=18,
      number=19, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=429,
  serialized_end=1199,
)

_FIMSOFTWAREINFO.fields_by_name['s1_process_fim_info'].message_type = _PROCESSFIMINFO
_FIMSOFTWAREINFO.fields_by_name['s2_process_fim_info'].message_type = _PROCESSFIMINFO
_FIMSOFTWAREINFO.fields_by_name['s3_process_fim_info'].message_type = _PROCESSFIMINFO
_FIMSOFTWAREINFO.fields_by_name['s4_process_fim_info'].message_type = _PROCESSFIMINFO
DESCRIPTOR.message_types_by_name['FimSoftwareInfo'] = _FIMSOFTWAREINFO
DESCRIPTOR.message_types_by_name['ProcessFimInfo'] = _PROCESSFIMINFO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

FimSoftwareInfo = _reflection.GeneratedProtocolMessageType('FimSoftwareInfo', (_message.Message,), {
  'DESCRIPTOR' : _FIMSOFTWAREINFO,
  '__module__' : 'common.diagnostic.fim.fim_software_pb2'
  # @@protoc_insertion_point(class_scope:nio.ad.messages.FimSoftwareInfo)
  })
_sym_db.RegisterMessage(FimSoftwareInfo)

ProcessFimInfo = _reflection.GeneratedProtocolMessageType('ProcessFimInfo', (_message.Message,), {
  'DESCRIPTOR' : _PROCESSFIMINFO,
  '__module__' : 'common.diagnostic.fim.fim_software_pb2'
  # @@protoc_insertion_point(class_scope:nio.ad.messages.ProcessFimInfo)
  })
_sym_db.RegisterMessage(ProcessFimInfo)


# @@protoc_insertion_point(module_scope)

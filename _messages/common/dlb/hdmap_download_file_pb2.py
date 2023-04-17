# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: common/dlb/hdmap_download_file.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='common/dlb/hdmap_download_file.proto',
  package='nio.ad.messages',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n$common/dlb/hdmap_download_file.proto\x12\x0fnio.ad.messages\"\x81\x02\n\x11HDMapDownloadFile\x12\x0c\n\x04uuid\x18\x01 \x01(\t\x12\x13\n\x0bresult_code\x18\x02 \x01(\t\x12\x13\n\x0bserver_time\x18\x03 \x01(\x03\x12\x11\n\tfile_path\x18\x04 \x01(\t\x12\x15\n\rhdmap_version\x18\x05 \x01(\x04\x12\x0f\n\x07tile_id\x18\x06 \x01(\x04\x12\x16\n\x0e\x66ormat_version\x18\x07 \x01(\x04\x12\x1a\n\x0epublish_ptp_ts\x18\xfb\xff\xff\xff\x01 \x01(\x04\x12\x18\n\x0cpublisher_id\x18\xfd\xff\xff\xff\x01 \x01(\t\x12\x13\n\x07\x63ounter\x18\xfe\xff\xff\xff\x01 \x01(\x04\x12\x16\n\npublish_ts\x18\xff\xff\xff\xff\x01 \x01(\x04')
)




_HDMAPDOWNLOADFILE = _descriptor.Descriptor(
  name='HDMapDownloadFile',
  full_name='nio.ad.messages.HDMapDownloadFile',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='uuid', full_name='nio.ad.messages.HDMapDownloadFile.uuid', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='result_code', full_name='nio.ad.messages.HDMapDownloadFile.result_code', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='server_time', full_name='nio.ad.messages.HDMapDownloadFile.server_time', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='file_path', full_name='nio.ad.messages.HDMapDownloadFile.file_path', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hdmap_version', full_name='nio.ad.messages.HDMapDownloadFile.hdmap_version', index=4,
      number=5, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tile_id', full_name='nio.ad.messages.HDMapDownloadFile.tile_id', index=5,
      number=6, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='format_version', full_name='nio.ad.messages.HDMapDownloadFile.format_version', index=6,
      number=7, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='publish_ptp_ts', full_name='nio.ad.messages.HDMapDownloadFile.publish_ptp_ts', index=7,
      number=536870907, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='publisher_id', full_name='nio.ad.messages.HDMapDownloadFile.publisher_id', index=8,
      number=536870909, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='counter', full_name='nio.ad.messages.HDMapDownloadFile.counter', index=9,
      number=536870910, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='publish_ts', full_name='nio.ad.messages.HDMapDownloadFile.publish_ts', index=10,
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
  serialized_start=58,
  serialized_end=315,
)

DESCRIPTOR.message_types_by_name['HDMapDownloadFile'] = _HDMAPDOWNLOADFILE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

HDMapDownloadFile = _reflection.GeneratedProtocolMessageType('HDMapDownloadFile', (_message.Message,), {
  'DESCRIPTOR' : _HDMAPDOWNLOADFILE,
  '__module__' : 'common.dlb.hdmap_download_file_pb2'
  # @@protoc_insertion_point(class_scope:nio.ad.messages.HDMapDownloadFile)
  })
_sym_db.RegisterMessage(HDMapDownloadFile)


# @@protoc_insertion_point(module_scope)

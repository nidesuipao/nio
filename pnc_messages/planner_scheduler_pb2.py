# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: planner_scheduler.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import hmi_state_pb2 as hmi__state__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='planner_scheduler.proto',
  package='nio.proto',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n\x17planner_scheduler.proto\x12\tnio.proto\x1a\x0fhmi_state.proto\"\xf8\x03\n\rSchedulerTask\x12\x46\n\x1ascheduler_lane_change_type\x18\x01 \x01(\x0e\x32\".nio.proto.SchedulerLaneChangeType\x12J\n\x1fscheduler_lane_change_task_type\x18\x02 \x01(\x0e\x32!.nio.proto.SchedulerTask.TaskType\x12\r\n\x05valid\x18\x03 \x01(\x08\x12\x18\n\x10need_reject_task\x18\x04 \x01(\x08\x12-\n\x05scene\x18\x05 \x01(\x0e\x32\x1e.nio.proto.SchedulerTask.Scene\x12\x36\n\x0ctrigger_type\x18\x06 \x01(\x0e\x32 .nio.proto.LaneChangeTriggerType\"\x81\x01\n\x08TaskType\x12\x15\n\x11TASK_TYPE_HMI_REQ\x10\x00\x12\x15\n\x11TASK_TYPE_ROUTING\x10\x01\x12\x16\n\x12TASK_TYPE_OVERTAKE\x10\x02\x12\x16\n\x12TASK_TYPE_PRIORITY\x10\x03\x12\x17\n\x13TASK_TYPE_EMERGENCY\x10\x04\"?\n\x05Scene\x12\x08\n\x04ROAD\x10\x00\x12\x10\n\x0cROAD_TO_RAMP\x10\x01\x12\x08\n\x04RAMP\x10\x02\x12\x10\n\x0cRAMP_TO_ROAD\x10\x03\"\xe8\x02\n\x19SchedulerLaneChangeStatus\x12O\n\x1bscheduler_lane_change_state\x18\x01 \x01(\x0e\x32*.nio.proto.SchedulerLaneChangeStatus.State\"\xf9\x01\n\x05State\x12\x13\n\x0fSTATE_LANE_KEEP\x10\x00\x12\x1a\n\x16STATE_LEFT_LANE_CHANGE\x10\x01\x12\x1b\n\x17STATE_RIGHT_LANE_CHANGE\x10\x02\x12!\n\x1dSTATE_CANCEL_LEFT_LANE_CHANGE\x10\x03\x12\"\n\x1eSTATE_CANCEL_RIGHT_LANE_CHANGE\x10\x04\x12\x12\n\x0eSTATE_FINISHED\x10\x05\x12\"\n\x1eSTATE_PREPARE_LEFT_LANE_CHANGE\x10\x06\x12#\n\x1fSTATE_PREPARE_RIGHT_LANE_CHANGE\x10\x07\"\xaa\x04\n\x19SchedulerLaneChangePrompt\x12\x14\n\x0cprompt_valid\x18\x01 \x01(\x08\x12T\n\x17prompt_lane_change_type\x18\x02 \x01(\x0e\x32\x33.nio.proto.SchedulerLaneChangePrompt.LaneChangeType\x12\x46\n\x0cprompt_scene\x18\x03 \x01(\x0e\x32\x30.nio.proto.SchedulerLaneChangePrompt.PromptScene\x12\x42\n\nprompt_msg\x18\x04 \x01(\x0e\x32..nio.proto.SchedulerLaneChangePrompt.PromptMsg\"\x84\x01\n\tPromptMsg\x12\x1f\n\x1bPROMPT_ROUTE_CHANGE_REQUEST\x10\x00\x12\x1b\n\x17PROMPT_SCENE_LEVEL_HIGH\x10\x01\x12\x1d\n\x19PROMPT_SCENE_LEVEL_MIDDLE\x10\x02\x12\x1a\n\x16PROMPT_SCENE_LEVEL_LOW\x10\x03\"G\n\x0bPromptScene\x12\x0b\n\x07ROUTING\x10\x00\x12\x0c\n\x08OFF_RAMP\x10\x01\x12\x0b\n\x07ON_RAMP\x10\x02\x12\x10\n\x0cRAMP_TO_ROAD\x10\x03\"E\n\x0eLaneChangeType\x12\x0e\n\nSUCCEEDING\x10\x00\x12\x10\n\x0cLEFT_FORWARD\x10\x01\x12\x11\n\rRIGHT_FORWARD\x10\x02\"\xd6\x02\n\x10PlannerScheduler\x12\x30\n\x0escheduler_task\x18\x01 \x01(\x0b\x32\x18.nio.proto.SchedulerTask\x12J\n\x1cscheduler_lane_change_status\x18\x02 \x01(\x0b\x32$.nio.proto.SchedulerLaneChangeStatus\x12J\n\x1cscheduler_lane_change_prompt\x18\x03 \x01(\x0b\x32$.nio.proto.SchedulerLaneChangePrompt\x12\x44\n\x19lane_change_user_response\x18\x04 \x01(\x0e\x32!.nio.proto.LaneChangeUserResponse\x12\x32\n\x10\x61lc_confirm_mode\x18\x05 \x01(\x0e\x32\x18.nio.proto.ALCConfirmReq*\x82\x01\n\x17SchedulerLaneChangeType\x12\x0e\n\nSUCCEEDING\x10\x00\x12\x10\n\x0cLEFT_FORWARD\x10\x01\x12\x11\n\rRIGHT_FORWARD\x10\x02\x12\x0f\n\x0b\x43\x41NCEL_LEFT\x10\x03\x12\x10\n\x0c\x43\x41NCEL_RIGHT\x10\x04\x12\x0f\n\x0b\x43HANGE_BOTH\x10\x05*\xa3\x01\n\x15LaneChangeTriggerType\x12\n\n\x06\x44RIVER\x10\x00\x12\x17\n\x13\x45MERGENCY_AVOIDANCE\x10\x01\x12\t\n\x05SPLIT\x10\x02\x12\x0c\n\x08OFF_RAMP\x10\x03\x12\x10\n\x0cRAMP_TO_ROAD\x10\x04\x12\t\n\x05MERGE\x10\x05\x12\x0c\n\x08PRIORITY\x10\x06\x12\t\n\x05SPEED\x10\x07\x12\x0c\n\x08OVERTAKE\x10\x08\x12\x08\n\x04NONE\x10\t*\\\n\x16LaneChangeUserResponse\x12\x11\n\rNONE_RESPONCE\x10\x00\x12\x17\n\x13\x43ONFIRM_LANE_CHANGE\x10\x01\x12\x16\n\x12REJECT_LANE_CHANGE\x10\x02')
  ,
  dependencies=[hmi__state__pb2.DESCRIPTOR,])

_SCHEDULERLANECHANGETYPE = _descriptor.EnumDescriptor(
  name='SchedulerLaneChangeType',
  full_name='nio.proto.SchedulerLaneChangeType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='SUCCEEDING', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LEFT_FORWARD', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RIGHT_FORWARD', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CANCEL_LEFT', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CANCEL_RIGHT', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CHANGE_BOTH', index=5, number=5,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1828,
  serialized_end=1958,
)
_sym_db.RegisterEnumDescriptor(_SCHEDULERLANECHANGETYPE)

SchedulerLaneChangeType = enum_type_wrapper.EnumTypeWrapper(_SCHEDULERLANECHANGETYPE)
_LANECHANGETRIGGERTYPE = _descriptor.EnumDescriptor(
  name='LaneChangeTriggerType',
  full_name='nio.proto.LaneChangeTriggerType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='DRIVER', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EMERGENCY_AVOIDANCE', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SPLIT', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OFF_RAMP', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RAMP_TO_ROAD', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MERGE', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PRIORITY', index=6, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SPEED', index=7, number=7,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OVERTAKE', index=8, number=8,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NONE', index=9, number=9,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1961,
  serialized_end=2124,
)
_sym_db.RegisterEnumDescriptor(_LANECHANGETRIGGERTYPE)

LaneChangeTriggerType = enum_type_wrapper.EnumTypeWrapper(_LANECHANGETRIGGERTYPE)
_LANECHANGEUSERRESPONSE = _descriptor.EnumDescriptor(
  name='LaneChangeUserResponse',
  full_name='nio.proto.LaneChangeUserResponse',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NONE_RESPONCE', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CONFIRM_LANE_CHANGE', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REJECT_LANE_CHANGE', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=2126,
  serialized_end=2218,
)
_sym_db.RegisterEnumDescriptor(_LANECHANGEUSERRESPONSE)

LaneChangeUserResponse = enum_type_wrapper.EnumTypeWrapper(_LANECHANGEUSERRESPONSE)
SUCCEEDING = 0
LEFT_FORWARD = 1
RIGHT_FORWARD = 2
CANCEL_LEFT = 3
CANCEL_RIGHT = 4
CHANGE_BOTH = 5
DRIVER = 0
EMERGENCY_AVOIDANCE = 1
SPLIT = 2
OFF_RAMP = 3
RAMP_TO_ROAD = 4
MERGE = 5
PRIORITY = 6
SPEED = 7
OVERTAKE = 8
NONE = 9
NONE_RESPONCE = 0
CONFIRM_LANE_CHANGE = 1
REJECT_LANE_CHANGE = 2


_SCHEDULERTASK_TASKTYPE = _descriptor.EnumDescriptor(
  name='TaskType',
  full_name='nio.proto.SchedulerTask.TaskType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='TASK_TYPE_HMI_REQ', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TASK_TYPE_ROUTING', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TASK_TYPE_OVERTAKE', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TASK_TYPE_PRIORITY', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TASK_TYPE_EMERGENCY', index=4, number=4,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=366,
  serialized_end=495,
)
_sym_db.RegisterEnumDescriptor(_SCHEDULERTASK_TASKTYPE)

_SCHEDULERTASK_SCENE = _descriptor.EnumDescriptor(
  name='Scene',
  full_name='nio.proto.SchedulerTask.Scene',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ROAD', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ROAD_TO_RAMP', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RAMP', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RAMP_TO_ROAD', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=497,
  serialized_end=560,
)
_sym_db.RegisterEnumDescriptor(_SCHEDULERTASK_SCENE)

_SCHEDULERLANECHANGESTATUS_STATE = _descriptor.EnumDescriptor(
  name='State',
  full_name='nio.proto.SchedulerLaneChangeStatus.State',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='STATE_LANE_KEEP', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STATE_LEFT_LANE_CHANGE', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STATE_RIGHT_LANE_CHANGE', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STATE_CANCEL_LEFT_LANE_CHANGE', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STATE_CANCEL_RIGHT_LANE_CHANGE', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STATE_FINISHED', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STATE_PREPARE_LEFT_LANE_CHANGE', index=6, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STATE_PREPARE_RIGHT_LANE_CHANGE', index=7, number=7,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=674,
  serialized_end=923,
)
_sym_db.RegisterEnumDescriptor(_SCHEDULERLANECHANGESTATUS_STATE)

_SCHEDULERLANECHANGEPROMPT_PROMPTMSG = _descriptor.EnumDescriptor(
  name='PromptMsg',
  full_name='nio.proto.SchedulerLaneChangePrompt.PromptMsg',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='PROMPT_ROUTE_CHANGE_REQUEST', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PROMPT_SCENE_LEVEL_HIGH', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PROMPT_SCENE_LEVEL_MIDDLE', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PROMPT_SCENE_LEVEL_LOW', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1204,
  serialized_end=1336,
)
_sym_db.RegisterEnumDescriptor(_SCHEDULERLANECHANGEPROMPT_PROMPTMSG)

_SCHEDULERLANECHANGEPROMPT_PROMPTSCENE = _descriptor.EnumDescriptor(
  name='PromptScene',
  full_name='nio.proto.SchedulerLaneChangePrompt.PromptScene',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ROUTING', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OFF_RAMP', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ON_RAMP', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RAMP_TO_ROAD', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1338,
  serialized_end=1409,
)
_sym_db.RegisterEnumDescriptor(_SCHEDULERLANECHANGEPROMPT_PROMPTSCENE)

_SCHEDULERLANECHANGEPROMPT_LANECHANGETYPE = _descriptor.EnumDescriptor(
  name='LaneChangeType',
  full_name='nio.proto.SchedulerLaneChangePrompt.LaneChangeType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='SUCCEEDING', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LEFT_FORWARD', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RIGHT_FORWARD', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1411,
  serialized_end=1480,
)
_sym_db.RegisterEnumDescriptor(_SCHEDULERLANECHANGEPROMPT_LANECHANGETYPE)


_SCHEDULERTASK = _descriptor.Descriptor(
  name='SchedulerTask',
  full_name='nio.proto.SchedulerTask',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='scheduler_lane_change_type', full_name='nio.proto.SchedulerTask.scheduler_lane_change_type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='scheduler_lane_change_task_type', full_name='nio.proto.SchedulerTask.scheduler_lane_change_task_type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='valid', full_name='nio.proto.SchedulerTask.valid', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='need_reject_task', full_name='nio.proto.SchedulerTask.need_reject_task', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='scene', full_name='nio.proto.SchedulerTask.scene', index=4,
      number=5, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='trigger_type', full_name='nio.proto.SchedulerTask.trigger_type', index=5,
      number=6, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _SCHEDULERTASK_TASKTYPE,
    _SCHEDULERTASK_SCENE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=56,
  serialized_end=560,
)


_SCHEDULERLANECHANGESTATUS = _descriptor.Descriptor(
  name='SchedulerLaneChangeStatus',
  full_name='nio.proto.SchedulerLaneChangeStatus',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='scheduler_lane_change_state', full_name='nio.proto.SchedulerLaneChangeStatus.scheduler_lane_change_state', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _SCHEDULERLANECHANGESTATUS_STATE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=563,
  serialized_end=923,
)


_SCHEDULERLANECHANGEPROMPT = _descriptor.Descriptor(
  name='SchedulerLaneChangePrompt',
  full_name='nio.proto.SchedulerLaneChangePrompt',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='prompt_valid', full_name='nio.proto.SchedulerLaneChangePrompt.prompt_valid', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='prompt_lane_change_type', full_name='nio.proto.SchedulerLaneChangePrompt.prompt_lane_change_type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='prompt_scene', full_name='nio.proto.SchedulerLaneChangePrompt.prompt_scene', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='prompt_msg', full_name='nio.proto.SchedulerLaneChangePrompt.prompt_msg', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _SCHEDULERLANECHANGEPROMPT_PROMPTMSG,
    _SCHEDULERLANECHANGEPROMPT_PROMPTSCENE,
    _SCHEDULERLANECHANGEPROMPT_LANECHANGETYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=926,
  serialized_end=1480,
)


_PLANNERSCHEDULER = _descriptor.Descriptor(
  name='PlannerScheduler',
  full_name='nio.proto.PlannerScheduler',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='scheduler_task', full_name='nio.proto.PlannerScheduler.scheduler_task', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='scheduler_lane_change_status', full_name='nio.proto.PlannerScheduler.scheduler_lane_change_status', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='scheduler_lane_change_prompt', full_name='nio.proto.PlannerScheduler.scheduler_lane_change_prompt', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lane_change_user_response', full_name='nio.proto.PlannerScheduler.lane_change_user_response', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='alc_confirm_mode', full_name='nio.proto.PlannerScheduler.alc_confirm_mode', index=4,
      number=5, type=14, cpp_type=8, label=1,
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
  serialized_start=1483,
  serialized_end=1825,
)

_SCHEDULERTASK.fields_by_name['scheduler_lane_change_type'].enum_type = _SCHEDULERLANECHANGETYPE
_SCHEDULERTASK.fields_by_name['scheduler_lane_change_task_type'].enum_type = _SCHEDULERTASK_TASKTYPE
_SCHEDULERTASK.fields_by_name['scene'].enum_type = _SCHEDULERTASK_SCENE
_SCHEDULERTASK.fields_by_name['trigger_type'].enum_type = _LANECHANGETRIGGERTYPE
_SCHEDULERTASK_TASKTYPE.containing_type = _SCHEDULERTASK
_SCHEDULERTASK_SCENE.containing_type = _SCHEDULERTASK
_SCHEDULERLANECHANGESTATUS.fields_by_name['scheduler_lane_change_state'].enum_type = _SCHEDULERLANECHANGESTATUS_STATE
_SCHEDULERLANECHANGESTATUS_STATE.containing_type = _SCHEDULERLANECHANGESTATUS
_SCHEDULERLANECHANGEPROMPT.fields_by_name['prompt_lane_change_type'].enum_type = _SCHEDULERLANECHANGEPROMPT_LANECHANGETYPE
_SCHEDULERLANECHANGEPROMPT.fields_by_name['prompt_scene'].enum_type = _SCHEDULERLANECHANGEPROMPT_PROMPTSCENE
_SCHEDULERLANECHANGEPROMPT.fields_by_name['prompt_msg'].enum_type = _SCHEDULERLANECHANGEPROMPT_PROMPTMSG
_SCHEDULERLANECHANGEPROMPT_PROMPTMSG.containing_type = _SCHEDULERLANECHANGEPROMPT
_SCHEDULERLANECHANGEPROMPT_PROMPTSCENE.containing_type = _SCHEDULERLANECHANGEPROMPT
_SCHEDULERLANECHANGEPROMPT_LANECHANGETYPE.containing_type = _SCHEDULERLANECHANGEPROMPT
_PLANNERSCHEDULER.fields_by_name['scheduler_task'].message_type = _SCHEDULERTASK
_PLANNERSCHEDULER.fields_by_name['scheduler_lane_change_status'].message_type = _SCHEDULERLANECHANGESTATUS
_PLANNERSCHEDULER.fields_by_name['scheduler_lane_change_prompt'].message_type = _SCHEDULERLANECHANGEPROMPT
_PLANNERSCHEDULER.fields_by_name['lane_change_user_response'].enum_type = _LANECHANGEUSERRESPONSE
_PLANNERSCHEDULER.fields_by_name['alc_confirm_mode'].enum_type = hmi__state__pb2._ALCCONFIRMREQ
DESCRIPTOR.message_types_by_name['SchedulerTask'] = _SCHEDULERTASK
DESCRIPTOR.message_types_by_name['SchedulerLaneChangeStatus'] = _SCHEDULERLANECHANGESTATUS
DESCRIPTOR.message_types_by_name['SchedulerLaneChangePrompt'] = _SCHEDULERLANECHANGEPROMPT
DESCRIPTOR.message_types_by_name['PlannerScheduler'] = _PLANNERSCHEDULER
DESCRIPTOR.enum_types_by_name['SchedulerLaneChangeType'] = _SCHEDULERLANECHANGETYPE
DESCRIPTOR.enum_types_by_name['LaneChangeTriggerType'] = _LANECHANGETRIGGERTYPE
DESCRIPTOR.enum_types_by_name['LaneChangeUserResponse'] = _LANECHANGEUSERRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SchedulerTask = _reflection.GeneratedProtocolMessageType('SchedulerTask', (_message.Message,), {
  'DESCRIPTOR' : _SCHEDULERTASK,
  '__module__' : 'planner_scheduler_pb2'
  # @@protoc_insertion_point(class_scope:nio.proto.SchedulerTask)
  })
_sym_db.RegisterMessage(SchedulerTask)

SchedulerLaneChangeStatus = _reflection.GeneratedProtocolMessageType('SchedulerLaneChangeStatus', (_message.Message,), {
  'DESCRIPTOR' : _SCHEDULERLANECHANGESTATUS,
  '__module__' : 'planner_scheduler_pb2'
  # @@protoc_insertion_point(class_scope:nio.proto.SchedulerLaneChangeStatus)
  })
_sym_db.RegisterMessage(SchedulerLaneChangeStatus)

SchedulerLaneChangePrompt = _reflection.GeneratedProtocolMessageType('SchedulerLaneChangePrompt', (_message.Message,), {
  'DESCRIPTOR' : _SCHEDULERLANECHANGEPROMPT,
  '__module__' : 'planner_scheduler_pb2'
  # @@protoc_insertion_point(class_scope:nio.proto.SchedulerLaneChangePrompt)
  })
_sym_db.RegisterMessage(SchedulerLaneChangePrompt)

PlannerScheduler = _reflection.GeneratedProtocolMessageType('PlannerScheduler', (_message.Message,), {
  'DESCRIPTOR' : _PLANNERSCHEDULER,
  '__module__' : 'planner_scheduler_pb2'
  # @@protoc_insertion_point(class_scope:nio.proto.PlannerScheduler)
  })
_sym_db.RegisterMessage(PlannerScheduler)


# @@protoc_insertion_point(module_scope)

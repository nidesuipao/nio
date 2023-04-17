# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from rospy_message_converter/FeatureOperationPoint.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import rospy_message_converter.msg

class FeatureOperationPoint(genpy.Message):
  _md5sum = "b4b5fb58952c95b5983ae21883e1dd6e"
  _type = "rospy_message_converter/FeatureOperationPoint"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """bool is_valid
int32 offset_start
int32 offset_end
uint64 linkid
int32 curr_laneidx
EventCondition event_condition
DrivingActionContext[] action_context

================================================================================
MSG: rospy_message_converter/EventCondition
string vehicle_model
string software_version
string hardware_version
string map_version
Point2D event_gps
string event_start_time
string event_end_time
ScenarioType scenario_type
int32 driver_filter
string range_start_time
string range_end_time

================================================================================
MSG: rospy_message_converter/Point2D
float64 x
float64 y

================================================================================
MSG: rospy_message_converter/ScenarioType
int32 weather_type
int32 lighting_type

================================================================================
MSG: rospy_message_converter/DrivingActionContext
InfoConfig[] info_config

================================================================================
MSG: rospy_message_converter/InfoConfig
int32 info_value
int32 static_info
int32 dynamic_info
int32 road_scenario_type
"""
  __slots__ = ['is_valid','offset_start','offset_end','linkid','curr_laneidx','event_condition','action_context']
  _slot_types = ['bool','int32','int32','uint64','int32','rospy_message_converter/EventCondition','rospy_message_converter/DrivingActionContext[]']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       is_valid,offset_start,offset_end,linkid,curr_laneidx,event_condition,action_context

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(FeatureOperationPoint, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.is_valid is None:
        self.is_valid = False
      if self.offset_start is None:
        self.offset_start = 0
      if self.offset_end is None:
        self.offset_end = 0
      if self.linkid is None:
        self.linkid = 0
      if self.curr_laneidx is None:
        self.curr_laneidx = 0
      if self.event_condition is None:
        self.event_condition = rospy_message_converter.msg.EventCondition()
      if self.action_context is None:
        self.action_context = []
    else:
      self.is_valid = False
      self.offset_start = 0
      self.offset_end = 0
      self.linkid = 0
      self.curr_laneidx = 0
      self.event_condition = rospy_message_converter.msg.EventCondition()
      self.action_context = []

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_get_struct_B2iQi().pack(_x.is_valid, _x.offset_start, _x.offset_end, _x.linkid, _x.curr_laneidx))
      _x = self.event_condition.vehicle_model
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self.event_condition.software_version
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self.event_condition.hardware_version
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self.event_condition.map_version
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_2d().pack(_x.event_condition.event_gps.x, _x.event_condition.event_gps.y))
      _x = self.event_condition.event_start_time
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self.event_condition.event_end_time
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_3i().pack(_x.event_condition.scenario_type.weather_type, _x.event_condition.scenario_type.lighting_type, _x.event_condition.driver_filter))
      _x = self.event_condition.range_start_time
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self.event_condition.range_end_time
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      length = len(self.action_context)
      buff.write(_struct_I.pack(length))
      for val1 in self.action_context:
        length = len(val1.info_config)
        buff.write(_struct_I.pack(length))
        for val2 in val1.info_config:
          _x = val2
          buff.write(_get_struct_4i().pack(_x.info_value, _x.static_info, _x.dynamic_info, _x.road_scenario_type))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.event_condition is None:
        self.event_condition = rospy_message_converter.msg.EventCondition()
      if self.action_context is None:
        self.action_context = None
      end = 0
      _x = self
      start = end
      end += 21
      (_x.is_valid, _x.offset_start, _x.offset_end, _x.linkid, _x.curr_laneidx,) = _get_struct_B2iQi().unpack(str[start:end])
      self.is_valid = bool(self.is_valid)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.event_condition.vehicle_model = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.event_condition.vehicle_model = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.event_condition.software_version = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.event_condition.software_version = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.event_condition.hardware_version = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.event_condition.hardware_version = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.event_condition.map_version = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.event_condition.map_version = str[start:end]
      _x = self
      start = end
      end += 16
      (_x.event_condition.event_gps.x, _x.event_condition.event_gps.y,) = _get_struct_2d().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.event_condition.event_start_time = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.event_condition.event_start_time = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.event_condition.event_end_time = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.event_condition.event_end_time = str[start:end]
      _x = self
      start = end
      end += 12
      (_x.event_condition.scenario_type.weather_type, _x.event_condition.scenario_type.lighting_type, _x.event_condition.driver_filter,) = _get_struct_3i().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.event_condition.range_start_time = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.event_condition.range_start_time = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.event_condition.range_end_time = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.event_condition.range_end_time = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.action_context = []
      for i in range(0, length):
        val1 = rospy_message_converter.msg.DrivingActionContext()
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        val1.info_config = []
        for i in range(0, length):
          val2 = rospy_message_converter.msg.InfoConfig()
          _x = val2
          start = end
          end += 16
          (_x.info_value, _x.static_info, _x.dynamic_info, _x.road_scenario_type,) = _get_struct_4i().unpack(str[start:end])
          val1.info_config.append(val2)
        self.action_context.append(val1)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_get_struct_B2iQi().pack(_x.is_valid, _x.offset_start, _x.offset_end, _x.linkid, _x.curr_laneidx))
      _x = self.event_condition.vehicle_model
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self.event_condition.software_version
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self.event_condition.hardware_version
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self.event_condition.map_version
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_2d().pack(_x.event_condition.event_gps.x, _x.event_condition.event_gps.y))
      _x = self.event_condition.event_start_time
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self.event_condition.event_end_time
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_3i().pack(_x.event_condition.scenario_type.weather_type, _x.event_condition.scenario_type.lighting_type, _x.event_condition.driver_filter))
      _x = self.event_condition.range_start_time
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self.event_condition.range_end_time
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      length = len(self.action_context)
      buff.write(_struct_I.pack(length))
      for val1 in self.action_context:
        length = len(val1.info_config)
        buff.write(_struct_I.pack(length))
        for val2 in val1.info_config:
          _x = val2
          buff.write(_get_struct_4i().pack(_x.info_value, _x.static_info, _x.dynamic_info, _x.road_scenario_type))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.event_condition is None:
        self.event_condition = rospy_message_converter.msg.EventCondition()
      if self.action_context is None:
        self.action_context = None
      end = 0
      _x = self
      start = end
      end += 21
      (_x.is_valid, _x.offset_start, _x.offset_end, _x.linkid, _x.curr_laneidx,) = _get_struct_B2iQi().unpack(str[start:end])
      self.is_valid = bool(self.is_valid)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.event_condition.vehicle_model = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.event_condition.vehicle_model = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.event_condition.software_version = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.event_condition.software_version = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.event_condition.hardware_version = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.event_condition.hardware_version = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.event_condition.map_version = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.event_condition.map_version = str[start:end]
      _x = self
      start = end
      end += 16
      (_x.event_condition.event_gps.x, _x.event_condition.event_gps.y,) = _get_struct_2d().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.event_condition.event_start_time = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.event_condition.event_start_time = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.event_condition.event_end_time = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.event_condition.event_end_time = str[start:end]
      _x = self
      start = end
      end += 12
      (_x.event_condition.scenario_type.weather_type, _x.event_condition.scenario_type.lighting_type, _x.event_condition.driver_filter,) = _get_struct_3i().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.event_condition.range_start_time = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.event_condition.range_start_time = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.event_condition.range_end_time = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.event_condition.range_end_time = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.action_context = []
      for i in range(0, length):
        val1 = rospy_message_converter.msg.DrivingActionContext()
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        val1.info_config = []
        for i in range(0, length):
          val2 = rospy_message_converter.msg.InfoConfig()
          _x = val2
          start = end
          end += 16
          (_x.info_value, _x.static_info, _x.dynamic_info, _x.road_scenario_type,) = _get_struct_4i().unpack(str[start:end])
          val1.info_config.append(val2)
        self.action_context.append(val1)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_2d = None
def _get_struct_2d():
    global _struct_2d
    if _struct_2d is None:
        _struct_2d = struct.Struct("<2d")
    return _struct_2d
_struct_3i = None
def _get_struct_3i():
    global _struct_3i
    if _struct_3i is None:
        _struct_3i = struct.Struct("<3i")
    return _struct_3i
_struct_4i = None
def _get_struct_4i():
    global _struct_4i
    if _struct_4i is None:
        _struct_4i = struct.Struct("<4i")
    return _struct_4i
_struct_B2iQi = None
def _get_struct_B2iQi():
    global _struct_B2iQi
    if _struct_B2iQi is None:
        _struct_B2iQi = struct.Struct("<B2iQi")
    return _struct_B2iQi

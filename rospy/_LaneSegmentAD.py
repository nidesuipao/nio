# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from rospy_message_converter/LaneSegmentAD.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class LaneSegmentAD(genpy.Message):
  _md5sum = "a72681c3f1a97b0fde5a65d3d16b2ec8"
  _type = "rospy_message_converter/LaneSegmentAD"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """uint64 id
float64 start_longitude
float64 start_latitude
float64 end_longitude
float64 end_latitude
int32 weather
float64 speed_limit
float64 valid_start_time
float64 valid_end_time
int32 type
"""
  __slots__ = ['id','start_longitude','start_latitude','end_longitude','end_latitude','weather','speed_limit','valid_start_time','valid_end_time','type']
  _slot_types = ['uint64','float64','float64','float64','float64','int32','float64','float64','float64','int32']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       id,start_longitude,start_latitude,end_longitude,end_latitude,weather,speed_limit,valid_start_time,valid_end_time,type

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(LaneSegmentAD, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.id is None:
        self.id = 0
      if self.start_longitude is None:
        self.start_longitude = 0.
      if self.start_latitude is None:
        self.start_latitude = 0.
      if self.end_longitude is None:
        self.end_longitude = 0.
      if self.end_latitude is None:
        self.end_latitude = 0.
      if self.weather is None:
        self.weather = 0
      if self.speed_limit is None:
        self.speed_limit = 0.
      if self.valid_start_time is None:
        self.valid_start_time = 0.
      if self.valid_end_time is None:
        self.valid_end_time = 0.
      if self.type is None:
        self.type = 0
    else:
      self.id = 0
      self.start_longitude = 0.
      self.start_latitude = 0.
      self.end_longitude = 0.
      self.end_latitude = 0.
      self.weather = 0
      self.speed_limit = 0.
      self.valid_start_time = 0.
      self.valid_end_time = 0.
      self.type = 0

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
      buff.write(_get_struct_Q4di3di().pack(_x.id, _x.start_longitude, _x.start_latitude, _x.end_longitude, _x.end_latitude, _x.weather, _x.speed_limit, _x.valid_start_time, _x.valid_end_time, _x.type))
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
      end = 0
      _x = self
      start = end
      end += 72
      (_x.id, _x.start_longitude, _x.start_latitude, _x.end_longitude, _x.end_latitude, _x.weather, _x.speed_limit, _x.valid_start_time, _x.valid_end_time, _x.type,) = _get_struct_Q4di3di().unpack(str[start:end])
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
      buff.write(_get_struct_Q4di3di().pack(_x.id, _x.start_longitude, _x.start_latitude, _x.end_longitude, _x.end_latitude, _x.weather, _x.speed_limit, _x.valid_start_time, _x.valid_end_time, _x.type))
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
      end = 0
      _x = self
      start = end
      end += 72
      (_x.id, _x.start_longitude, _x.start_latitude, _x.end_longitude, _x.end_latitude, _x.weather, _x.speed_limit, _x.valid_start_time, _x.valid_end_time, _x.type,) = _get_struct_Q4di3di().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_Q4di3di = None
def _get_struct_Q4di3di():
    global _struct_Q4di3di
    if _struct_Q4di3di is None:
        _struct_Q4di3di = struct.Struct("<Q4di3di")
    return _struct_Q4di3di

# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from rospy_message_converter/RadarStatus.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class RadarStatus(genpy.Message):
  _md5sum = "a6dd5227f0308a750a9cb6005d75faba"
  _type = "rospy_message_converter/RadarStatus"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """bool flg_blindness
bool flg_failure
bool flg_loss_comm_fault
bool flg_time_stamp_invalid
float32 mis_alignment_angle
int32 alignment_st
int32 sensor_location
"""
  __slots__ = ['flg_blindness','flg_failure','flg_loss_comm_fault','flg_time_stamp_invalid','mis_alignment_angle','alignment_st','sensor_location']
  _slot_types = ['bool','bool','bool','bool','float32','int32','int32']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       flg_blindness,flg_failure,flg_loss_comm_fault,flg_time_stamp_invalid,mis_alignment_angle,alignment_st,sensor_location

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(RadarStatus, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.flg_blindness is None:
        self.flg_blindness = False
      if self.flg_failure is None:
        self.flg_failure = False
      if self.flg_loss_comm_fault is None:
        self.flg_loss_comm_fault = False
      if self.flg_time_stamp_invalid is None:
        self.flg_time_stamp_invalid = False
      if self.mis_alignment_angle is None:
        self.mis_alignment_angle = 0.
      if self.alignment_st is None:
        self.alignment_st = 0
      if self.sensor_location is None:
        self.sensor_location = 0
    else:
      self.flg_blindness = False
      self.flg_failure = False
      self.flg_loss_comm_fault = False
      self.flg_time_stamp_invalid = False
      self.mis_alignment_angle = 0.
      self.alignment_st = 0
      self.sensor_location = 0

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
      buff.write(_get_struct_4Bf2i().pack(_x.flg_blindness, _x.flg_failure, _x.flg_loss_comm_fault, _x.flg_time_stamp_invalid, _x.mis_alignment_angle, _x.alignment_st, _x.sensor_location))
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
      end += 16
      (_x.flg_blindness, _x.flg_failure, _x.flg_loss_comm_fault, _x.flg_time_stamp_invalid, _x.mis_alignment_angle, _x.alignment_st, _x.sensor_location,) = _get_struct_4Bf2i().unpack(str[start:end])
      self.flg_blindness = bool(self.flg_blindness)
      self.flg_failure = bool(self.flg_failure)
      self.flg_loss_comm_fault = bool(self.flg_loss_comm_fault)
      self.flg_time_stamp_invalid = bool(self.flg_time_stamp_invalid)
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
      buff.write(_get_struct_4Bf2i().pack(_x.flg_blindness, _x.flg_failure, _x.flg_loss_comm_fault, _x.flg_time_stamp_invalid, _x.mis_alignment_angle, _x.alignment_st, _x.sensor_location))
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
      end += 16
      (_x.flg_blindness, _x.flg_failure, _x.flg_loss_comm_fault, _x.flg_time_stamp_invalid, _x.mis_alignment_angle, _x.alignment_st, _x.sensor_location,) = _get_struct_4Bf2i().unpack(str[start:end])
      self.flg_blindness = bool(self.flg_blindness)
      self.flg_failure = bool(self.flg_failure)
      self.flg_loss_comm_fault = bool(self.flg_loss_comm_fault)
      self.flg_time_stamp_invalid = bool(self.flg_time_stamp_invalid)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_4Bf2i = None
def _get_struct_4Bf2i():
    global _struct_4Bf2i
    if _struct_4Bf2i is None:
        _struct_4Bf2i = struct.Struct("<4Bf2i")
    return _struct_4Bf2i

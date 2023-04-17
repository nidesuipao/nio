# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from rospy_message_converter/esd_np_alc.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class esd_np_alc(genpy.Message):
  _md5sum = "a64de322662a6904972602b8b8063531"
  _type = "rospy_message_converter/esd_np_alc"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """uint64 esd_np_alc_crossing
uint64 esd_np_alc_sts
uint32 esd_laneChngIntent
bool esd_crossed_left_lane
bool esd_crossed_right_lane
"""
  __slots__ = ['esd_np_alc_crossing','esd_np_alc_sts','esd_laneChngIntent','esd_crossed_left_lane','esd_crossed_right_lane']
  _slot_types = ['uint64','uint64','uint32','bool','bool']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       esd_np_alc_crossing,esd_np_alc_sts,esd_laneChngIntent,esd_crossed_left_lane,esd_crossed_right_lane

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(esd_np_alc, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.esd_np_alc_crossing is None:
        self.esd_np_alc_crossing = 0
      if self.esd_np_alc_sts is None:
        self.esd_np_alc_sts = 0
      if self.esd_laneChngIntent is None:
        self.esd_laneChngIntent = 0
      if self.esd_crossed_left_lane is None:
        self.esd_crossed_left_lane = False
      if self.esd_crossed_right_lane is None:
        self.esd_crossed_right_lane = False
    else:
      self.esd_np_alc_crossing = 0
      self.esd_np_alc_sts = 0
      self.esd_laneChngIntent = 0
      self.esd_crossed_left_lane = False
      self.esd_crossed_right_lane = False

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
      buff.write(_get_struct_2QI2B().pack(_x.esd_np_alc_crossing, _x.esd_np_alc_sts, _x.esd_laneChngIntent, _x.esd_crossed_left_lane, _x.esd_crossed_right_lane))
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
      end += 22
      (_x.esd_np_alc_crossing, _x.esd_np_alc_sts, _x.esd_laneChngIntent, _x.esd_crossed_left_lane, _x.esd_crossed_right_lane,) = _get_struct_2QI2B().unpack(str[start:end])
      self.esd_crossed_left_lane = bool(self.esd_crossed_left_lane)
      self.esd_crossed_right_lane = bool(self.esd_crossed_right_lane)
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
      buff.write(_get_struct_2QI2B().pack(_x.esd_np_alc_crossing, _x.esd_np_alc_sts, _x.esd_laneChngIntent, _x.esd_crossed_left_lane, _x.esd_crossed_right_lane))
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
      end += 22
      (_x.esd_np_alc_crossing, _x.esd_np_alc_sts, _x.esd_laneChngIntent, _x.esd_crossed_left_lane, _x.esd_crossed_right_lane,) = _get_struct_2QI2B().unpack(str[start:end])
      self.esd_crossed_left_lane = bool(self.esd_crossed_left_lane)
      self.esd_crossed_right_lane = bool(self.esd_crossed_right_lane)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_2QI2B = None
def _get_struct_2QI2B():
    global _struct_2QI2B
    if _struct_2QI2B is None:
        _struct_2QI2B = struct.Struct("<2QI2B")
    return _struct_2QI2B

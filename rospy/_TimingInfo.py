# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from rospy_message_converter/TimingInfo.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class TimingInfo(genpy.Message):
  _md5sum = "c23841df94d1681592a88140fe373679"
  _type = "rospy_message_converter/TimingInfo"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """uint32 Yr
uint32 Mth
uint32 Day
uint32 Hr
uint32 Min
uint32 Sec
"""
  __slots__ = ['Yr','Mth','Day','Hr','Min','Sec']
  _slot_types = ['uint32','uint32','uint32','uint32','uint32','uint32']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       Yr,Mth,Day,Hr,Min,Sec

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(TimingInfo, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.Yr is None:
        self.Yr = 0
      if self.Mth is None:
        self.Mth = 0
      if self.Day is None:
        self.Day = 0
      if self.Hr is None:
        self.Hr = 0
      if self.Min is None:
        self.Min = 0
      if self.Sec is None:
        self.Sec = 0
    else:
      self.Yr = 0
      self.Mth = 0
      self.Day = 0
      self.Hr = 0
      self.Min = 0
      self.Sec = 0

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
      buff.write(_get_struct_6I().pack(_x.Yr, _x.Mth, _x.Day, _x.Hr, _x.Min, _x.Sec))
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
      end += 24
      (_x.Yr, _x.Mth, _x.Day, _x.Hr, _x.Min, _x.Sec,) = _get_struct_6I().unpack(str[start:end])
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
      buff.write(_get_struct_6I().pack(_x.Yr, _x.Mth, _x.Day, _x.Hr, _x.Min, _x.Sec))
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
      end += 24
      (_x.Yr, _x.Mth, _x.Day, _x.Hr, _x.Min, _x.Sec,) = _get_struct_6I().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_6I = None
def _get_struct_6I():
    global _struct_6I
    if _struct_6I is None:
        _struct_6I = struct.Struct("<6I")
    return _struct_6I

# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from rospy_message_converter/AdasMapProfilePoint.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class AdasMapProfilePoint(genpy.Message):
  _md5sum = "e509721f01e06f7a7bd22d1944d35720"
  _type = "rospy_message_converter/AdasMapProfilePoint"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """uint64 offset
uint64 index
int32 type
uint64 value
bool is_control_point
float64 decoded_value
"""
  __slots__ = ['offset','index','type','value','is_control_point','decoded_value']
  _slot_types = ['uint64','uint64','int32','uint64','bool','float64']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       offset,index,type,value,is_control_point,decoded_value

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(AdasMapProfilePoint, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.offset is None:
        self.offset = 0
      if self.index is None:
        self.index = 0
      if self.type is None:
        self.type = 0
      if self.value is None:
        self.value = 0
      if self.is_control_point is None:
        self.is_control_point = False
      if self.decoded_value is None:
        self.decoded_value = 0.
    else:
      self.offset = 0
      self.index = 0
      self.type = 0
      self.value = 0
      self.is_control_point = False
      self.decoded_value = 0.

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
      buff.write(_get_struct_2QiQBd().pack(_x.offset, _x.index, _x.type, _x.value, _x.is_control_point, _x.decoded_value))
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
      end += 37
      (_x.offset, _x.index, _x.type, _x.value, _x.is_control_point, _x.decoded_value,) = _get_struct_2QiQBd().unpack(str[start:end])
      self.is_control_point = bool(self.is_control_point)
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
      buff.write(_get_struct_2QiQBd().pack(_x.offset, _x.index, _x.type, _x.value, _x.is_control_point, _x.decoded_value))
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
      end += 37
      (_x.offset, _x.index, _x.type, _x.value, _x.is_control_point, _x.decoded_value,) = _get_struct_2QiQBd().unpack(str[start:end])
      self.is_control_point = bool(self.is_control_point)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_2QiQBd = None
def _get_struct_2QiQBd():
    global _struct_2QiQBd
    if _struct_2QiQBd is None:
        _struct_2QiQBd = struct.Struct("<2QiQBd")
    return _struct_2QiQBd

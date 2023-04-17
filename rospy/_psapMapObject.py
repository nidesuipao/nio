# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from rospy_message_converter/psapMapObject.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class psapMapObject(genpy.Message):
  _md5sum = "55fb2669679cf3c8667d8e6afba3a18c"
  _type = "rospy_message_converter/psapMapObject"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """int32 psapMapObjectType
bool psapMapObjectValid
float32 psapMapObjectPointX1
float32 psapMapObjectPointY1
float32 psapMapObjectPointX2
float32 psapMapObjectPointY2
float32 psapMapObjectPointX3
float32 psapMapObjectPointY3
float32 psapMapObjectPointX4
float32 psapMapObjectPointY4
"""
  __slots__ = ['psapMapObjectType','psapMapObjectValid','psapMapObjectPointX1','psapMapObjectPointY1','psapMapObjectPointX2','psapMapObjectPointY2','psapMapObjectPointX3','psapMapObjectPointY3','psapMapObjectPointX4','psapMapObjectPointY4']
  _slot_types = ['int32','bool','float32','float32','float32','float32','float32','float32','float32','float32']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       psapMapObjectType,psapMapObjectValid,psapMapObjectPointX1,psapMapObjectPointY1,psapMapObjectPointX2,psapMapObjectPointY2,psapMapObjectPointX3,psapMapObjectPointY3,psapMapObjectPointX4,psapMapObjectPointY4

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(psapMapObject, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.psapMapObjectType is None:
        self.psapMapObjectType = 0
      if self.psapMapObjectValid is None:
        self.psapMapObjectValid = False
      if self.psapMapObjectPointX1 is None:
        self.psapMapObjectPointX1 = 0.
      if self.psapMapObjectPointY1 is None:
        self.psapMapObjectPointY1 = 0.
      if self.psapMapObjectPointX2 is None:
        self.psapMapObjectPointX2 = 0.
      if self.psapMapObjectPointY2 is None:
        self.psapMapObjectPointY2 = 0.
      if self.psapMapObjectPointX3 is None:
        self.psapMapObjectPointX3 = 0.
      if self.psapMapObjectPointY3 is None:
        self.psapMapObjectPointY3 = 0.
      if self.psapMapObjectPointX4 is None:
        self.psapMapObjectPointX4 = 0.
      if self.psapMapObjectPointY4 is None:
        self.psapMapObjectPointY4 = 0.
    else:
      self.psapMapObjectType = 0
      self.psapMapObjectValid = False
      self.psapMapObjectPointX1 = 0.
      self.psapMapObjectPointY1 = 0.
      self.psapMapObjectPointX2 = 0.
      self.psapMapObjectPointY2 = 0.
      self.psapMapObjectPointX3 = 0.
      self.psapMapObjectPointY3 = 0.
      self.psapMapObjectPointX4 = 0.
      self.psapMapObjectPointY4 = 0.

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
      buff.write(_get_struct_iB8f().pack(_x.psapMapObjectType, _x.psapMapObjectValid, _x.psapMapObjectPointX1, _x.psapMapObjectPointY1, _x.psapMapObjectPointX2, _x.psapMapObjectPointY2, _x.psapMapObjectPointX3, _x.psapMapObjectPointY3, _x.psapMapObjectPointX4, _x.psapMapObjectPointY4))
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
      (_x.psapMapObjectType, _x.psapMapObjectValid, _x.psapMapObjectPointX1, _x.psapMapObjectPointY1, _x.psapMapObjectPointX2, _x.psapMapObjectPointY2, _x.psapMapObjectPointX3, _x.psapMapObjectPointY3, _x.psapMapObjectPointX4, _x.psapMapObjectPointY4,) = _get_struct_iB8f().unpack(str[start:end])
      self.psapMapObjectValid = bool(self.psapMapObjectValid)
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
      buff.write(_get_struct_iB8f().pack(_x.psapMapObjectType, _x.psapMapObjectValid, _x.psapMapObjectPointX1, _x.psapMapObjectPointY1, _x.psapMapObjectPointX2, _x.psapMapObjectPointY2, _x.psapMapObjectPointX3, _x.psapMapObjectPointY3, _x.psapMapObjectPointX4, _x.psapMapObjectPointY4))
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
      (_x.psapMapObjectType, _x.psapMapObjectValid, _x.psapMapObjectPointX1, _x.psapMapObjectPointY1, _x.psapMapObjectPointX2, _x.psapMapObjectPointY2, _x.psapMapObjectPointX3, _x.psapMapObjectPointY3, _x.psapMapObjectPointX4, _x.psapMapObjectPointY4,) = _get_struct_iB8f().unpack(str[start:end])
      self.psapMapObjectValid = bool(self.psapMapObjectValid)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_iB8f = None
def _get_struct_iB8f():
    global _struct_iB8f
    if _struct_iB8f is None:
        _struct_iB8f = struct.Struct("<iB8f")
    return _struct_iB8f

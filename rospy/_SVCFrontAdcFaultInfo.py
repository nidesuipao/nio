# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from rospy_message_converter/SVCFrontAdcFaultInfo.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class SVCFrontAdcFaultInfo(genpy.Message):
  _md5sum = "68426f0c142c10415f6a631f33c00901"
  _type = "rospy_message_converter/SVCFrontAdcFaultInfo"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """bool SVCFront_DES4_LinkNotLocked
bool SVCFront_DES4_VideoNotLocked
"""
  __slots__ = ['SVCFront_DES4_LinkNotLocked','SVCFront_DES4_VideoNotLocked']
  _slot_types = ['bool','bool']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       SVCFront_DES4_LinkNotLocked,SVCFront_DES4_VideoNotLocked

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(SVCFrontAdcFaultInfo, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.SVCFront_DES4_LinkNotLocked is None:
        self.SVCFront_DES4_LinkNotLocked = False
      if self.SVCFront_DES4_VideoNotLocked is None:
        self.SVCFront_DES4_VideoNotLocked = False
    else:
      self.SVCFront_DES4_LinkNotLocked = False
      self.SVCFront_DES4_VideoNotLocked = False

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
      buff.write(_get_struct_2B().pack(_x.SVCFront_DES4_LinkNotLocked, _x.SVCFront_DES4_VideoNotLocked))
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
      end += 2
      (_x.SVCFront_DES4_LinkNotLocked, _x.SVCFront_DES4_VideoNotLocked,) = _get_struct_2B().unpack(str[start:end])
      self.SVCFront_DES4_LinkNotLocked = bool(self.SVCFront_DES4_LinkNotLocked)
      self.SVCFront_DES4_VideoNotLocked = bool(self.SVCFront_DES4_VideoNotLocked)
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
      buff.write(_get_struct_2B().pack(_x.SVCFront_DES4_LinkNotLocked, _x.SVCFront_DES4_VideoNotLocked))
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
      end += 2
      (_x.SVCFront_DES4_LinkNotLocked, _x.SVCFront_DES4_VideoNotLocked,) = _get_struct_2B().unpack(str[start:end])
      self.SVCFront_DES4_LinkNotLocked = bool(self.SVCFront_DES4_LinkNotLocked)
      self.SVCFront_DES4_VideoNotLocked = bool(self.SVCFront_DES4_VideoNotLocked)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_2B = None
def _get_struct_2B():
    global _struct_2B
    if _struct_2B is None:
        _struct_2B = struct.Struct("<2B")
    return _struct_2B

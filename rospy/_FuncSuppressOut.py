# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from rospy_message_converter/FuncSuppressOut.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class FuncSuppressOut(genpy.Message):
  _md5sum = "7d43b032d795052eaf83c4803d6e1881"
  _type = "rospy_message_converter/FuncSuppressOut"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """bool Aeb_Suppress
bool Fcw_Suppress
bool Aebrear_Suppress
bool Fcwrear_Suppress
"""
  __slots__ = ['Aeb_Suppress','Fcw_Suppress','Aebrear_Suppress','Fcwrear_Suppress']
  _slot_types = ['bool','bool','bool','bool']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       Aeb_Suppress,Fcw_Suppress,Aebrear_Suppress,Fcwrear_Suppress

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(FuncSuppressOut, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.Aeb_Suppress is None:
        self.Aeb_Suppress = False
      if self.Fcw_Suppress is None:
        self.Fcw_Suppress = False
      if self.Aebrear_Suppress is None:
        self.Aebrear_Suppress = False
      if self.Fcwrear_Suppress is None:
        self.Fcwrear_Suppress = False
    else:
      self.Aeb_Suppress = False
      self.Fcw_Suppress = False
      self.Aebrear_Suppress = False
      self.Fcwrear_Suppress = False

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
      buff.write(_get_struct_4B().pack(_x.Aeb_Suppress, _x.Fcw_Suppress, _x.Aebrear_Suppress, _x.Fcwrear_Suppress))
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
      end += 4
      (_x.Aeb_Suppress, _x.Fcw_Suppress, _x.Aebrear_Suppress, _x.Fcwrear_Suppress,) = _get_struct_4B().unpack(str[start:end])
      self.Aeb_Suppress = bool(self.Aeb_Suppress)
      self.Fcw_Suppress = bool(self.Fcw_Suppress)
      self.Aebrear_Suppress = bool(self.Aebrear_Suppress)
      self.Fcwrear_Suppress = bool(self.Fcwrear_Suppress)
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
      buff.write(_get_struct_4B().pack(_x.Aeb_Suppress, _x.Fcw_Suppress, _x.Aebrear_Suppress, _x.Fcwrear_Suppress))
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
      end += 4
      (_x.Aeb_Suppress, _x.Fcw_Suppress, _x.Aebrear_Suppress, _x.Fcwrear_Suppress,) = _get_struct_4B().unpack(str[start:end])
      self.Aeb_Suppress = bool(self.Aeb_Suppress)
      self.Fcw_Suppress = bool(self.Fcw_Suppress)
      self.Aebrear_Suppress = bool(self.Aebrear_Suppress)
      self.Fcwrear_Suppress = bool(self.Fcwrear_Suppress)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_4B = None
def _get_struct_4B():
    global _struct_4B
    if _struct_4B is None:
        _struct_4B = struct.Struct("<4B")
    return _struct_4B

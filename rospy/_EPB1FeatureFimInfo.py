# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from rospy_message_converter/EPB1FeatureFimInfo.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class EPB1FeatureFimInfo(genpy.Message):
  _md5sum = "512ec9a442f34f07833be181dd3c2471"
  _type = "rospy_message_converter/EPB1FeatureFimInfo"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """bool FIM_CHS1_EPB1_EPB1_SwtSts_Invalid
bool FIM_CHS1_EPB1_EPBSts_Invalid
bool FIM_CHS1_EPB1_EPBFailLampReq_Invalid
bool FIM_CHS1_EPB1_EPB1_Mod_Invalid
"""
  __slots__ = ['FIM_CHS1_EPB1_EPB1_SwtSts_Invalid','FIM_CHS1_EPB1_EPBSts_Invalid','FIM_CHS1_EPB1_EPBFailLampReq_Invalid','FIM_CHS1_EPB1_EPB1_Mod_Invalid']
  _slot_types = ['bool','bool','bool','bool']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       FIM_CHS1_EPB1_EPB1_SwtSts_Invalid,FIM_CHS1_EPB1_EPBSts_Invalid,FIM_CHS1_EPB1_EPBFailLampReq_Invalid,FIM_CHS1_EPB1_EPB1_Mod_Invalid

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(EPB1FeatureFimInfo, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.FIM_CHS1_EPB1_EPB1_SwtSts_Invalid is None:
        self.FIM_CHS1_EPB1_EPB1_SwtSts_Invalid = False
      if self.FIM_CHS1_EPB1_EPBSts_Invalid is None:
        self.FIM_CHS1_EPB1_EPBSts_Invalid = False
      if self.FIM_CHS1_EPB1_EPBFailLampReq_Invalid is None:
        self.FIM_CHS1_EPB1_EPBFailLampReq_Invalid = False
      if self.FIM_CHS1_EPB1_EPB1_Mod_Invalid is None:
        self.FIM_CHS1_EPB1_EPB1_Mod_Invalid = False
    else:
      self.FIM_CHS1_EPB1_EPB1_SwtSts_Invalid = False
      self.FIM_CHS1_EPB1_EPBSts_Invalid = False
      self.FIM_CHS1_EPB1_EPBFailLampReq_Invalid = False
      self.FIM_CHS1_EPB1_EPB1_Mod_Invalid = False

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
      buff.write(_get_struct_4B().pack(_x.FIM_CHS1_EPB1_EPB1_SwtSts_Invalid, _x.FIM_CHS1_EPB1_EPBSts_Invalid, _x.FIM_CHS1_EPB1_EPBFailLampReq_Invalid, _x.FIM_CHS1_EPB1_EPB1_Mod_Invalid))
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
      (_x.FIM_CHS1_EPB1_EPB1_SwtSts_Invalid, _x.FIM_CHS1_EPB1_EPBSts_Invalid, _x.FIM_CHS1_EPB1_EPBFailLampReq_Invalid, _x.FIM_CHS1_EPB1_EPB1_Mod_Invalid,) = _get_struct_4B().unpack(str[start:end])
      self.FIM_CHS1_EPB1_EPB1_SwtSts_Invalid = bool(self.FIM_CHS1_EPB1_EPB1_SwtSts_Invalid)
      self.FIM_CHS1_EPB1_EPBSts_Invalid = bool(self.FIM_CHS1_EPB1_EPBSts_Invalid)
      self.FIM_CHS1_EPB1_EPBFailLampReq_Invalid = bool(self.FIM_CHS1_EPB1_EPBFailLampReq_Invalid)
      self.FIM_CHS1_EPB1_EPB1_Mod_Invalid = bool(self.FIM_CHS1_EPB1_EPB1_Mod_Invalid)
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
      buff.write(_get_struct_4B().pack(_x.FIM_CHS1_EPB1_EPB1_SwtSts_Invalid, _x.FIM_CHS1_EPB1_EPBSts_Invalid, _x.FIM_CHS1_EPB1_EPBFailLampReq_Invalid, _x.FIM_CHS1_EPB1_EPB1_Mod_Invalid))
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
      (_x.FIM_CHS1_EPB1_EPB1_SwtSts_Invalid, _x.FIM_CHS1_EPB1_EPBSts_Invalid, _x.FIM_CHS1_EPB1_EPBFailLampReq_Invalid, _x.FIM_CHS1_EPB1_EPB1_Mod_Invalid,) = _get_struct_4B().unpack(str[start:end])
      self.FIM_CHS1_EPB1_EPB1_SwtSts_Invalid = bool(self.FIM_CHS1_EPB1_EPB1_SwtSts_Invalid)
      self.FIM_CHS1_EPB1_EPBSts_Invalid = bool(self.FIM_CHS1_EPB1_EPBSts_Invalid)
      self.FIM_CHS1_EPB1_EPBFailLampReq_Invalid = bool(self.FIM_CHS1_EPB1_EPBFailLampReq_Invalid)
      self.FIM_CHS1_EPB1_EPB1_Mod_Invalid = bool(self.FIM_CHS1_EPB1_EPB1_Mod_Invalid)
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

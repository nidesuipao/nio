# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from rospy_message_converter/VCUFaultInfo.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class VCUFaultInfo(genpy.Message):
  _md5sum = "42b52b84d8155ae1e57a34a0653b323c"
  _type = "rospy_message_converter/VCUFaultInfo"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """bool CHS1_VCU_LossCom
bool CHS2_VCU_LossCom
bool CHS1_VCU_13_MsgError
bool CHS1_VCU_05_MsgError
bool CHS1_VCU_02_MsgError
bool CHS1_VCU_HealthMngt_MsgError
bool CHS2_VCU_13_MsgError
bool CHS2_VCU_HealthMngt_MsgError
bool CHS1_VCU_CDC_328_MsgError
"""
  __slots__ = ['CHS1_VCU_LossCom','CHS2_VCU_LossCom','CHS1_VCU_13_MsgError','CHS1_VCU_05_MsgError','CHS1_VCU_02_MsgError','CHS1_VCU_HealthMngt_MsgError','CHS2_VCU_13_MsgError','CHS2_VCU_HealthMngt_MsgError','CHS1_VCU_CDC_328_MsgError']
  _slot_types = ['bool','bool','bool','bool','bool','bool','bool','bool','bool']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       CHS1_VCU_LossCom,CHS2_VCU_LossCom,CHS1_VCU_13_MsgError,CHS1_VCU_05_MsgError,CHS1_VCU_02_MsgError,CHS1_VCU_HealthMngt_MsgError,CHS2_VCU_13_MsgError,CHS2_VCU_HealthMngt_MsgError,CHS1_VCU_CDC_328_MsgError

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(VCUFaultInfo, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.CHS1_VCU_LossCom is None:
        self.CHS1_VCU_LossCom = False
      if self.CHS2_VCU_LossCom is None:
        self.CHS2_VCU_LossCom = False
      if self.CHS1_VCU_13_MsgError is None:
        self.CHS1_VCU_13_MsgError = False
      if self.CHS1_VCU_05_MsgError is None:
        self.CHS1_VCU_05_MsgError = False
      if self.CHS1_VCU_02_MsgError is None:
        self.CHS1_VCU_02_MsgError = False
      if self.CHS1_VCU_HealthMngt_MsgError is None:
        self.CHS1_VCU_HealthMngt_MsgError = False
      if self.CHS2_VCU_13_MsgError is None:
        self.CHS2_VCU_13_MsgError = False
      if self.CHS2_VCU_HealthMngt_MsgError is None:
        self.CHS2_VCU_HealthMngt_MsgError = False
      if self.CHS1_VCU_CDC_328_MsgError is None:
        self.CHS1_VCU_CDC_328_MsgError = False
    else:
      self.CHS1_VCU_LossCom = False
      self.CHS2_VCU_LossCom = False
      self.CHS1_VCU_13_MsgError = False
      self.CHS1_VCU_05_MsgError = False
      self.CHS1_VCU_02_MsgError = False
      self.CHS1_VCU_HealthMngt_MsgError = False
      self.CHS2_VCU_13_MsgError = False
      self.CHS2_VCU_HealthMngt_MsgError = False
      self.CHS1_VCU_CDC_328_MsgError = False

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
      buff.write(_get_struct_9B().pack(_x.CHS1_VCU_LossCom, _x.CHS2_VCU_LossCom, _x.CHS1_VCU_13_MsgError, _x.CHS1_VCU_05_MsgError, _x.CHS1_VCU_02_MsgError, _x.CHS1_VCU_HealthMngt_MsgError, _x.CHS2_VCU_13_MsgError, _x.CHS2_VCU_HealthMngt_MsgError, _x.CHS1_VCU_CDC_328_MsgError))
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
      end += 9
      (_x.CHS1_VCU_LossCom, _x.CHS2_VCU_LossCom, _x.CHS1_VCU_13_MsgError, _x.CHS1_VCU_05_MsgError, _x.CHS1_VCU_02_MsgError, _x.CHS1_VCU_HealthMngt_MsgError, _x.CHS2_VCU_13_MsgError, _x.CHS2_VCU_HealthMngt_MsgError, _x.CHS1_VCU_CDC_328_MsgError,) = _get_struct_9B().unpack(str[start:end])
      self.CHS1_VCU_LossCom = bool(self.CHS1_VCU_LossCom)
      self.CHS2_VCU_LossCom = bool(self.CHS2_VCU_LossCom)
      self.CHS1_VCU_13_MsgError = bool(self.CHS1_VCU_13_MsgError)
      self.CHS1_VCU_05_MsgError = bool(self.CHS1_VCU_05_MsgError)
      self.CHS1_VCU_02_MsgError = bool(self.CHS1_VCU_02_MsgError)
      self.CHS1_VCU_HealthMngt_MsgError = bool(self.CHS1_VCU_HealthMngt_MsgError)
      self.CHS2_VCU_13_MsgError = bool(self.CHS2_VCU_13_MsgError)
      self.CHS2_VCU_HealthMngt_MsgError = bool(self.CHS2_VCU_HealthMngt_MsgError)
      self.CHS1_VCU_CDC_328_MsgError = bool(self.CHS1_VCU_CDC_328_MsgError)
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
      buff.write(_get_struct_9B().pack(_x.CHS1_VCU_LossCom, _x.CHS2_VCU_LossCom, _x.CHS1_VCU_13_MsgError, _x.CHS1_VCU_05_MsgError, _x.CHS1_VCU_02_MsgError, _x.CHS1_VCU_HealthMngt_MsgError, _x.CHS2_VCU_13_MsgError, _x.CHS2_VCU_HealthMngt_MsgError, _x.CHS1_VCU_CDC_328_MsgError))
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
      end += 9
      (_x.CHS1_VCU_LossCom, _x.CHS2_VCU_LossCom, _x.CHS1_VCU_13_MsgError, _x.CHS1_VCU_05_MsgError, _x.CHS1_VCU_02_MsgError, _x.CHS1_VCU_HealthMngt_MsgError, _x.CHS2_VCU_13_MsgError, _x.CHS2_VCU_HealthMngt_MsgError, _x.CHS1_VCU_CDC_328_MsgError,) = _get_struct_9B().unpack(str[start:end])
      self.CHS1_VCU_LossCom = bool(self.CHS1_VCU_LossCom)
      self.CHS2_VCU_LossCom = bool(self.CHS2_VCU_LossCom)
      self.CHS1_VCU_13_MsgError = bool(self.CHS1_VCU_13_MsgError)
      self.CHS1_VCU_05_MsgError = bool(self.CHS1_VCU_05_MsgError)
      self.CHS1_VCU_02_MsgError = bool(self.CHS1_VCU_02_MsgError)
      self.CHS1_VCU_HealthMngt_MsgError = bool(self.CHS1_VCU_HealthMngt_MsgError)
      self.CHS2_VCU_13_MsgError = bool(self.CHS2_VCU_13_MsgError)
      self.CHS2_VCU_HealthMngt_MsgError = bool(self.CHS2_VCU_HealthMngt_MsgError)
      self.CHS1_VCU_CDC_328_MsgError = bool(self.CHS1_VCU_CDC_328_MsgError)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_9B = None
def _get_struct_9B():
    global _struct_9B
    if _struct_9B is None:
        _struct_9B = struct.Struct("<9B")
    return _struct_9B

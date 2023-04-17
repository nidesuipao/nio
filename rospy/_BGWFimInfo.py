# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from rospy_message_converter/BGWFimInfo.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class BGWFimInfo(genpy.Message):
  _md5sum = "89c5d442df3d49b5694f26d744aa164c"
  _type = "rospy_message_converter/BGWFimInfo"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """bool FIM_CHS1_BGW_01_MsgError
bool FIM_CHS1_BGW_02_MsgError
bool FIM_CHS1_BGW_03_MsgError
bool FIM_CHS1_BGW_LI_MsgError
bool FIM_CHS1_BGW_TCU_01_MsgError
bool FIM_CHS1_BGW_WIPR_MsgError
bool FIM_ADAS_BGW_POWER_SWAP_MsgError
bool FIM_ADAS_BGW_SCU_D_02_MsgError
bool FIM_ADAS_BGW_SCU_P_01_MsgError
bool FIM_ADAS_BGW_SCU_P_02_MsgError
bool FIM_ADAS_BGW_SNSR_MsgError
bool FIM_ADAS_BGW_STEERWHL_CMD_MsgError
bool FIM_CHS1_BGW_CAN_Error
bool FIM_ADAS_BGW_CAN_Error
"""
  __slots__ = ['FIM_CHS1_BGW_01_MsgError','FIM_CHS1_BGW_02_MsgError','FIM_CHS1_BGW_03_MsgError','FIM_CHS1_BGW_LI_MsgError','FIM_CHS1_BGW_TCU_01_MsgError','FIM_CHS1_BGW_WIPR_MsgError','FIM_ADAS_BGW_POWER_SWAP_MsgError','FIM_ADAS_BGW_SCU_D_02_MsgError','FIM_ADAS_BGW_SCU_P_01_MsgError','FIM_ADAS_BGW_SCU_P_02_MsgError','FIM_ADAS_BGW_SNSR_MsgError','FIM_ADAS_BGW_STEERWHL_CMD_MsgError','FIM_CHS1_BGW_CAN_Error','FIM_ADAS_BGW_CAN_Error']
  _slot_types = ['bool','bool','bool','bool','bool','bool','bool','bool','bool','bool','bool','bool','bool','bool']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       FIM_CHS1_BGW_01_MsgError,FIM_CHS1_BGW_02_MsgError,FIM_CHS1_BGW_03_MsgError,FIM_CHS1_BGW_LI_MsgError,FIM_CHS1_BGW_TCU_01_MsgError,FIM_CHS1_BGW_WIPR_MsgError,FIM_ADAS_BGW_POWER_SWAP_MsgError,FIM_ADAS_BGW_SCU_D_02_MsgError,FIM_ADAS_BGW_SCU_P_01_MsgError,FIM_ADAS_BGW_SCU_P_02_MsgError,FIM_ADAS_BGW_SNSR_MsgError,FIM_ADAS_BGW_STEERWHL_CMD_MsgError,FIM_CHS1_BGW_CAN_Error,FIM_ADAS_BGW_CAN_Error

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(BGWFimInfo, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.FIM_CHS1_BGW_01_MsgError is None:
        self.FIM_CHS1_BGW_01_MsgError = False
      if self.FIM_CHS1_BGW_02_MsgError is None:
        self.FIM_CHS1_BGW_02_MsgError = False
      if self.FIM_CHS1_BGW_03_MsgError is None:
        self.FIM_CHS1_BGW_03_MsgError = False
      if self.FIM_CHS1_BGW_LI_MsgError is None:
        self.FIM_CHS1_BGW_LI_MsgError = False
      if self.FIM_CHS1_BGW_TCU_01_MsgError is None:
        self.FIM_CHS1_BGW_TCU_01_MsgError = False
      if self.FIM_CHS1_BGW_WIPR_MsgError is None:
        self.FIM_CHS1_BGW_WIPR_MsgError = False
      if self.FIM_ADAS_BGW_POWER_SWAP_MsgError is None:
        self.FIM_ADAS_BGW_POWER_SWAP_MsgError = False
      if self.FIM_ADAS_BGW_SCU_D_02_MsgError is None:
        self.FIM_ADAS_BGW_SCU_D_02_MsgError = False
      if self.FIM_ADAS_BGW_SCU_P_01_MsgError is None:
        self.FIM_ADAS_BGW_SCU_P_01_MsgError = False
      if self.FIM_ADAS_BGW_SCU_P_02_MsgError is None:
        self.FIM_ADAS_BGW_SCU_P_02_MsgError = False
      if self.FIM_ADAS_BGW_SNSR_MsgError is None:
        self.FIM_ADAS_BGW_SNSR_MsgError = False
      if self.FIM_ADAS_BGW_STEERWHL_CMD_MsgError is None:
        self.FIM_ADAS_BGW_STEERWHL_CMD_MsgError = False
      if self.FIM_CHS1_BGW_CAN_Error is None:
        self.FIM_CHS1_BGW_CAN_Error = False
      if self.FIM_ADAS_BGW_CAN_Error is None:
        self.FIM_ADAS_BGW_CAN_Error = False
    else:
      self.FIM_CHS1_BGW_01_MsgError = False
      self.FIM_CHS1_BGW_02_MsgError = False
      self.FIM_CHS1_BGW_03_MsgError = False
      self.FIM_CHS1_BGW_LI_MsgError = False
      self.FIM_CHS1_BGW_TCU_01_MsgError = False
      self.FIM_CHS1_BGW_WIPR_MsgError = False
      self.FIM_ADAS_BGW_POWER_SWAP_MsgError = False
      self.FIM_ADAS_BGW_SCU_D_02_MsgError = False
      self.FIM_ADAS_BGW_SCU_P_01_MsgError = False
      self.FIM_ADAS_BGW_SCU_P_02_MsgError = False
      self.FIM_ADAS_BGW_SNSR_MsgError = False
      self.FIM_ADAS_BGW_STEERWHL_CMD_MsgError = False
      self.FIM_CHS1_BGW_CAN_Error = False
      self.FIM_ADAS_BGW_CAN_Error = False

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
      buff.write(_get_struct_14B().pack(_x.FIM_CHS1_BGW_01_MsgError, _x.FIM_CHS1_BGW_02_MsgError, _x.FIM_CHS1_BGW_03_MsgError, _x.FIM_CHS1_BGW_LI_MsgError, _x.FIM_CHS1_BGW_TCU_01_MsgError, _x.FIM_CHS1_BGW_WIPR_MsgError, _x.FIM_ADAS_BGW_POWER_SWAP_MsgError, _x.FIM_ADAS_BGW_SCU_D_02_MsgError, _x.FIM_ADAS_BGW_SCU_P_01_MsgError, _x.FIM_ADAS_BGW_SCU_P_02_MsgError, _x.FIM_ADAS_BGW_SNSR_MsgError, _x.FIM_ADAS_BGW_STEERWHL_CMD_MsgError, _x.FIM_CHS1_BGW_CAN_Error, _x.FIM_ADAS_BGW_CAN_Error))
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
      end += 14
      (_x.FIM_CHS1_BGW_01_MsgError, _x.FIM_CHS1_BGW_02_MsgError, _x.FIM_CHS1_BGW_03_MsgError, _x.FIM_CHS1_BGW_LI_MsgError, _x.FIM_CHS1_BGW_TCU_01_MsgError, _x.FIM_CHS1_BGW_WIPR_MsgError, _x.FIM_ADAS_BGW_POWER_SWAP_MsgError, _x.FIM_ADAS_BGW_SCU_D_02_MsgError, _x.FIM_ADAS_BGW_SCU_P_01_MsgError, _x.FIM_ADAS_BGW_SCU_P_02_MsgError, _x.FIM_ADAS_BGW_SNSR_MsgError, _x.FIM_ADAS_BGW_STEERWHL_CMD_MsgError, _x.FIM_CHS1_BGW_CAN_Error, _x.FIM_ADAS_BGW_CAN_Error,) = _get_struct_14B().unpack(str[start:end])
      self.FIM_CHS1_BGW_01_MsgError = bool(self.FIM_CHS1_BGW_01_MsgError)
      self.FIM_CHS1_BGW_02_MsgError = bool(self.FIM_CHS1_BGW_02_MsgError)
      self.FIM_CHS1_BGW_03_MsgError = bool(self.FIM_CHS1_BGW_03_MsgError)
      self.FIM_CHS1_BGW_LI_MsgError = bool(self.FIM_CHS1_BGW_LI_MsgError)
      self.FIM_CHS1_BGW_TCU_01_MsgError = bool(self.FIM_CHS1_BGW_TCU_01_MsgError)
      self.FIM_CHS1_BGW_WIPR_MsgError = bool(self.FIM_CHS1_BGW_WIPR_MsgError)
      self.FIM_ADAS_BGW_POWER_SWAP_MsgError = bool(self.FIM_ADAS_BGW_POWER_SWAP_MsgError)
      self.FIM_ADAS_BGW_SCU_D_02_MsgError = bool(self.FIM_ADAS_BGW_SCU_D_02_MsgError)
      self.FIM_ADAS_BGW_SCU_P_01_MsgError = bool(self.FIM_ADAS_BGW_SCU_P_01_MsgError)
      self.FIM_ADAS_BGW_SCU_P_02_MsgError = bool(self.FIM_ADAS_BGW_SCU_P_02_MsgError)
      self.FIM_ADAS_BGW_SNSR_MsgError = bool(self.FIM_ADAS_BGW_SNSR_MsgError)
      self.FIM_ADAS_BGW_STEERWHL_CMD_MsgError = bool(self.FIM_ADAS_BGW_STEERWHL_CMD_MsgError)
      self.FIM_CHS1_BGW_CAN_Error = bool(self.FIM_CHS1_BGW_CAN_Error)
      self.FIM_ADAS_BGW_CAN_Error = bool(self.FIM_ADAS_BGW_CAN_Error)
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
      buff.write(_get_struct_14B().pack(_x.FIM_CHS1_BGW_01_MsgError, _x.FIM_CHS1_BGW_02_MsgError, _x.FIM_CHS1_BGW_03_MsgError, _x.FIM_CHS1_BGW_LI_MsgError, _x.FIM_CHS1_BGW_TCU_01_MsgError, _x.FIM_CHS1_BGW_WIPR_MsgError, _x.FIM_ADAS_BGW_POWER_SWAP_MsgError, _x.FIM_ADAS_BGW_SCU_D_02_MsgError, _x.FIM_ADAS_BGW_SCU_P_01_MsgError, _x.FIM_ADAS_BGW_SCU_P_02_MsgError, _x.FIM_ADAS_BGW_SNSR_MsgError, _x.FIM_ADAS_BGW_STEERWHL_CMD_MsgError, _x.FIM_CHS1_BGW_CAN_Error, _x.FIM_ADAS_BGW_CAN_Error))
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
      end += 14
      (_x.FIM_CHS1_BGW_01_MsgError, _x.FIM_CHS1_BGW_02_MsgError, _x.FIM_CHS1_BGW_03_MsgError, _x.FIM_CHS1_BGW_LI_MsgError, _x.FIM_CHS1_BGW_TCU_01_MsgError, _x.FIM_CHS1_BGW_WIPR_MsgError, _x.FIM_ADAS_BGW_POWER_SWAP_MsgError, _x.FIM_ADAS_BGW_SCU_D_02_MsgError, _x.FIM_ADAS_BGW_SCU_P_01_MsgError, _x.FIM_ADAS_BGW_SCU_P_02_MsgError, _x.FIM_ADAS_BGW_SNSR_MsgError, _x.FIM_ADAS_BGW_STEERWHL_CMD_MsgError, _x.FIM_CHS1_BGW_CAN_Error, _x.FIM_ADAS_BGW_CAN_Error,) = _get_struct_14B().unpack(str[start:end])
      self.FIM_CHS1_BGW_01_MsgError = bool(self.FIM_CHS1_BGW_01_MsgError)
      self.FIM_CHS1_BGW_02_MsgError = bool(self.FIM_CHS1_BGW_02_MsgError)
      self.FIM_CHS1_BGW_03_MsgError = bool(self.FIM_CHS1_BGW_03_MsgError)
      self.FIM_CHS1_BGW_LI_MsgError = bool(self.FIM_CHS1_BGW_LI_MsgError)
      self.FIM_CHS1_BGW_TCU_01_MsgError = bool(self.FIM_CHS1_BGW_TCU_01_MsgError)
      self.FIM_CHS1_BGW_WIPR_MsgError = bool(self.FIM_CHS1_BGW_WIPR_MsgError)
      self.FIM_ADAS_BGW_POWER_SWAP_MsgError = bool(self.FIM_ADAS_BGW_POWER_SWAP_MsgError)
      self.FIM_ADAS_BGW_SCU_D_02_MsgError = bool(self.FIM_ADAS_BGW_SCU_D_02_MsgError)
      self.FIM_ADAS_BGW_SCU_P_01_MsgError = bool(self.FIM_ADAS_BGW_SCU_P_01_MsgError)
      self.FIM_ADAS_BGW_SCU_P_02_MsgError = bool(self.FIM_ADAS_BGW_SCU_P_02_MsgError)
      self.FIM_ADAS_BGW_SNSR_MsgError = bool(self.FIM_ADAS_BGW_SNSR_MsgError)
      self.FIM_ADAS_BGW_STEERWHL_CMD_MsgError = bool(self.FIM_ADAS_BGW_STEERWHL_CMD_MsgError)
      self.FIM_CHS1_BGW_CAN_Error = bool(self.FIM_CHS1_BGW_CAN_Error)
      self.FIM_ADAS_BGW_CAN_Error = bool(self.FIM_ADAS_BGW_CAN_Error)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_14B = None
def _get_struct_14B():
    global _struct_14B
    if _struct_14B is None:
        _struct_14B = struct.Struct("<14B")
    return _struct_14B

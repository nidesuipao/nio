# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from rospy_message_converter/BCUFeatureFimInfo.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class BCUFeatureFimInfo(genpy.Message):
  _md5sum = "4e5e3e8b101c7b324683a45fe09900b1"
  _type = "rospy_message_converter/BCUFeatureFimInfo"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """bool FIM_CHS1_BCU_WhlSpdMovgDir_Invalid
bool FIM_CHS1_BCU_WhlSpdSts_invalid
bool FIM_CHS1_BCU_WhlPlsCntr_Invalid
bool FIM_CHS1_BCU_VehSpdSts_Invalid
bool FIM_CHS1_BCU_BrkPressValid_Invalid
bool FIM_CHS1_BCU_BrkPedlSts_Invalid
bool FIM_CHS1_BCU_VehMovgDir_Invalid
bool FIM_CHS1_BCU_BrkPressOffsetValid_Invalid
bool FIM_CHS1_BCU_HDCSts_Invalid
bool FIM_CHS1_BCU_AVHSts_Invalid
bool FIM_CHS1_BCU_VehSpdSts_ASILD_Invalid
bool FIM_CHS1_BCU_ABSFailLampReq_LampOn
bool FIM_CHS1_VDCTCSFailLampReq
bool FIM_CHS1_AutoBrkgAvl_Invalid
bool FIM_CHS1_AWBAvl_Invalid
bool FIM_CHS1_BrkOverHeat
bool FIM_CHS1_ABAAvl_NotAvailable
bool FIM_CHS1_ABPAvl_NotAvailable
"""
  __slots__ = ['FIM_CHS1_BCU_WhlSpdMovgDir_Invalid','FIM_CHS1_BCU_WhlSpdSts_invalid','FIM_CHS1_BCU_WhlPlsCntr_Invalid','FIM_CHS1_BCU_VehSpdSts_Invalid','FIM_CHS1_BCU_BrkPressValid_Invalid','FIM_CHS1_BCU_BrkPedlSts_Invalid','FIM_CHS1_BCU_VehMovgDir_Invalid','FIM_CHS1_BCU_BrkPressOffsetValid_Invalid','FIM_CHS1_BCU_HDCSts_Invalid','FIM_CHS1_BCU_AVHSts_Invalid','FIM_CHS1_BCU_VehSpdSts_ASILD_Invalid','FIM_CHS1_BCU_ABSFailLampReq_LampOn','FIM_CHS1_VDCTCSFailLampReq','FIM_CHS1_AutoBrkgAvl_Invalid','FIM_CHS1_AWBAvl_Invalid','FIM_CHS1_BrkOverHeat','FIM_CHS1_ABAAvl_NotAvailable','FIM_CHS1_ABPAvl_NotAvailable']
  _slot_types = ['bool','bool','bool','bool','bool','bool','bool','bool','bool','bool','bool','bool','bool','bool','bool','bool','bool','bool']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       FIM_CHS1_BCU_WhlSpdMovgDir_Invalid,FIM_CHS1_BCU_WhlSpdSts_invalid,FIM_CHS1_BCU_WhlPlsCntr_Invalid,FIM_CHS1_BCU_VehSpdSts_Invalid,FIM_CHS1_BCU_BrkPressValid_Invalid,FIM_CHS1_BCU_BrkPedlSts_Invalid,FIM_CHS1_BCU_VehMovgDir_Invalid,FIM_CHS1_BCU_BrkPressOffsetValid_Invalid,FIM_CHS1_BCU_HDCSts_Invalid,FIM_CHS1_BCU_AVHSts_Invalid,FIM_CHS1_BCU_VehSpdSts_ASILD_Invalid,FIM_CHS1_BCU_ABSFailLampReq_LampOn,FIM_CHS1_VDCTCSFailLampReq,FIM_CHS1_AutoBrkgAvl_Invalid,FIM_CHS1_AWBAvl_Invalid,FIM_CHS1_BrkOverHeat,FIM_CHS1_ABAAvl_NotAvailable,FIM_CHS1_ABPAvl_NotAvailable

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(BCUFeatureFimInfo, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.FIM_CHS1_BCU_WhlSpdMovgDir_Invalid is None:
        self.FIM_CHS1_BCU_WhlSpdMovgDir_Invalid = False
      if self.FIM_CHS1_BCU_WhlSpdSts_invalid is None:
        self.FIM_CHS1_BCU_WhlSpdSts_invalid = False
      if self.FIM_CHS1_BCU_WhlPlsCntr_Invalid is None:
        self.FIM_CHS1_BCU_WhlPlsCntr_Invalid = False
      if self.FIM_CHS1_BCU_VehSpdSts_Invalid is None:
        self.FIM_CHS1_BCU_VehSpdSts_Invalid = False
      if self.FIM_CHS1_BCU_BrkPressValid_Invalid is None:
        self.FIM_CHS1_BCU_BrkPressValid_Invalid = False
      if self.FIM_CHS1_BCU_BrkPedlSts_Invalid is None:
        self.FIM_CHS1_BCU_BrkPedlSts_Invalid = False
      if self.FIM_CHS1_BCU_VehMovgDir_Invalid is None:
        self.FIM_CHS1_BCU_VehMovgDir_Invalid = False
      if self.FIM_CHS1_BCU_BrkPressOffsetValid_Invalid is None:
        self.FIM_CHS1_BCU_BrkPressOffsetValid_Invalid = False
      if self.FIM_CHS1_BCU_HDCSts_Invalid is None:
        self.FIM_CHS1_BCU_HDCSts_Invalid = False
      if self.FIM_CHS1_BCU_AVHSts_Invalid is None:
        self.FIM_CHS1_BCU_AVHSts_Invalid = False
      if self.FIM_CHS1_BCU_VehSpdSts_ASILD_Invalid is None:
        self.FIM_CHS1_BCU_VehSpdSts_ASILD_Invalid = False
      if self.FIM_CHS1_BCU_ABSFailLampReq_LampOn is None:
        self.FIM_CHS1_BCU_ABSFailLampReq_LampOn = False
      if self.FIM_CHS1_VDCTCSFailLampReq is None:
        self.FIM_CHS1_VDCTCSFailLampReq = False
      if self.FIM_CHS1_AutoBrkgAvl_Invalid is None:
        self.FIM_CHS1_AutoBrkgAvl_Invalid = False
      if self.FIM_CHS1_AWBAvl_Invalid is None:
        self.FIM_CHS1_AWBAvl_Invalid = False
      if self.FIM_CHS1_BrkOverHeat is None:
        self.FIM_CHS1_BrkOverHeat = False
      if self.FIM_CHS1_ABAAvl_NotAvailable is None:
        self.FIM_CHS1_ABAAvl_NotAvailable = False
      if self.FIM_CHS1_ABPAvl_NotAvailable is None:
        self.FIM_CHS1_ABPAvl_NotAvailable = False
    else:
      self.FIM_CHS1_BCU_WhlSpdMovgDir_Invalid = False
      self.FIM_CHS1_BCU_WhlSpdSts_invalid = False
      self.FIM_CHS1_BCU_WhlPlsCntr_Invalid = False
      self.FIM_CHS1_BCU_VehSpdSts_Invalid = False
      self.FIM_CHS1_BCU_BrkPressValid_Invalid = False
      self.FIM_CHS1_BCU_BrkPedlSts_Invalid = False
      self.FIM_CHS1_BCU_VehMovgDir_Invalid = False
      self.FIM_CHS1_BCU_BrkPressOffsetValid_Invalid = False
      self.FIM_CHS1_BCU_HDCSts_Invalid = False
      self.FIM_CHS1_BCU_AVHSts_Invalid = False
      self.FIM_CHS1_BCU_VehSpdSts_ASILD_Invalid = False
      self.FIM_CHS1_BCU_ABSFailLampReq_LampOn = False
      self.FIM_CHS1_VDCTCSFailLampReq = False
      self.FIM_CHS1_AutoBrkgAvl_Invalid = False
      self.FIM_CHS1_AWBAvl_Invalid = False
      self.FIM_CHS1_BrkOverHeat = False
      self.FIM_CHS1_ABAAvl_NotAvailable = False
      self.FIM_CHS1_ABPAvl_NotAvailable = False

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
      buff.write(_get_struct_18B().pack(_x.FIM_CHS1_BCU_WhlSpdMovgDir_Invalid, _x.FIM_CHS1_BCU_WhlSpdSts_invalid, _x.FIM_CHS1_BCU_WhlPlsCntr_Invalid, _x.FIM_CHS1_BCU_VehSpdSts_Invalid, _x.FIM_CHS1_BCU_BrkPressValid_Invalid, _x.FIM_CHS1_BCU_BrkPedlSts_Invalid, _x.FIM_CHS1_BCU_VehMovgDir_Invalid, _x.FIM_CHS1_BCU_BrkPressOffsetValid_Invalid, _x.FIM_CHS1_BCU_HDCSts_Invalid, _x.FIM_CHS1_BCU_AVHSts_Invalid, _x.FIM_CHS1_BCU_VehSpdSts_ASILD_Invalid, _x.FIM_CHS1_BCU_ABSFailLampReq_LampOn, _x.FIM_CHS1_VDCTCSFailLampReq, _x.FIM_CHS1_AutoBrkgAvl_Invalid, _x.FIM_CHS1_AWBAvl_Invalid, _x.FIM_CHS1_BrkOverHeat, _x.FIM_CHS1_ABAAvl_NotAvailable, _x.FIM_CHS1_ABPAvl_NotAvailable))
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
      end += 18
      (_x.FIM_CHS1_BCU_WhlSpdMovgDir_Invalid, _x.FIM_CHS1_BCU_WhlSpdSts_invalid, _x.FIM_CHS1_BCU_WhlPlsCntr_Invalid, _x.FIM_CHS1_BCU_VehSpdSts_Invalid, _x.FIM_CHS1_BCU_BrkPressValid_Invalid, _x.FIM_CHS1_BCU_BrkPedlSts_Invalid, _x.FIM_CHS1_BCU_VehMovgDir_Invalid, _x.FIM_CHS1_BCU_BrkPressOffsetValid_Invalid, _x.FIM_CHS1_BCU_HDCSts_Invalid, _x.FIM_CHS1_BCU_AVHSts_Invalid, _x.FIM_CHS1_BCU_VehSpdSts_ASILD_Invalid, _x.FIM_CHS1_BCU_ABSFailLampReq_LampOn, _x.FIM_CHS1_VDCTCSFailLampReq, _x.FIM_CHS1_AutoBrkgAvl_Invalid, _x.FIM_CHS1_AWBAvl_Invalid, _x.FIM_CHS1_BrkOverHeat, _x.FIM_CHS1_ABAAvl_NotAvailable, _x.FIM_CHS1_ABPAvl_NotAvailable,) = _get_struct_18B().unpack(str[start:end])
      self.FIM_CHS1_BCU_WhlSpdMovgDir_Invalid = bool(self.FIM_CHS1_BCU_WhlSpdMovgDir_Invalid)
      self.FIM_CHS1_BCU_WhlSpdSts_invalid = bool(self.FIM_CHS1_BCU_WhlSpdSts_invalid)
      self.FIM_CHS1_BCU_WhlPlsCntr_Invalid = bool(self.FIM_CHS1_BCU_WhlPlsCntr_Invalid)
      self.FIM_CHS1_BCU_VehSpdSts_Invalid = bool(self.FIM_CHS1_BCU_VehSpdSts_Invalid)
      self.FIM_CHS1_BCU_BrkPressValid_Invalid = bool(self.FIM_CHS1_BCU_BrkPressValid_Invalid)
      self.FIM_CHS1_BCU_BrkPedlSts_Invalid = bool(self.FIM_CHS1_BCU_BrkPedlSts_Invalid)
      self.FIM_CHS1_BCU_VehMovgDir_Invalid = bool(self.FIM_CHS1_BCU_VehMovgDir_Invalid)
      self.FIM_CHS1_BCU_BrkPressOffsetValid_Invalid = bool(self.FIM_CHS1_BCU_BrkPressOffsetValid_Invalid)
      self.FIM_CHS1_BCU_HDCSts_Invalid = bool(self.FIM_CHS1_BCU_HDCSts_Invalid)
      self.FIM_CHS1_BCU_AVHSts_Invalid = bool(self.FIM_CHS1_BCU_AVHSts_Invalid)
      self.FIM_CHS1_BCU_VehSpdSts_ASILD_Invalid = bool(self.FIM_CHS1_BCU_VehSpdSts_ASILD_Invalid)
      self.FIM_CHS1_BCU_ABSFailLampReq_LampOn = bool(self.FIM_CHS1_BCU_ABSFailLampReq_LampOn)
      self.FIM_CHS1_VDCTCSFailLampReq = bool(self.FIM_CHS1_VDCTCSFailLampReq)
      self.FIM_CHS1_AutoBrkgAvl_Invalid = bool(self.FIM_CHS1_AutoBrkgAvl_Invalid)
      self.FIM_CHS1_AWBAvl_Invalid = bool(self.FIM_CHS1_AWBAvl_Invalid)
      self.FIM_CHS1_BrkOverHeat = bool(self.FIM_CHS1_BrkOverHeat)
      self.FIM_CHS1_ABAAvl_NotAvailable = bool(self.FIM_CHS1_ABAAvl_NotAvailable)
      self.FIM_CHS1_ABPAvl_NotAvailable = bool(self.FIM_CHS1_ABPAvl_NotAvailable)
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
      buff.write(_get_struct_18B().pack(_x.FIM_CHS1_BCU_WhlSpdMovgDir_Invalid, _x.FIM_CHS1_BCU_WhlSpdSts_invalid, _x.FIM_CHS1_BCU_WhlPlsCntr_Invalid, _x.FIM_CHS1_BCU_VehSpdSts_Invalid, _x.FIM_CHS1_BCU_BrkPressValid_Invalid, _x.FIM_CHS1_BCU_BrkPedlSts_Invalid, _x.FIM_CHS1_BCU_VehMovgDir_Invalid, _x.FIM_CHS1_BCU_BrkPressOffsetValid_Invalid, _x.FIM_CHS1_BCU_HDCSts_Invalid, _x.FIM_CHS1_BCU_AVHSts_Invalid, _x.FIM_CHS1_BCU_VehSpdSts_ASILD_Invalid, _x.FIM_CHS1_BCU_ABSFailLampReq_LampOn, _x.FIM_CHS1_VDCTCSFailLampReq, _x.FIM_CHS1_AutoBrkgAvl_Invalid, _x.FIM_CHS1_AWBAvl_Invalid, _x.FIM_CHS1_BrkOverHeat, _x.FIM_CHS1_ABAAvl_NotAvailable, _x.FIM_CHS1_ABPAvl_NotAvailable))
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
      end += 18
      (_x.FIM_CHS1_BCU_WhlSpdMovgDir_Invalid, _x.FIM_CHS1_BCU_WhlSpdSts_invalid, _x.FIM_CHS1_BCU_WhlPlsCntr_Invalid, _x.FIM_CHS1_BCU_VehSpdSts_Invalid, _x.FIM_CHS1_BCU_BrkPressValid_Invalid, _x.FIM_CHS1_BCU_BrkPedlSts_Invalid, _x.FIM_CHS1_BCU_VehMovgDir_Invalid, _x.FIM_CHS1_BCU_BrkPressOffsetValid_Invalid, _x.FIM_CHS1_BCU_HDCSts_Invalid, _x.FIM_CHS1_BCU_AVHSts_Invalid, _x.FIM_CHS1_BCU_VehSpdSts_ASILD_Invalid, _x.FIM_CHS1_BCU_ABSFailLampReq_LampOn, _x.FIM_CHS1_VDCTCSFailLampReq, _x.FIM_CHS1_AutoBrkgAvl_Invalid, _x.FIM_CHS1_AWBAvl_Invalid, _x.FIM_CHS1_BrkOverHeat, _x.FIM_CHS1_ABAAvl_NotAvailable, _x.FIM_CHS1_ABPAvl_NotAvailable,) = _get_struct_18B().unpack(str[start:end])
      self.FIM_CHS1_BCU_WhlSpdMovgDir_Invalid = bool(self.FIM_CHS1_BCU_WhlSpdMovgDir_Invalid)
      self.FIM_CHS1_BCU_WhlSpdSts_invalid = bool(self.FIM_CHS1_BCU_WhlSpdSts_invalid)
      self.FIM_CHS1_BCU_WhlPlsCntr_Invalid = bool(self.FIM_CHS1_BCU_WhlPlsCntr_Invalid)
      self.FIM_CHS1_BCU_VehSpdSts_Invalid = bool(self.FIM_CHS1_BCU_VehSpdSts_Invalid)
      self.FIM_CHS1_BCU_BrkPressValid_Invalid = bool(self.FIM_CHS1_BCU_BrkPressValid_Invalid)
      self.FIM_CHS1_BCU_BrkPedlSts_Invalid = bool(self.FIM_CHS1_BCU_BrkPedlSts_Invalid)
      self.FIM_CHS1_BCU_VehMovgDir_Invalid = bool(self.FIM_CHS1_BCU_VehMovgDir_Invalid)
      self.FIM_CHS1_BCU_BrkPressOffsetValid_Invalid = bool(self.FIM_CHS1_BCU_BrkPressOffsetValid_Invalid)
      self.FIM_CHS1_BCU_HDCSts_Invalid = bool(self.FIM_CHS1_BCU_HDCSts_Invalid)
      self.FIM_CHS1_BCU_AVHSts_Invalid = bool(self.FIM_CHS1_BCU_AVHSts_Invalid)
      self.FIM_CHS1_BCU_VehSpdSts_ASILD_Invalid = bool(self.FIM_CHS1_BCU_VehSpdSts_ASILD_Invalid)
      self.FIM_CHS1_BCU_ABSFailLampReq_LampOn = bool(self.FIM_CHS1_BCU_ABSFailLampReq_LampOn)
      self.FIM_CHS1_VDCTCSFailLampReq = bool(self.FIM_CHS1_VDCTCSFailLampReq)
      self.FIM_CHS1_AutoBrkgAvl_Invalid = bool(self.FIM_CHS1_AutoBrkgAvl_Invalid)
      self.FIM_CHS1_AWBAvl_Invalid = bool(self.FIM_CHS1_AWBAvl_Invalid)
      self.FIM_CHS1_BrkOverHeat = bool(self.FIM_CHS1_BrkOverHeat)
      self.FIM_CHS1_ABAAvl_NotAvailable = bool(self.FIM_CHS1_ABAAvl_NotAvailable)
      self.FIM_CHS1_ABPAvl_NotAvailable = bool(self.FIM_CHS1_ABPAvl_NotAvailable)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_18B = None
def _get_struct_18B():
    global _struct_18B
    if _struct_18B is None:
        _struct_18B = struct.Struct("<18B")
    return _struct_18B

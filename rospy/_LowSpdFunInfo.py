# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from rospy_message_converter/LowSpdFunInfo.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import rospy_message_converter.msg

class LowSpdFunInfo(genpy.Message):
  _md5sum = "5615e566fe723c03a81eda9eb6a8261a"
  _type = "rospy_message_converter/LowSpdFunInfo"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """ParkStInfo ParkSt
SummonStInfo SummonSt

================================================================================
MSG: rospy_message_converter/ParkStInfo
int32 PrkgTypSts
int32 SAPAOpMode
int32 SApaStatus
int32 APAReq
uint32 APASlotTrackID
int32 SVCReq
int32 SApaDrivingDir
int32[] SApaPscSlot
int32[] SApaPocSLot
int32 SApaInstruction
uint32 SApaStopDstDisp
int32 SVCEDRReq
uint32 SApaAbortReason
uint32 SAPATextInfo
int32 PSAPOutInstruction
int32 PSAPInstruction
int32 PsapTextInfo
int32 PSAPAbortReason
int32 PSAPHMIStatus
int32 PSAPDrivingDir
uint32 PSAPStopDstDisp
int32 PSAPOutHMIStatus
uint32 SApaProgress
int32 PrkgActvFeatureTyp

================================================================================
MSG: rospy_message_converter/SummonStInfo
uint32 NBSInstruction
int32 NBSBlkage
uint32 NBSAbortReason
bool NBSBlkageFrntLe
bool NBSBlkageFrntRi
bool NBSBlkageReLe
bool NBSBlkageReRi
int32[] RpsDir_Avail
uint32 RpsTextInfo
int32 RpsSlotSts
uint32 RpsProgress
bool RpsStandstillReq
int32 RpsSts
int32 RpsLockUnlckCtrl
int32 RpsInstruction
uint32 RpsAbortReason
"""
  __slots__ = ['ParkSt','SummonSt']
  _slot_types = ['rospy_message_converter/ParkStInfo','rospy_message_converter/SummonStInfo']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       ParkSt,SummonSt

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(LowSpdFunInfo, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.ParkSt is None:
        self.ParkSt = rospy_message_converter.msg.ParkStInfo()
      if self.SummonSt is None:
        self.SummonSt = rospy_message_converter.msg.SummonStInfo()
    else:
      self.ParkSt = rospy_message_converter.msg.ParkStInfo()
      self.SummonSt = rospy_message_converter.msg.SummonStInfo()

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
      buff.write(_get_struct_4iI2i().pack(_x.ParkSt.PrkgTypSts, _x.ParkSt.SAPAOpMode, _x.ParkSt.SApaStatus, _x.ParkSt.APAReq, _x.ParkSt.APASlotTrackID, _x.ParkSt.SVCReq, _x.ParkSt.SApaDrivingDir))
      length = len(self.ParkSt.SApaPscSlot)
      buff.write(_struct_I.pack(length))
      pattern = '<%si'%length
      buff.write(struct.Struct(pattern).pack(*self.ParkSt.SApaPscSlot))
      length = len(self.ParkSt.SApaPocSLot)
      buff.write(_struct_I.pack(length))
      pattern = '<%si'%length
      buff.write(struct.Struct(pattern).pack(*self.ParkSt.SApaPocSLot))
      _x = self
      buff.write(_get_struct_iIi2I6iIiIiIiI4B().pack(_x.ParkSt.SApaInstruction, _x.ParkSt.SApaStopDstDisp, _x.ParkSt.SVCEDRReq, _x.ParkSt.SApaAbortReason, _x.ParkSt.SAPATextInfo, _x.ParkSt.PSAPOutInstruction, _x.ParkSt.PSAPInstruction, _x.ParkSt.PsapTextInfo, _x.ParkSt.PSAPAbortReason, _x.ParkSt.PSAPHMIStatus, _x.ParkSt.PSAPDrivingDir, _x.ParkSt.PSAPStopDstDisp, _x.ParkSt.PSAPOutHMIStatus, _x.ParkSt.SApaProgress, _x.ParkSt.PrkgActvFeatureTyp, _x.SummonSt.NBSInstruction, _x.SummonSt.NBSBlkage, _x.SummonSt.NBSAbortReason, _x.SummonSt.NBSBlkageFrntLe, _x.SummonSt.NBSBlkageFrntRi, _x.SummonSt.NBSBlkageReLe, _x.SummonSt.NBSBlkageReRi))
      length = len(self.SummonSt.RpsDir_Avail)
      buff.write(_struct_I.pack(length))
      pattern = '<%si'%length
      buff.write(struct.Struct(pattern).pack(*self.SummonSt.RpsDir_Avail))
      _x = self
      buff.write(_get_struct_IiIB3iI().pack(_x.SummonSt.RpsTextInfo, _x.SummonSt.RpsSlotSts, _x.SummonSt.RpsProgress, _x.SummonSt.RpsStandstillReq, _x.SummonSt.RpsSts, _x.SummonSt.RpsLockUnlckCtrl, _x.SummonSt.RpsInstruction, _x.SummonSt.RpsAbortReason))
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
      if self.ParkSt is None:
        self.ParkSt = rospy_message_converter.msg.ParkStInfo()
      if self.SummonSt is None:
        self.SummonSt = rospy_message_converter.msg.SummonStInfo()
      end = 0
      _x = self
      start = end
      end += 28
      (_x.ParkSt.PrkgTypSts, _x.ParkSt.SAPAOpMode, _x.ParkSt.SApaStatus, _x.ParkSt.APAReq, _x.ParkSt.APASlotTrackID, _x.ParkSt.SVCReq, _x.ParkSt.SApaDrivingDir,) = _get_struct_4iI2i().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%si'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.ParkSt.SApaPscSlot = s.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%si'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.ParkSt.SApaPocSLot = s.unpack(str[start:end])
      _x = self
      start = end
      end += 76
      (_x.ParkSt.SApaInstruction, _x.ParkSt.SApaStopDstDisp, _x.ParkSt.SVCEDRReq, _x.ParkSt.SApaAbortReason, _x.ParkSt.SAPATextInfo, _x.ParkSt.PSAPOutInstruction, _x.ParkSt.PSAPInstruction, _x.ParkSt.PsapTextInfo, _x.ParkSt.PSAPAbortReason, _x.ParkSt.PSAPHMIStatus, _x.ParkSt.PSAPDrivingDir, _x.ParkSt.PSAPStopDstDisp, _x.ParkSt.PSAPOutHMIStatus, _x.ParkSt.SApaProgress, _x.ParkSt.PrkgActvFeatureTyp, _x.SummonSt.NBSInstruction, _x.SummonSt.NBSBlkage, _x.SummonSt.NBSAbortReason, _x.SummonSt.NBSBlkageFrntLe, _x.SummonSt.NBSBlkageFrntRi, _x.SummonSt.NBSBlkageReLe, _x.SummonSt.NBSBlkageReRi,) = _get_struct_iIi2I6iIiIiIiI4B().unpack(str[start:end])
      self.SummonSt.NBSBlkageFrntLe = bool(self.SummonSt.NBSBlkageFrntLe)
      self.SummonSt.NBSBlkageFrntRi = bool(self.SummonSt.NBSBlkageFrntRi)
      self.SummonSt.NBSBlkageReLe = bool(self.SummonSt.NBSBlkageReLe)
      self.SummonSt.NBSBlkageReRi = bool(self.SummonSt.NBSBlkageReRi)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%si'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.SummonSt.RpsDir_Avail = s.unpack(str[start:end])
      _x = self
      start = end
      end += 29
      (_x.SummonSt.RpsTextInfo, _x.SummonSt.RpsSlotSts, _x.SummonSt.RpsProgress, _x.SummonSt.RpsStandstillReq, _x.SummonSt.RpsSts, _x.SummonSt.RpsLockUnlckCtrl, _x.SummonSt.RpsInstruction, _x.SummonSt.RpsAbortReason,) = _get_struct_IiIB3iI().unpack(str[start:end])
      self.SummonSt.RpsStandstillReq = bool(self.SummonSt.RpsStandstillReq)
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
      buff.write(_get_struct_4iI2i().pack(_x.ParkSt.PrkgTypSts, _x.ParkSt.SAPAOpMode, _x.ParkSt.SApaStatus, _x.ParkSt.APAReq, _x.ParkSt.APASlotTrackID, _x.ParkSt.SVCReq, _x.ParkSt.SApaDrivingDir))
      length = len(self.ParkSt.SApaPscSlot)
      buff.write(_struct_I.pack(length))
      pattern = '<%si'%length
      buff.write(self.ParkSt.SApaPscSlot.tostring())
      length = len(self.ParkSt.SApaPocSLot)
      buff.write(_struct_I.pack(length))
      pattern = '<%si'%length
      buff.write(self.ParkSt.SApaPocSLot.tostring())
      _x = self
      buff.write(_get_struct_iIi2I6iIiIiIiI4B().pack(_x.ParkSt.SApaInstruction, _x.ParkSt.SApaStopDstDisp, _x.ParkSt.SVCEDRReq, _x.ParkSt.SApaAbortReason, _x.ParkSt.SAPATextInfo, _x.ParkSt.PSAPOutInstruction, _x.ParkSt.PSAPInstruction, _x.ParkSt.PsapTextInfo, _x.ParkSt.PSAPAbortReason, _x.ParkSt.PSAPHMIStatus, _x.ParkSt.PSAPDrivingDir, _x.ParkSt.PSAPStopDstDisp, _x.ParkSt.PSAPOutHMIStatus, _x.ParkSt.SApaProgress, _x.ParkSt.PrkgActvFeatureTyp, _x.SummonSt.NBSInstruction, _x.SummonSt.NBSBlkage, _x.SummonSt.NBSAbortReason, _x.SummonSt.NBSBlkageFrntLe, _x.SummonSt.NBSBlkageFrntRi, _x.SummonSt.NBSBlkageReLe, _x.SummonSt.NBSBlkageReRi))
      length = len(self.SummonSt.RpsDir_Avail)
      buff.write(_struct_I.pack(length))
      pattern = '<%si'%length
      buff.write(self.SummonSt.RpsDir_Avail.tostring())
      _x = self
      buff.write(_get_struct_IiIB3iI().pack(_x.SummonSt.RpsTextInfo, _x.SummonSt.RpsSlotSts, _x.SummonSt.RpsProgress, _x.SummonSt.RpsStandstillReq, _x.SummonSt.RpsSts, _x.SummonSt.RpsLockUnlckCtrl, _x.SummonSt.RpsInstruction, _x.SummonSt.RpsAbortReason))
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
      if self.ParkSt is None:
        self.ParkSt = rospy_message_converter.msg.ParkStInfo()
      if self.SummonSt is None:
        self.SummonSt = rospy_message_converter.msg.SummonStInfo()
      end = 0
      _x = self
      start = end
      end += 28
      (_x.ParkSt.PrkgTypSts, _x.ParkSt.SAPAOpMode, _x.ParkSt.SApaStatus, _x.ParkSt.APAReq, _x.ParkSt.APASlotTrackID, _x.ParkSt.SVCReq, _x.ParkSt.SApaDrivingDir,) = _get_struct_4iI2i().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%si'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.ParkSt.SApaPscSlot = numpy.frombuffer(str[start:end], dtype=numpy.int32, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%si'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.ParkSt.SApaPocSLot = numpy.frombuffer(str[start:end], dtype=numpy.int32, count=length)
      _x = self
      start = end
      end += 76
      (_x.ParkSt.SApaInstruction, _x.ParkSt.SApaStopDstDisp, _x.ParkSt.SVCEDRReq, _x.ParkSt.SApaAbortReason, _x.ParkSt.SAPATextInfo, _x.ParkSt.PSAPOutInstruction, _x.ParkSt.PSAPInstruction, _x.ParkSt.PsapTextInfo, _x.ParkSt.PSAPAbortReason, _x.ParkSt.PSAPHMIStatus, _x.ParkSt.PSAPDrivingDir, _x.ParkSt.PSAPStopDstDisp, _x.ParkSt.PSAPOutHMIStatus, _x.ParkSt.SApaProgress, _x.ParkSt.PrkgActvFeatureTyp, _x.SummonSt.NBSInstruction, _x.SummonSt.NBSBlkage, _x.SummonSt.NBSAbortReason, _x.SummonSt.NBSBlkageFrntLe, _x.SummonSt.NBSBlkageFrntRi, _x.SummonSt.NBSBlkageReLe, _x.SummonSt.NBSBlkageReRi,) = _get_struct_iIi2I6iIiIiIiI4B().unpack(str[start:end])
      self.SummonSt.NBSBlkageFrntLe = bool(self.SummonSt.NBSBlkageFrntLe)
      self.SummonSt.NBSBlkageFrntRi = bool(self.SummonSt.NBSBlkageFrntRi)
      self.SummonSt.NBSBlkageReLe = bool(self.SummonSt.NBSBlkageReLe)
      self.SummonSt.NBSBlkageReRi = bool(self.SummonSt.NBSBlkageReRi)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%si'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.SummonSt.RpsDir_Avail = numpy.frombuffer(str[start:end], dtype=numpy.int32, count=length)
      _x = self
      start = end
      end += 29
      (_x.SummonSt.RpsTextInfo, _x.SummonSt.RpsSlotSts, _x.SummonSt.RpsProgress, _x.SummonSt.RpsStandstillReq, _x.SummonSt.RpsSts, _x.SummonSt.RpsLockUnlckCtrl, _x.SummonSt.RpsInstruction, _x.SummonSt.RpsAbortReason,) = _get_struct_IiIB3iI().unpack(str[start:end])
      self.SummonSt.RpsStandstillReq = bool(self.SummonSt.RpsStandstillReq)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_4iI2i = None
def _get_struct_4iI2i():
    global _struct_4iI2i
    if _struct_4iI2i is None:
        _struct_4iI2i = struct.Struct("<4iI2i")
    return _struct_4iI2i
_struct_IiIB3iI = None
def _get_struct_IiIB3iI():
    global _struct_IiIB3iI
    if _struct_IiIB3iI is None:
        _struct_IiIB3iI = struct.Struct("<IiIB3iI")
    return _struct_IiIB3iI
_struct_iIi2I6iIiIiIiI4B = None
def _get_struct_iIi2I6iIiIiIiI4B():
    global _struct_iIi2I6iIiIiIiI4B
    if _struct_iIi2I6iIiIiIiI4B is None:
        _struct_iIi2I6iIiIiIiI4B = struct.Struct("<iIi2I6iIiIiIiI4B")
    return _struct_iIi2I6iIiIiIiI4B

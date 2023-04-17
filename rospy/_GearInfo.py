# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from rospy_message_converter/GearInfo.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class GearInfo(genpy.Message):
  _md5sum = "9e8e21c340be635212e25495a576750f"
  _type = "rospy_message_converter/GearInfo"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """int32 SlctrPosnVld
int32 ActGearVld
int32 TrgtGearVld
int32 SlctrPosn
int32 ActGear
int32 TrgtGear
uint64 timestamp_ptp_ns
"""
  __slots__ = ['SlctrPosnVld','ActGearVld','TrgtGearVld','SlctrPosn','ActGear','TrgtGear','timestamp_ptp_ns']
  _slot_types = ['int32','int32','int32','int32','int32','int32','uint64']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       SlctrPosnVld,ActGearVld,TrgtGearVld,SlctrPosn,ActGear,TrgtGear,timestamp_ptp_ns

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(GearInfo, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.SlctrPosnVld is None:
        self.SlctrPosnVld = 0
      if self.ActGearVld is None:
        self.ActGearVld = 0
      if self.TrgtGearVld is None:
        self.TrgtGearVld = 0
      if self.SlctrPosn is None:
        self.SlctrPosn = 0
      if self.ActGear is None:
        self.ActGear = 0
      if self.TrgtGear is None:
        self.TrgtGear = 0
      if self.timestamp_ptp_ns is None:
        self.timestamp_ptp_ns = 0
    else:
      self.SlctrPosnVld = 0
      self.ActGearVld = 0
      self.TrgtGearVld = 0
      self.SlctrPosn = 0
      self.ActGear = 0
      self.TrgtGear = 0
      self.timestamp_ptp_ns = 0

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
      buff.write(_get_struct_6iQ().pack(_x.SlctrPosnVld, _x.ActGearVld, _x.TrgtGearVld, _x.SlctrPosn, _x.ActGear, _x.TrgtGear, _x.timestamp_ptp_ns))
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
      end += 32
      (_x.SlctrPosnVld, _x.ActGearVld, _x.TrgtGearVld, _x.SlctrPosn, _x.ActGear, _x.TrgtGear, _x.timestamp_ptp_ns,) = _get_struct_6iQ().unpack(str[start:end])
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
      buff.write(_get_struct_6iQ().pack(_x.SlctrPosnVld, _x.ActGearVld, _x.TrgtGearVld, _x.SlctrPosn, _x.ActGear, _x.TrgtGear, _x.timestamp_ptp_ns))
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
      end += 32
      (_x.SlctrPosnVld, _x.ActGearVld, _x.TrgtGearVld, _x.SlctrPosn, _x.ActGear, _x.TrgtGear, _x.timestamp_ptp_ns,) = _get_struct_6iQ().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_6iQ = None
def _get_struct_6iQ():
    global _struct_6iQ
    if _struct_6iQ is None:
        _struct_6iQ = struct.Struct("<6iQ")
    return _struct_6iQ

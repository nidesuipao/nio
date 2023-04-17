# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from rospy_message_converter/NopVehicleOut.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class NopVehicleOut(genpy.Message):
  _md5sum = "05560c3e403d2b2a895271906706b03d"
  _type = "rospy_message_converter/NopVehicleOut"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """uint32 nop_alc_sts
uint32 nop_colllision_risk
bool nop_freeSpace_intrusion_at_standstill
bool nop_freeSpace_intrusion_go_notifier
uint32 nop_lat_ctrl_tarLe
uint32 nop_lat_ctrl_tarRi
uint32 nop_long_ctrl_tar
uint32 nop_turn_indicator_req
uint32 nop_wti
float32[] reserved
uint64 publish_ptp_ts
string publisher_id
uint64 counter
uint64 publish_ts
"""
  __slots__ = ['nop_alc_sts','nop_colllision_risk','nop_freeSpace_intrusion_at_standstill','nop_freeSpace_intrusion_go_notifier','nop_lat_ctrl_tarLe','nop_lat_ctrl_tarRi','nop_long_ctrl_tar','nop_turn_indicator_req','nop_wti','reserved','publish_ptp_ts','publisher_id','counter','publish_ts']
  _slot_types = ['uint32','uint32','bool','bool','uint32','uint32','uint32','uint32','uint32','float32[]','uint64','string','uint64','uint64']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       nop_alc_sts,nop_colllision_risk,nop_freeSpace_intrusion_at_standstill,nop_freeSpace_intrusion_go_notifier,nop_lat_ctrl_tarLe,nop_lat_ctrl_tarRi,nop_long_ctrl_tar,nop_turn_indicator_req,nop_wti,reserved,publish_ptp_ts,publisher_id,counter,publish_ts

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(NopVehicleOut, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.nop_alc_sts is None:
        self.nop_alc_sts = 0
      if self.nop_colllision_risk is None:
        self.nop_colllision_risk = 0
      if self.nop_freeSpace_intrusion_at_standstill is None:
        self.nop_freeSpace_intrusion_at_standstill = False
      if self.nop_freeSpace_intrusion_go_notifier is None:
        self.nop_freeSpace_intrusion_go_notifier = False
      if self.nop_lat_ctrl_tarLe is None:
        self.nop_lat_ctrl_tarLe = 0
      if self.nop_lat_ctrl_tarRi is None:
        self.nop_lat_ctrl_tarRi = 0
      if self.nop_long_ctrl_tar is None:
        self.nop_long_ctrl_tar = 0
      if self.nop_turn_indicator_req is None:
        self.nop_turn_indicator_req = 0
      if self.nop_wti is None:
        self.nop_wti = 0
      if self.reserved is None:
        self.reserved = []
      if self.publish_ptp_ts is None:
        self.publish_ptp_ts = 0
      if self.publisher_id is None:
        self.publisher_id = ''
      if self.counter is None:
        self.counter = 0
      if self.publish_ts is None:
        self.publish_ts = 0
    else:
      self.nop_alc_sts = 0
      self.nop_colllision_risk = 0
      self.nop_freeSpace_intrusion_at_standstill = False
      self.nop_freeSpace_intrusion_go_notifier = False
      self.nop_lat_ctrl_tarLe = 0
      self.nop_lat_ctrl_tarRi = 0
      self.nop_long_ctrl_tar = 0
      self.nop_turn_indicator_req = 0
      self.nop_wti = 0
      self.reserved = []
      self.publish_ptp_ts = 0
      self.publisher_id = ''
      self.counter = 0
      self.publish_ts = 0

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
      buff.write(_get_struct_2I2B5I().pack(_x.nop_alc_sts, _x.nop_colllision_risk, _x.nop_freeSpace_intrusion_at_standstill, _x.nop_freeSpace_intrusion_go_notifier, _x.nop_lat_ctrl_tarLe, _x.nop_lat_ctrl_tarRi, _x.nop_long_ctrl_tar, _x.nop_turn_indicator_req, _x.nop_wti))
      length = len(self.reserved)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(struct.Struct(pattern).pack(*self.reserved))
      _x = self.publish_ptp_ts
      buff.write(_get_struct_Q().pack(_x))
      _x = self.publisher_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_2Q().pack(_x.counter, _x.publish_ts))
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
      end += 30
      (_x.nop_alc_sts, _x.nop_colllision_risk, _x.nop_freeSpace_intrusion_at_standstill, _x.nop_freeSpace_intrusion_go_notifier, _x.nop_lat_ctrl_tarLe, _x.nop_lat_ctrl_tarRi, _x.nop_long_ctrl_tar, _x.nop_turn_indicator_req, _x.nop_wti,) = _get_struct_2I2B5I().unpack(str[start:end])
      self.nop_freeSpace_intrusion_at_standstill = bool(self.nop_freeSpace_intrusion_at_standstill)
      self.nop_freeSpace_intrusion_go_notifier = bool(self.nop_freeSpace_intrusion_go_notifier)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sf'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.reserved = s.unpack(str[start:end])
      start = end
      end += 8
      (self.publish_ptp_ts,) = _get_struct_Q().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.publisher_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.publisher_id = str[start:end]
      _x = self
      start = end
      end += 16
      (_x.counter, _x.publish_ts,) = _get_struct_2Q().unpack(str[start:end])
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
      buff.write(_get_struct_2I2B5I().pack(_x.nop_alc_sts, _x.nop_colllision_risk, _x.nop_freeSpace_intrusion_at_standstill, _x.nop_freeSpace_intrusion_go_notifier, _x.nop_lat_ctrl_tarLe, _x.nop_lat_ctrl_tarRi, _x.nop_long_ctrl_tar, _x.nop_turn_indicator_req, _x.nop_wti))
      length = len(self.reserved)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(self.reserved.tostring())
      _x = self.publish_ptp_ts
      buff.write(_get_struct_Q().pack(_x))
      _x = self.publisher_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_2Q().pack(_x.counter, _x.publish_ts))
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
      end += 30
      (_x.nop_alc_sts, _x.nop_colllision_risk, _x.nop_freeSpace_intrusion_at_standstill, _x.nop_freeSpace_intrusion_go_notifier, _x.nop_lat_ctrl_tarLe, _x.nop_lat_ctrl_tarRi, _x.nop_long_ctrl_tar, _x.nop_turn_indicator_req, _x.nop_wti,) = _get_struct_2I2B5I().unpack(str[start:end])
      self.nop_freeSpace_intrusion_at_standstill = bool(self.nop_freeSpace_intrusion_at_standstill)
      self.nop_freeSpace_intrusion_go_notifier = bool(self.nop_freeSpace_intrusion_go_notifier)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sf'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.reserved = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=length)
      start = end
      end += 8
      (self.publish_ptp_ts,) = _get_struct_Q().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.publisher_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.publisher_id = str[start:end]
      _x = self
      start = end
      end += 16
      (_x.counter, _x.publish_ts,) = _get_struct_2Q().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_2I2B5I = None
def _get_struct_2I2B5I():
    global _struct_2I2B5I
    if _struct_2I2B5I is None:
        _struct_2I2B5I = struct.Struct("<2I2B5I")
    return _struct_2I2B5I
_struct_2Q = None
def _get_struct_2Q():
    global _struct_2Q
    if _struct_2Q is None:
        _struct_2Q = struct.Struct("<2Q")
    return _struct_2Q
_struct_Q = None
def _get_struct_Q():
    global _struct_Q
    if _struct_Q is None:
        _struct_Q = struct.Struct("<Q")
    return _struct_Q

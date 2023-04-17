# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from rospy_message_converter/Lidar_FailSafeDetection.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import rospy_message_converter.msg

class Lidar_FailSafeDetection(genpy.Message):
  _md5sum = "af07dc1694bef80bc74bd8c979ee69bf"
  _type = "rospy_message_converter/Lidar_FailSafeDetection"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """uint64 timestamp
Lidar_FailSafe failsafe
uint64 publish_ptp_ts
string publisher_id
uint64 counter
uint64 publish_ts

================================================================================
MSG: rospy_message_converter/Lidar_FailSafe
uint32 FS_Window_Blockage
uint32 FS_Dust
uint32 FS_Wet_Road
uint32 FS_Rain_Snow
uint32 FS_Intrinsic_Calibration
uint32 FS_HW
uint32 FS_Out_Of_Calibration
"""
  __slots__ = ['timestamp','failsafe','publish_ptp_ts','publisher_id','counter','publish_ts']
  _slot_types = ['uint64','rospy_message_converter/Lidar_FailSafe','uint64','string','uint64','uint64']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       timestamp,failsafe,publish_ptp_ts,publisher_id,counter,publish_ts

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(Lidar_FailSafeDetection, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.timestamp is None:
        self.timestamp = 0
      if self.failsafe is None:
        self.failsafe = rospy_message_converter.msg.Lidar_FailSafe()
      if self.publish_ptp_ts is None:
        self.publish_ptp_ts = 0
      if self.publisher_id is None:
        self.publisher_id = ''
      if self.counter is None:
        self.counter = 0
      if self.publish_ts is None:
        self.publish_ts = 0
    else:
      self.timestamp = 0
      self.failsafe = rospy_message_converter.msg.Lidar_FailSafe()
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
      buff.write(_get_struct_Q7IQ().pack(_x.timestamp, _x.failsafe.FS_Window_Blockage, _x.failsafe.FS_Dust, _x.failsafe.FS_Wet_Road, _x.failsafe.FS_Rain_Snow, _x.failsafe.FS_Intrinsic_Calibration, _x.failsafe.FS_HW, _x.failsafe.FS_Out_Of_Calibration, _x.publish_ptp_ts))
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
      if self.failsafe is None:
        self.failsafe = rospy_message_converter.msg.Lidar_FailSafe()
      end = 0
      _x = self
      start = end
      end += 44
      (_x.timestamp, _x.failsafe.FS_Window_Blockage, _x.failsafe.FS_Dust, _x.failsafe.FS_Wet_Road, _x.failsafe.FS_Rain_Snow, _x.failsafe.FS_Intrinsic_Calibration, _x.failsafe.FS_HW, _x.failsafe.FS_Out_Of_Calibration, _x.publish_ptp_ts,) = _get_struct_Q7IQ().unpack(str[start:end])
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
      buff.write(_get_struct_Q7IQ().pack(_x.timestamp, _x.failsafe.FS_Window_Blockage, _x.failsafe.FS_Dust, _x.failsafe.FS_Wet_Road, _x.failsafe.FS_Rain_Snow, _x.failsafe.FS_Intrinsic_Calibration, _x.failsafe.FS_HW, _x.failsafe.FS_Out_Of_Calibration, _x.publish_ptp_ts))
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
      if self.failsafe is None:
        self.failsafe = rospy_message_converter.msg.Lidar_FailSafe()
      end = 0
      _x = self
      start = end
      end += 44
      (_x.timestamp, _x.failsafe.FS_Window_Blockage, _x.failsafe.FS_Dust, _x.failsafe.FS_Wet_Road, _x.failsafe.FS_Rain_Snow, _x.failsafe.FS_Intrinsic_Calibration, _x.failsafe.FS_HW, _x.failsafe.FS_Out_Of_Calibration, _x.publish_ptp_ts,) = _get_struct_Q7IQ().unpack(str[start:end])
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
_struct_2Q = None
def _get_struct_2Q():
    global _struct_2Q
    if _struct_2Q is None:
        _struct_2Q = struct.Struct("<2Q")
    return _struct_2Q
_struct_Q7IQ = None
def _get_struct_Q7IQ():
    global _struct_Q7IQ
    if _struct_Q7IQ is None:
        _struct_Q7IQ = struct.Struct("<Q7IQ")
    return _struct_Q7IQ

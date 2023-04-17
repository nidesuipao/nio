# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from rospy_message_converter/MCUCameraStatus.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class MCUCameraStatus(genpy.Message):
  _md5sum = "950987339c1a4b39644f879337045ecc"
  _type = "rospy_message_converter/MCUCameraStatus"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """int32 F120_sharing_link_Status
int32 mcu_svc_front_Status
int32 mcu_svc_rear_Status
int32 mcu_svc_left_Status
int32 mcu_svc_right_Status
uint64 publish_ptp_ts
string publisher_id
uint64 counter
uint64 publish_ts
"""
  __slots__ = ['F120_sharing_link_Status','mcu_svc_front_Status','mcu_svc_rear_Status','mcu_svc_left_Status','mcu_svc_right_Status','publish_ptp_ts','publisher_id','counter','publish_ts']
  _slot_types = ['int32','int32','int32','int32','int32','uint64','string','uint64','uint64']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       F120_sharing_link_Status,mcu_svc_front_Status,mcu_svc_rear_Status,mcu_svc_left_Status,mcu_svc_right_Status,publish_ptp_ts,publisher_id,counter,publish_ts

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(MCUCameraStatus, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.F120_sharing_link_Status is None:
        self.F120_sharing_link_Status = 0
      if self.mcu_svc_front_Status is None:
        self.mcu_svc_front_Status = 0
      if self.mcu_svc_rear_Status is None:
        self.mcu_svc_rear_Status = 0
      if self.mcu_svc_left_Status is None:
        self.mcu_svc_left_Status = 0
      if self.mcu_svc_right_Status is None:
        self.mcu_svc_right_Status = 0
      if self.publish_ptp_ts is None:
        self.publish_ptp_ts = 0
      if self.publisher_id is None:
        self.publisher_id = ''
      if self.counter is None:
        self.counter = 0
      if self.publish_ts is None:
        self.publish_ts = 0
    else:
      self.F120_sharing_link_Status = 0
      self.mcu_svc_front_Status = 0
      self.mcu_svc_rear_Status = 0
      self.mcu_svc_left_Status = 0
      self.mcu_svc_right_Status = 0
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
      buff.write(_get_struct_5iQ().pack(_x.F120_sharing_link_Status, _x.mcu_svc_front_Status, _x.mcu_svc_rear_Status, _x.mcu_svc_left_Status, _x.mcu_svc_right_Status, _x.publish_ptp_ts))
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
      end += 28
      (_x.F120_sharing_link_Status, _x.mcu_svc_front_Status, _x.mcu_svc_rear_Status, _x.mcu_svc_left_Status, _x.mcu_svc_right_Status, _x.publish_ptp_ts,) = _get_struct_5iQ().unpack(str[start:end])
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
      buff.write(_get_struct_5iQ().pack(_x.F120_sharing_link_Status, _x.mcu_svc_front_Status, _x.mcu_svc_rear_Status, _x.mcu_svc_left_Status, _x.mcu_svc_right_Status, _x.publish_ptp_ts))
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
      end += 28
      (_x.F120_sharing_link_Status, _x.mcu_svc_front_Status, _x.mcu_svc_rear_Status, _x.mcu_svc_left_Status, _x.mcu_svc_right_Status, _x.publish_ptp_ts,) = _get_struct_5iQ().unpack(str[start:end])
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
_struct_5iQ = None
def _get_struct_5iQ():
    global _struct_5iQ
    if _struct_5iQ is None:
        _struct_5iQ = struct.Struct("<5iQ")
    return _struct_5iQ

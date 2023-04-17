# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from rospy_message_converter/GNSSSwitchRequest.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class GNSSSwitchRequest(genpy.Message):
  _md5sum = "631f6209aedb1f614577ae0773f05f8d"
  _type = "rospy_message_converter/GNSSSwitchRequest"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """int32 swch_req_content
string vid
uint32 swch_req_user_id
uint32 swch_req_sequence
uint64 swch_req_timestamp
uint64 publish_ptp_ts
string publisher_id
uint64 counter
uint64 publish_ts
"""
  __slots__ = ['swch_req_content','vid','swch_req_user_id','swch_req_sequence','swch_req_timestamp','publish_ptp_ts','publisher_id','counter','publish_ts']
  _slot_types = ['int32','string','uint32','uint32','uint64','uint64','string','uint64','uint64']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       swch_req_content,vid,swch_req_user_id,swch_req_sequence,swch_req_timestamp,publish_ptp_ts,publisher_id,counter,publish_ts

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(GNSSSwitchRequest, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.swch_req_content is None:
        self.swch_req_content = 0
      if self.vid is None:
        self.vid = ''
      if self.swch_req_user_id is None:
        self.swch_req_user_id = 0
      if self.swch_req_sequence is None:
        self.swch_req_sequence = 0
      if self.swch_req_timestamp is None:
        self.swch_req_timestamp = 0
      if self.publish_ptp_ts is None:
        self.publish_ptp_ts = 0
      if self.publisher_id is None:
        self.publisher_id = ''
      if self.counter is None:
        self.counter = 0
      if self.publish_ts is None:
        self.publish_ts = 0
    else:
      self.swch_req_content = 0
      self.vid = ''
      self.swch_req_user_id = 0
      self.swch_req_sequence = 0
      self.swch_req_timestamp = 0
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
      _x = self.swch_req_content
      buff.write(_get_struct_i().pack(_x))
      _x = self.vid
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_2I2Q().pack(_x.swch_req_user_id, _x.swch_req_sequence, _x.swch_req_timestamp, _x.publish_ptp_ts))
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
      start = end
      end += 4
      (self.swch_req_content,) = _get_struct_i().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.vid = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.vid = str[start:end]
      _x = self
      start = end
      end += 24
      (_x.swch_req_user_id, _x.swch_req_sequence, _x.swch_req_timestamp, _x.publish_ptp_ts,) = _get_struct_2I2Q().unpack(str[start:end])
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
      _x = self.swch_req_content
      buff.write(_get_struct_i().pack(_x))
      _x = self.vid
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_2I2Q().pack(_x.swch_req_user_id, _x.swch_req_sequence, _x.swch_req_timestamp, _x.publish_ptp_ts))
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
      start = end
      end += 4
      (self.swch_req_content,) = _get_struct_i().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.vid = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.vid = str[start:end]
      _x = self
      start = end
      end += 24
      (_x.swch_req_user_id, _x.swch_req_sequence, _x.swch_req_timestamp, _x.publish_ptp_ts,) = _get_struct_2I2Q().unpack(str[start:end])
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
_struct_2I2Q = None
def _get_struct_2I2Q():
    global _struct_2I2Q
    if _struct_2I2Q is None:
        _struct_2I2Q = struct.Struct("<2I2Q")
    return _struct_2I2Q
_struct_2Q = None
def _get_struct_2Q():
    global _struct_2Q
    if _struct_2Q is None:
        _struct_2Q = struct.Struct("<2Q")
    return _struct_2Q
_struct_i = None
def _get_struct_i():
    global _struct_i
    if _struct_i is None:
        _struct_i = struct.Struct("<i")
    return _struct_i

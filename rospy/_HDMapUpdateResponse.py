# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from rospy_message_converter/HDMapUpdateResponse.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class HDMapUpdateResponse(genpy.Message):
  _md5sum = "fff21db197bc5100e6a8f87e88723433"
  _type = "rospy_message_converter/HDMapUpdateResponse"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """string uuid
int32 status
uint64 publish_ptp_ts
string publisher_id
uint64 counter
uint64 publish_ts
"""
  __slots__ = ['uuid','status','publish_ptp_ts','publisher_id','counter','publish_ts']
  _slot_types = ['string','int32','uint64','string','uint64','uint64']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       uuid,status,publish_ptp_ts,publisher_id,counter,publish_ts

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(HDMapUpdateResponse, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.uuid is None:
        self.uuid = ''
      if self.status is None:
        self.status = 0
      if self.publish_ptp_ts is None:
        self.publish_ptp_ts = 0
      if self.publisher_id is None:
        self.publisher_id = ''
      if self.counter is None:
        self.counter = 0
      if self.publish_ts is None:
        self.publish_ts = 0
    else:
      self.uuid = ''
      self.status = 0
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
      _x = self.uuid
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_iQ().pack(_x.status, _x.publish_ptp_ts))
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
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.uuid = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.uuid = str[start:end]
      _x = self
      start = end
      end += 12
      (_x.status, _x.publish_ptp_ts,) = _get_struct_iQ().unpack(str[start:end])
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
      _x = self.uuid
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_iQ().pack(_x.status, _x.publish_ptp_ts))
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
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.uuid = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.uuid = str[start:end]
      _x = self
      start = end
      end += 12
      (_x.status, _x.publish_ptp_ts,) = _get_struct_iQ().unpack(str[start:end])
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
_struct_iQ = None
def _get_struct_iQ():
    global _struct_iQ
    if _struct_iQ is None:
        _struct_iQ = struct.Struct("<iQ")
    return _struct_iQ

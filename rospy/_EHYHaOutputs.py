# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from rospy_message_converter/EHYHaOutputs.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class EHYHaOutputs(genpy.Message):
  _md5sum = "5f27bdcd992a4a34ab7e106e9937b5b2"
  _type = "rospy_message_converter/EHYHaOutputs"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """uint32 icon_info
int32 text_info
uint32 sound_info
uint32[] hmi_highlight_obj_id
bool left_lane_flash
bool right_lane_flash
uint64 publish_ptp_ts
string publisher_id
uint64 counter
uint64 publish_ts
"""
  __slots__ = ['icon_info','text_info','sound_info','hmi_highlight_obj_id','left_lane_flash','right_lane_flash','publish_ptp_ts','publisher_id','counter','publish_ts']
  _slot_types = ['uint32','int32','uint32','uint32[]','bool','bool','uint64','string','uint64','uint64']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       icon_info,text_info,sound_info,hmi_highlight_obj_id,left_lane_flash,right_lane_flash,publish_ptp_ts,publisher_id,counter,publish_ts

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(EHYHaOutputs, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.icon_info is None:
        self.icon_info = 0
      if self.text_info is None:
        self.text_info = 0
      if self.sound_info is None:
        self.sound_info = 0
      if self.hmi_highlight_obj_id is None:
        self.hmi_highlight_obj_id = []
      if self.left_lane_flash is None:
        self.left_lane_flash = False
      if self.right_lane_flash is None:
        self.right_lane_flash = False
      if self.publish_ptp_ts is None:
        self.publish_ptp_ts = 0
      if self.publisher_id is None:
        self.publisher_id = ''
      if self.counter is None:
        self.counter = 0
      if self.publish_ts is None:
        self.publish_ts = 0
    else:
      self.icon_info = 0
      self.text_info = 0
      self.sound_info = 0
      self.hmi_highlight_obj_id = []
      self.left_lane_flash = False
      self.right_lane_flash = False
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
      buff.write(_get_struct_IiI().pack(_x.icon_info, _x.text_info, _x.sound_info))
      length = len(self.hmi_highlight_obj_id)
      buff.write(_struct_I.pack(length))
      pattern = '<%sI'%length
      buff.write(struct.Struct(pattern).pack(*self.hmi_highlight_obj_id))
      _x = self
      buff.write(_get_struct_2BQ().pack(_x.left_lane_flash, _x.right_lane_flash, _x.publish_ptp_ts))
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
      end += 12
      (_x.icon_info, _x.text_info, _x.sound_info,) = _get_struct_IiI().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sI'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.hmi_highlight_obj_id = s.unpack(str[start:end])
      _x = self
      start = end
      end += 10
      (_x.left_lane_flash, _x.right_lane_flash, _x.publish_ptp_ts,) = _get_struct_2BQ().unpack(str[start:end])
      self.left_lane_flash = bool(self.left_lane_flash)
      self.right_lane_flash = bool(self.right_lane_flash)
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
      buff.write(_get_struct_IiI().pack(_x.icon_info, _x.text_info, _x.sound_info))
      length = len(self.hmi_highlight_obj_id)
      buff.write(_struct_I.pack(length))
      pattern = '<%sI'%length
      buff.write(self.hmi_highlight_obj_id.tostring())
      _x = self
      buff.write(_get_struct_2BQ().pack(_x.left_lane_flash, _x.right_lane_flash, _x.publish_ptp_ts))
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
      end += 12
      (_x.icon_info, _x.text_info, _x.sound_info,) = _get_struct_IiI().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sI'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.hmi_highlight_obj_id = numpy.frombuffer(str[start:end], dtype=numpy.uint32, count=length)
      _x = self
      start = end
      end += 10
      (_x.left_lane_flash, _x.right_lane_flash, _x.publish_ptp_ts,) = _get_struct_2BQ().unpack(str[start:end])
      self.left_lane_flash = bool(self.left_lane_flash)
      self.right_lane_flash = bool(self.right_lane_flash)
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
_struct_2BQ = None
def _get_struct_2BQ():
    global _struct_2BQ
    if _struct_2BQ is None:
        _struct_2BQ = struct.Struct("<2BQ")
    return _struct_2BQ
_struct_2Q = None
def _get_struct_2Q():
    global _struct_2Q
    if _struct_2Q is None:
        _struct_2Q = struct.Struct("<2Q")
    return _struct_2Q
_struct_IiI = None
def _get_struct_IiI():
    global _struct_IiI
    if _struct_IiI is None:
        _struct_IiI = struct.Struct("<IiI")
    return _struct_IiI

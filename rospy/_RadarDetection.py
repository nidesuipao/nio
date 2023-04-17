# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from rospy_message_converter/RadarDetection.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import rospy_message_converter.msg

class RadarDetection(genpy.Message):
  _md5sum = "7f8b2da5c6d35382acc206117e047827"
  _type = "rospy_message_converter/RadarDetection"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """uint64 timestamp
uint32 sync_bit
RadarDetectionObject[] detection

================================================================================
MSG: rospy_message_converter/RadarDetectionObject
uint32 ID
int32 source
float32 range
float32 range_rate
float32 azimuth
float32 elevation_angle
float32 radar_cross_section
float32 azimuth_conf
float32 elevation_conf
float32 exist_prob
"""
  __slots__ = ['timestamp','sync_bit','detection']
  _slot_types = ['uint64','uint32','rospy_message_converter/RadarDetectionObject[]']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       timestamp,sync_bit,detection

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(RadarDetection, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.timestamp is None:
        self.timestamp = 0
      if self.sync_bit is None:
        self.sync_bit = 0
      if self.detection is None:
        self.detection = []
    else:
      self.timestamp = 0
      self.sync_bit = 0
      self.detection = []

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
      buff.write(_get_struct_QI().pack(_x.timestamp, _x.sync_bit))
      length = len(self.detection)
      buff.write(_struct_I.pack(length))
      for val1 in self.detection:
        _x = val1
        buff.write(_get_struct_Ii8f().pack(_x.ID, _x.source, _x.range, _x.range_rate, _x.azimuth, _x.elevation_angle, _x.radar_cross_section, _x.azimuth_conf, _x.elevation_conf, _x.exist_prob))
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
      if self.detection is None:
        self.detection = None
      end = 0
      _x = self
      start = end
      end += 12
      (_x.timestamp, _x.sync_bit,) = _get_struct_QI().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.detection = []
      for i in range(0, length):
        val1 = rospy_message_converter.msg.RadarDetectionObject()
        _x = val1
        start = end
        end += 40
        (_x.ID, _x.source, _x.range, _x.range_rate, _x.azimuth, _x.elevation_angle, _x.radar_cross_section, _x.azimuth_conf, _x.elevation_conf, _x.exist_prob,) = _get_struct_Ii8f().unpack(str[start:end])
        self.detection.append(val1)
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
      buff.write(_get_struct_QI().pack(_x.timestamp, _x.sync_bit))
      length = len(self.detection)
      buff.write(_struct_I.pack(length))
      for val1 in self.detection:
        _x = val1
        buff.write(_get_struct_Ii8f().pack(_x.ID, _x.source, _x.range, _x.range_rate, _x.azimuth, _x.elevation_angle, _x.radar_cross_section, _x.azimuth_conf, _x.elevation_conf, _x.exist_prob))
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
      if self.detection is None:
        self.detection = None
      end = 0
      _x = self
      start = end
      end += 12
      (_x.timestamp, _x.sync_bit,) = _get_struct_QI().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.detection = []
      for i in range(0, length):
        val1 = rospy_message_converter.msg.RadarDetectionObject()
        _x = val1
        start = end
        end += 40
        (_x.ID, _x.source, _x.range, _x.range_rate, _x.azimuth, _x.elevation_angle, _x.radar_cross_section, _x.azimuth_conf, _x.elevation_conf, _x.exist_prob,) = _get_struct_Ii8f().unpack(str[start:end])
        self.detection.append(val1)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_Ii8f = None
def _get_struct_Ii8f():
    global _struct_Ii8f
    if _struct_Ii8f is None:
        _struct_Ii8f = struct.Struct("<Ii8f")
    return _struct_Ii8f
_struct_QI = None
def _get_struct_QI():
    global _struct_QI
    if _struct_QI is None:
        _struct_QI = struct.Struct("<QI")
    return _struct_QI

# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from rospy_message_converter/ParLocation.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import rospy_message_converter.msg

class ParLocation(genpy.Message):
  _md5sum = "2585a34f50cd6470f7b42dadfa09707a"
  _type = "rospy_message_converter/ParLocation"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """uint64 timestamp
bool location_valid
ParPoint position
ParQuaternion orientation
float32 easting
float32 northing
float32 height
float32 speed
float32 sum_s

================================================================================
MSG: rospy_message_converter/ParPoint
float32 x
float32 y
float32 z

================================================================================
MSG: rospy_message_converter/ParQuaternion
float32 x
float32 y
float32 z
float32 w
"""
  __slots__ = ['timestamp','location_valid','position','orientation','easting','northing','height','speed','sum_s']
  _slot_types = ['uint64','bool','rospy_message_converter/ParPoint','rospy_message_converter/ParQuaternion','float32','float32','float32','float32','float32']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       timestamp,location_valid,position,orientation,easting,northing,height,speed,sum_s

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(ParLocation, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.timestamp is None:
        self.timestamp = 0
      if self.location_valid is None:
        self.location_valid = False
      if self.position is None:
        self.position = rospy_message_converter.msg.ParPoint()
      if self.orientation is None:
        self.orientation = rospy_message_converter.msg.ParQuaternion()
      if self.easting is None:
        self.easting = 0.
      if self.northing is None:
        self.northing = 0.
      if self.height is None:
        self.height = 0.
      if self.speed is None:
        self.speed = 0.
      if self.sum_s is None:
        self.sum_s = 0.
    else:
      self.timestamp = 0
      self.location_valid = False
      self.position = rospy_message_converter.msg.ParPoint()
      self.orientation = rospy_message_converter.msg.ParQuaternion()
      self.easting = 0.
      self.northing = 0.
      self.height = 0.
      self.speed = 0.
      self.sum_s = 0.

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
      buff.write(_get_struct_QB12f().pack(_x.timestamp, _x.location_valid, _x.position.x, _x.position.y, _x.position.z, _x.orientation.x, _x.orientation.y, _x.orientation.z, _x.orientation.w, _x.easting, _x.northing, _x.height, _x.speed, _x.sum_s))
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
      if self.position is None:
        self.position = rospy_message_converter.msg.ParPoint()
      if self.orientation is None:
        self.orientation = rospy_message_converter.msg.ParQuaternion()
      end = 0
      _x = self
      start = end
      end += 57
      (_x.timestamp, _x.location_valid, _x.position.x, _x.position.y, _x.position.z, _x.orientation.x, _x.orientation.y, _x.orientation.z, _x.orientation.w, _x.easting, _x.northing, _x.height, _x.speed, _x.sum_s,) = _get_struct_QB12f().unpack(str[start:end])
      self.location_valid = bool(self.location_valid)
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
      buff.write(_get_struct_QB12f().pack(_x.timestamp, _x.location_valid, _x.position.x, _x.position.y, _x.position.z, _x.orientation.x, _x.orientation.y, _x.orientation.z, _x.orientation.w, _x.easting, _x.northing, _x.height, _x.speed, _x.sum_s))
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
      if self.position is None:
        self.position = rospy_message_converter.msg.ParPoint()
      if self.orientation is None:
        self.orientation = rospy_message_converter.msg.ParQuaternion()
      end = 0
      _x = self
      start = end
      end += 57
      (_x.timestamp, _x.location_valid, _x.position.x, _x.position.y, _x.position.z, _x.orientation.x, _x.orientation.y, _x.orientation.z, _x.orientation.w, _x.easting, _x.northing, _x.height, _x.speed, _x.sum_s,) = _get_struct_QB12f().unpack(str[start:end])
      self.location_valid = bool(self.location_valid)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_QB12f = None
def _get_struct_QB12f():
    global _struct_QB12f
    if _struct_QB12f is None:
        _struct_QB12f = struct.Struct("<QB12f")
    return _struct_QB12f

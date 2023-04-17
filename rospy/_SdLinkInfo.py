# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from rospy_message_converter/SdLinkInfo.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import rospy_message_converter.msg

class SdLinkInfo(genpy.Message):
  _md5sum = "b2c97fde8c963a5fa495309de01f4175"
  _type = "rospy_message_converter/SdLinkInfo"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """uint64 sd_link_id
Point3d[] shape_points
float32 link_length

================================================================================
MSG: rospy_message_converter/Point3d
float64 longitude
float64 latitude
float64 altitude
"""
  __slots__ = ['sd_link_id','shape_points','link_length']
  _slot_types = ['uint64','rospy_message_converter/Point3d[]','float32']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       sd_link_id,shape_points,link_length

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(SdLinkInfo, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.sd_link_id is None:
        self.sd_link_id = 0
      if self.shape_points is None:
        self.shape_points = []
      if self.link_length is None:
        self.link_length = 0.
    else:
      self.sd_link_id = 0
      self.shape_points = []
      self.link_length = 0.

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
      _x = self.sd_link_id
      buff.write(_get_struct_Q().pack(_x))
      length = len(self.shape_points)
      buff.write(_struct_I.pack(length))
      for val1 in self.shape_points:
        _x = val1
        buff.write(_get_struct_3d().pack(_x.longitude, _x.latitude, _x.altitude))
      _x = self.link_length
      buff.write(_get_struct_f().pack(_x))
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
      if self.shape_points is None:
        self.shape_points = None
      end = 0
      start = end
      end += 8
      (self.sd_link_id,) = _get_struct_Q().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.shape_points = []
      for i in range(0, length):
        val1 = rospy_message_converter.msg.Point3d()
        _x = val1
        start = end
        end += 24
        (_x.longitude, _x.latitude, _x.altitude,) = _get_struct_3d().unpack(str[start:end])
        self.shape_points.append(val1)
      start = end
      end += 4
      (self.link_length,) = _get_struct_f().unpack(str[start:end])
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
      _x = self.sd_link_id
      buff.write(_get_struct_Q().pack(_x))
      length = len(self.shape_points)
      buff.write(_struct_I.pack(length))
      for val1 in self.shape_points:
        _x = val1
        buff.write(_get_struct_3d().pack(_x.longitude, _x.latitude, _x.altitude))
      _x = self.link_length
      buff.write(_get_struct_f().pack(_x))
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
      if self.shape_points is None:
        self.shape_points = None
      end = 0
      start = end
      end += 8
      (self.sd_link_id,) = _get_struct_Q().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.shape_points = []
      for i in range(0, length):
        val1 = rospy_message_converter.msg.Point3d()
        _x = val1
        start = end
        end += 24
        (_x.longitude, _x.latitude, _x.altitude,) = _get_struct_3d().unpack(str[start:end])
        self.shape_points.append(val1)
      start = end
      end += 4
      (self.link_length,) = _get_struct_f().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_3d = None
def _get_struct_3d():
    global _struct_3d
    if _struct_3d is None:
        _struct_3d = struct.Struct("<3d")
    return _struct_3d
_struct_Q = None
def _get_struct_Q():
    global _struct_Q
    if _struct_Q is None:
        _struct_Q = struct.Struct("<Q")
    return _struct_Q
_struct_f = None
def _get_struct_f():
    global _struct_f
    if _struct_f is None:
        _struct_f = struct.Struct("<f")
    return _struct_f

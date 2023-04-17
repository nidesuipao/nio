# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from rospy_message_converter/ParEnvObjectInfo.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import rospy_message_converter.msg

class ParEnvObjectInfo(genpy.Message):
  _md5sum = "a1391c52ab3c6defa4fad06d95048ba8"
  _type = "rospy_message_converter/ParEnvObjectInfo"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """int32 type
int32 src
ParEnvObjectPoint pt
ParEnvObjectSegment line
ParEnvObjectPolygon polygon

================================================================================
MSG: rospy_message_converter/ParEnvObjectPoint
float32 x
float32 y

================================================================================
MSG: rospy_message_converter/ParEnvObjectSegment
ParEnvObjectPoint pt1
ParEnvObjectPoint pt2

================================================================================
MSG: rospy_message_converter/ParEnvObjectPolygon
ParEnvObjectPoint[] pts
"""
  __slots__ = ['type','src','pt','line','polygon']
  _slot_types = ['int32','int32','rospy_message_converter/ParEnvObjectPoint','rospy_message_converter/ParEnvObjectSegment','rospy_message_converter/ParEnvObjectPolygon']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       type,src,pt,line,polygon

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(ParEnvObjectInfo, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.type is None:
        self.type = 0
      if self.src is None:
        self.src = 0
      if self.pt is None:
        self.pt = rospy_message_converter.msg.ParEnvObjectPoint()
      if self.line is None:
        self.line = rospy_message_converter.msg.ParEnvObjectSegment()
      if self.polygon is None:
        self.polygon = rospy_message_converter.msg.ParEnvObjectPolygon()
    else:
      self.type = 0
      self.src = 0
      self.pt = rospy_message_converter.msg.ParEnvObjectPoint()
      self.line = rospy_message_converter.msg.ParEnvObjectSegment()
      self.polygon = rospy_message_converter.msg.ParEnvObjectPolygon()

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
      buff.write(_get_struct_2i6f().pack(_x.type, _x.src, _x.pt.x, _x.pt.y, _x.line.pt1.x, _x.line.pt1.y, _x.line.pt2.x, _x.line.pt2.y))
      length = len(self.polygon.pts)
      buff.write(_struct_I.pack(length))
      for val1 in self.polygon.pts:
        _x = val1
        buff.write(_get_struct_2f().pack(_x.x, _x.y))
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
      if self.pt is None:
        self.pt = rospy_message_converter.msg.ParEnvObjectPoint()
      if self.line is None:
        self.line = rospy_message_converter.msg.ParEnvObjectSegment()
      if self.polygon is None:
        self.polygon = rospy_message_converter.msg.ParEnvObjectPolygon()
      end = 0
      _x = self
      start = end
      end += 32
      (_x.type, _x.src, _x.pt.x, _x.pt.y, _x.line.pt1.x, _x.line.pt1.y, _x.line.pt2.x, _x.line.pt2.y,) = _get_struct_2i6f().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.polygon.pts = []
      for i in range(0, length):
        val1 = rospy_message_converter.msg.ParEnvObjectPoint()
        _x = val1
        start = end
        end += 8
        (_x.x, _x.y,) = _get_struct_2f().unpack(str[start:end])
        self.polygon.pts.append(val1)
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
      buff.write(_get_struct_2i6f().pack(_x.type, _x.src, _x.pt.x, _x.pt.y, _x.line.pt1.x, _x.line.pt1.y, _x.line.pt2.x, _x.line.pt2.y))
      length = len(self.polygon.pts)
      buff.write(_struct_I.pack(length))
      for val1 in self.polygon.pts:
        _x = val1
        buff.write(_get_struct_2f().pack(_x.x, _x.y))
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
      if self.pt is None:
        self.pt = rospy_message_converter.msg.ParEnvObjectPoint()
      if self.line is None:
        self.line = rospy_message_converter.msg.ParEnvObjectSegment()
      if self.polygon is None:
        self.polygon = rospy_message_converter.msg.ParEnvObjectPolygon()
      end = 0
      _x = self
      start = end
      end += 32
      (_x.type, _x.src, _x.pt.x, _x.pt.y, _x.line.pt1.x, _x.line.pt1.y, _x.line.pt2.x, _x.line.pt2.y,) = _get_struct_2i6f().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.polygon.pts = []
      for i in range(0, length):
        val1 = rospy_message_converter.msg.ParEnvObjectPoint()
        _x = val1
        start = end
        end += 8
        (_x.x, _x.y,) = _get_struct_2f().unpack(str[start:end])
        self.polygon.pts.append(val1)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_2f = None
def _get_struct_2f():
    global _struct_2f
    if _struct_2f is None:
        _struct_2f = struct.Struct("<2f")
    return _struct_2f
_struct_2i6f = None
def _get_struct_2i6f():
    global _struct_2i6f
    if _struct_2i6f is None:
        _struct_2i6f = struct.Struct("<2i6f")
    return _struct_2i6f

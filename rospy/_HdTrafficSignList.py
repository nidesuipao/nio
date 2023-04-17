# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from rospy_message_converter/HdTrafficSignList.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import rospy_message_converter.msg

class HdTrafficSignList(genpy.Message):
  _md5sum = "e2574d01267ce9c972678bb107f24590"
  _type = "rospy_message_converter/HdTrafficSignList"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """HdTrafficSign[] traffic_sign_list

================================================================================
MSG: rospy_message_converter/HdTrafficSign
uint64 id
MapPolygon surface
int32 type
float64 heading
uint64[] lane_id
MapPoint center

================================================================================
MSG: rospy_message_converter/MapPolygon
float64[] x
float64[] y
float64[] z

================================================================================
MSG: rospy_message_converter/MapPoint
float64 x
float64 y
float64 z
"""
  __slots__ = ['traffic_sign_list']
  _slot_types = ['rospy_message_converter/HdTrafficSign[]']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       traffic_sign_list

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(HdTrafficSignList, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.traffic_sign_list is None:
        self.traffic_sign_list = []
    else:
      self.traffic_sign_list = []

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
      length = len(self.traffic_sign_list)
      buff.write(_struct_I.pack(length))
      for val1 in self.traffic_sign_list:
        _x = val1.id
        buff.write(_get_struct_Q().pack(_x))
        _v1 = val1.surface
        length = len(_v1.x)
        buff.write(_struct_I.pack(length))
        pattern = '<%sd'%length
        buff.write(struct.Struct(pattern).pack(*_v1.x))
        length = len(_v1.y)
        buff.write(_struct_I.pack(length))
        pattern = '<%sd'%length
        buff.write(struct.Struct(pattern).pack(*_v1.y))
        length = len(_v1.z)
        buff.write(_struct_I.pack(length))
        pattern = '<%sd'%length
        buff.write(struct.Struct(pattern).pack(*_v1.z))
        _x = val1
        buff.write(_get_struct_id().pack(_x.type, _x.heading))
        length = len(val1.lane_id)
        buff.write(_struct_I.pack(length))
        pattern = '<%sQ'%length
        buff.write(struct.Struct(pattern).pack(*val1.lane_id))
        _v2 = val1.center
        _x = _v2
        buff.write(_get_struct_3d().pack(_x.x, _x.y, _x.z))
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
      if self.traffic_sign_list is None:
        self.traffic_sign_list = None
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.traffic_sign_list = []
      for i in range(0, length):
        val1 = rospy_message_converter.msg.HdTrafficSign()
        start = end
        end += 8
        (val1.id,) = _get_struct_Q().unpack(str[start:end])
        _v3 = val1.surface
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        pattern = '<%sd'%length
        start = end
        s = struct.Struct(pattern)
        end += s.size
        _v3.x = s.unpack(str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        pattern = '<%sd'%length
        start = end
        s = struct.Struct(pattern)
        end += s.size
        _v3.y = s.unpack(str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        pattern = '<%sd'%length
        start = end
        s = struct.Struct(pattern)
        end += s.size
        _v3.z = s.unpack(str[start:end])
        _x = val1
        start = end
        end += 12
        (_x.type, _x.heading,) = _get_struct_id().unpack(str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        pattern = '<%sQ'%length
        start = end
        s = struct.Struct(pattern)
        end += s.size
        val1.lane_id = s.unpack(str[start:end])
        _v4 = val1.center
        _x = _v4
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _get_struct_3d().unpack(str[start:end])
        self.traffic_sign_list.append(val1)
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
      length = len(self.traffic_sign_list)
      buff.write(_struct_I.pack(length))
      for val1 in self.traffic_sign_list:
        _x = val1.id
        buff.write(_get_struct_Q().pack(_x))
        _v5 = val1.surface
        length = len(_v5.x)
        buff.write(_struct_I.pack(length))
        pattern = '<%sd'%length
        buff.write(_v5.x.tostring())
        length = len(_v5.y)
        buff.write(_struct_I.pack(length))
        pattern = '<%sd'%length
        buff.write(_v5.y.tostring())
        length = len(_v5.z)
        buff.write(_struct_I.pack(length))
        pattern = '<%sd'%length
        buff.write(_v5.z.tostring())
        _x = val1
        buff.write(_get_struct_id().pack(_x.type, _x.heading))
        length = len(val1.lane_id)
        buff.write(_struct_I.pack(length))
        pattern = '<%sQ'%length
        buff.write(val1.lane_id.tostring())
        _v6 = val1.center
        _x = _v6
        buff.write(_get_struct_3d().pack(_x.x, _x.y, _x.z))
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
      if self.traffic_sign_list is None:
        self.traffic_sign_list = None
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.traffic_sign_list = []
      for i in range(0, length):
        val1 = rospy_message_converter.msg.HdTrafficSign()
        start = end
        end += 8
        (val1.id,) = _get_struct_Q().unpack(str[start:end])
        _v7 = val1.surface
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        pattern = '<%sd'%length
        start = end
        s = struct.Struct(pattern)
        end += s.size
        _v7.x = numpy.frombuffer(str[start:end], dtype=numpy.float64, count=length)
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        pattern = '<%sd'%length
        start = end
        s = struct.Struct(pattern)
        end += s.size
        _v7.y = numpy.frombuffer(str[start:end], dtype=numpy.float64, count=length)
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        pattern = '<%sd'%length
        start = end
        s = struct.Struct(pattern)
        end += s.size
        _v7.z = numpy.frombuffer(str[start:end], dtype=numpy.float64, count=length)
        _x = val1
        start = end
        end += 12
        (_x.type, _x.heading,) = _get_struct_id().unpack(str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        pattern = '<%sQ'%length
        start = end
        s = struct.Struct(pattern)
        end += s.size
        val1.lane_id = numpy.frombuffer(str[start:end], dtype=numpy.uint64, count=length)
        _v8 = val1.center
        _x = _v8
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _get_struct_3d().unpack(str[start:end])
        self.traffic_sign_list.append(val1)
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
_struct_id = None
def _get_struct_id():
    global _struct_id
    if _struct_id is None:
        _struct_id = struct.Struct("<id")
    return _struct_id

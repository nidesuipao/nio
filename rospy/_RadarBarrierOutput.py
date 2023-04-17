# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from rospy_message_converter/RadarBarrierOutput.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import rospy_message_converter.msg

class RadarBarrierOutput(genpy.Message):
  _md5sum = "2a383e6cd09a8c39847d2623254d881d"
  _type = "rospy_message_converter/RadarBarrierOutput"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """RadarBarrier barrier_left
RadarBarrier barrier_right

================================================================================
MSG: rospy_message_converter/RadarBarrier
float32[] coef
float32 dist_end
float32 dist_from
uint32 lka_confidence
"""
  __slots__ = ['barrier_left','barrier_right']
  _slot_types = ['rospy_message_converter/RadarBarrier','rospy_message_converter/RadarBarrier']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       barrier_left,barrier_right

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(RadarBarrierOutput, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.barrier_left is None:
        self.barrier_left = rospy_message_converter.msg.RadarBarrier()
      if self.barrier_right is None:
        self.barrier_right = rospy_message_converter.msg.RadarBarrier()
    else:
      self.barrier_left = rospy_message_converter.msg.RadarBarrier()
      self.barrier_right = rospy_message_converter.msg.RadarBarrier()

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
      length = len(self.barrier_left.coef)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(struct.Struct(pattern).pack(*self.barrier_left.coef))
      _x = self
      buff.write(_get_struct_2fI().pack(_x.barrier_left.dist_end, _x.barrier_left.dist_from, _x.barrier_left.lka_confidence))
      length = len(self.barrier_right.coef)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(struct.Struct(pattern).pack(*self.barrier_right.coef))
      _x = self
      buff.write(_get_struct_2fI().pack(_x.barrier_right.dist_end, _x.barrier_right.dist_from, _x.barrier_right.lka_confidence))
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
      if self.barrier_left is None:
        self.barrier_left = rospy_message_converter.msg.RadarBarrier()
      if self.barrier_right is None:
        self.barrier_right = rospy_message_converter.msg.RadarBarrier()
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sf'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.barrier_left.coef = s.unpack(str[start:end])
      _x = self
      start = end
      end += 12
      (_x.barrier_left.dist_end, _x.barrier_left.dist_from, _x.barrier_left.lka_confidence,) = _get_struct_2fI().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sf'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.barrier_right.coef = s.unpack(str[start:end])
      _x = self
      start = end
      end += 12
      (_x.barrier_right.dist_end, _x.barrier_right.dist_from, _x.barrier_right.lka_confidence,) = _get_struct_2fI().unpack(str[start:end])
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
      length = len(self.barrier_left.coef)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(self.barrier_left.coef.tostring())
      _x = self
      buff.write(_get_struct_2fI().pack(_x.barrier_left.dist_end, _x.barrier_left.dist_from, _x.barrier_left.lka_confidence))
      length = len(self.barrier_right.coef)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(self.barrier_right.coef.tostring())
      _x = self
      buff.write(_get_struct_2fI().pack(_x.barrier_right.dist_end, _x.barrier_right.dist_from, _x.barrier_right.lka_confidence))
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
      if self.barrier_left is None:
        self.barrier_left = rospy_message_converter.msg.RadarBarrier()
      if self.barrier_right is None:
        self.barrier_right = rospy_message_converter.msg.RadarBarrier()
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sf'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.barrier_left.coef = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=length)
      _x = self
      start = end
      end += 12
      (_x.barrier_left.dist_end, _x.barrier_left.dist_from, _x.barrier_left.lka_confidence,) = _get_struct_2fI().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sf'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.barrier_right.coef = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=length)
      _x = self
      start = end
      end += 12
      (_x.barrier_right.dist_end, _x.barrier_right.dist_from, _x.barrier_right.lka_confidence,) = _get_struct_2fI().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_2fI = None
def _get_struct_2fI():
    global _struct_2fI
    if _struct_2fI is None:
        _struct_2fI = struct.Struct("<2fI")
    return _struct_2fI

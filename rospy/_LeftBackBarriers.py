# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from rospy_message_converter/LeftBackBarriers.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class LeftBackBarriers(genpy.Message):
  _md5sum = "8646784504d9b11d2ed1d9536d9a786c"
  _type = "rospy_message_converter/LeftBackBarriers"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """float32 left_back_c0
float32 left_back_c1
float32 left_back_c2
float32 left_back_c3
uint32 barrier_conf
float32 left_back_start_distance
float32 left_back_end_distance
"""
  __slots__ = ['left_back_c0','left_back_c1','left_back_c2','left_back_c3','barrier_conf','left_back_start_distance','left_back_end_distance']
  _slot_types = ['float32','float32','float32','float32','uint32','float32','float32']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       left_back_c0,left_back_c1,left_back_c2,left_back_c3,barrier_conf,left_back_start_distance,left_back_end_distance

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(LeftBackBarriers, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.left_back_c0 is None:
        self.left_back_c0 = 0.
      if self.left_back_c1 is None:
        self.left_back_c1 = 0.
      if self.left_back_c2 is None:
        self.left_back_c2 = 0.
      if self.left_back_c3 is None:
        self.left_back_c3 = 0.
      if self.barrier_conf is None:
        self.barrier_conf = 0
      if self.left_back_start_distance is None:
        self.left_back_start_distance = 0.
      if self.left_back_end_distance is None:
        self.left_back_end_distance = 0.
    else:
      self.left_back_c0 = 0.
      self.left_back_c1 = 0.
      self.left_back_c2 = 0.
      self.left_back_c3 = 0.
      self.barrier_conf = 0
      self.left_back_start_distance = 0.
      self.left_back_end_distance = 0.

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
      buff.write(_get_struct_4fI2f().pack(_x.left_back_c0, _x.left_back_c1, _x.left_back_c2, _x.left_back_c3, _x.barrier_conf, _x.left_back_start_distance, _x.left_back_end_distance))
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
      (_x.left_back_c0, _x.left_back_c1, _x.left_back_c2, _x.left_back_c3, _x.barrier_conf, _x.left_back_start_distance, _x.left_back_end_distance,) = _get_struct_4fI2f().unpack(str[start:end])
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
      buff.write(_get_struct_4fI2f().pack(_x.left_back_c0, _x.left_back_c1, _x.left_back_c2, _x.left_back_c3, _x.barrier_conf, _x.left_back_start_distance, _x.left_back_end_distance))
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
      (_x.left_back_c0, _x.left_back_c1, _x.left_back_c2, _x.left_back_c3, _x.barrier_conf, _x.left_back_start_distance, _x.left_back_end_distance,) = _get_struct_4fI2f().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_4fI2f = None
def _get_struct_4fI2f():
    global _struct_4fI2f
    if _struct_4fI2f is None:
        _struct_4fI2f = struct.Struct("<4fI2f")
    return _struct_4fI2f

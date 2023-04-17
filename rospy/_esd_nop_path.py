# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from rospy_message_converter/esd_nop_path.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import rospy_message_converter.msg

class esd_nop_path(genpy.Message):
  _md5sum = "dda27acd1e345a76215337889733a7f3"
  _type = "rospy_message_converter/esd_nop_path"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """esd_nop_path_point[] esd_nop_path_points
float32 esd_nop_discrete_path_length
bool esd_nop_discrete_path_enable

================================================================================
MSG: rospy_message_converter/esd_nop_path_point
float32 x
float32 y
float32 z
"""
  __slots__ = ['esd_nop_path_points','esd_nop_discrete_path_length','esd_nop_discrete_path_enable']
  _slot_types = ['rospy_message_converter/esd_nop_path_point[]','float32','bool']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       esd_nop_path_points,esd_nop_discrete_path_length,esd_nop_discrete_path_enable

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(esd_nop_path, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.esd_nop_path_points is None:
        self.esd_nop_path_points = []
      if self.esd_nop_discrete_path_length is None:
        self.esd_nop_discrete_path_length = 0.
      if self.esd_nop_discrete_path_enable is None:
        self.esd_nop_discrete_path_enable = False
    else:
      self.esd_nop_path_points = []
      self.esd_nop_discrete_path_length = 0.
      self.esd_nop_discrete_path_enable = False

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
      length = len(self.esd_nop_path_points)
      buff.write(_struct_I.pack(length))
      for val1 in self.esd_nop_path_points:
        _x = val1
        buff.write(_get_struct_3f().pack(_x.x, _x.y, _x.z))
      _x = self
      buff.write(_get_struct_fB().pack(_x.esd_nop_discrete_path_length, _x.esd_nop_discrete_path_enable))
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
      if self.esd_nop_path_points is None:
        self.esd_nop_path_points = None
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.esd_nop_path_points = []
      for i in range(0, length):
        val1 = rospy_message_converter.msg.esd_nop_path_point()
        _x = val1
        start = end
        end += 12
        (_x.x, _x.y, _x.z,) = _get_struct_3f().unpack(str[start:end])
        self.esd_nop_path_points.append(val1)
      _x = self
      start = end
      end += 5
      (_x.esd_nop_discrete_path_length, _x.esd_nop_discrete_path_enable,) = _get_struct_fB().unpack(str[start:end])
      self.esd_nop_discrete_path_enable = bool(self.esd_nop_discrete_path_enable)
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
      length = len(self.esd_nop_path_points)
      buff.write(_struct_I.pack(length))
      for val1 in self.esd_nop_path_points:
        _x = val1
        buff.write(_get_struct_3f().pack(_x.x, _x.y, _x.z))
      _x = self
      buff.write(_get_struct_fB().pack(_x.esd_nop_discrete_path_length, _x.esd_nop_discrete_path_enable))
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
      if self.esd_nop_path_points is None:
        self.esd_nop_path_points = None
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.esd_nop_path_points = []
      for i in range(0, length):
        val1 = rospy_message_converter.msg.esd_nop_path_point()
        _x = val1
        start = end
        end += 12
        (_x.x, _x.y, _x.z,) = _get_struct_3f().unpack(str[start:end])
        self.esd_nop_path_points.append(val1)
      _x = self
      start = end
      end += 5
      (_x.esd_nop_discrete_path_length, _x.esd_nop_discrete_path_enable,) = _get_struct_fB().unpack(str[start:end])
      self.esd_nop_discrete_path_enable = bool(self.esd_nop_discrete_path_enable)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_3f = None
def _get_struct_3f():
    global _struct_3f
    if _struct_3f is None:
        _struct_3f = struct.Struct("<3f")
    return _struct_3f
_struct_fB = None
def _get_struct_fB():
    global _struct_fB
    if _struct_fB is None:
        _struct_fB = struct.Struct("<fB")
    return _struct_fB

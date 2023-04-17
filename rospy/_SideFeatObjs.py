# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from rospy_message_converter/SideFeatObjs.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class SideFeatObjs(genpy.Message):
  _md5sum = "9b0eecdc860583f3c52811c27e55b4b2"
  _type = "rospy_message_converter/SideFeatObjs"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """int32 long_pos_obj_1
int32 lat_pos_obj_1
int32 long_vel_obj_1
int32 lat_vel_obj_1
int32 long_pos_obj_2
int32 lat_pos_obj_2
int32 long_vel_obj_2
int32 lat_vel_obj_2
"""
  __slots__ = ['long_pos_obj_1','lat_pos_obj_1','long_vel_obj_1','lat_vel_obj_1','long_pos_obj_2','lat_pos_obj_2','long_vel_obj_2','lat_vel_obj_2']
  _slot_types = ['int32','int32','int32','int32','int32','int32','int32','int32']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       long_pos_obj_1,lat_pos_obj_1,long_vel_obj_1,lat_vel_obj_1,long_pos_obj_2,lat_pos_obj_2,long_vel_obj_2,lat_vel_obj_2

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(SideFeatObjs, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.long_pos_obj_1 is None:
        self.long_pos_obj_1 = 0
      if self.lat_pos_obj_1 is None:
        self.lat_pos_obj_1 = 0
      if self.long_vel_obj_1 is None:
        self.long_vel_obj_1 = 0
      if self.lat_vel_obj_1 is None:
        self.lat_vel_obj_1 = 0
      if self.long_pos_obj_2 is None:
        self.long_pos_obj_2 = 0
      if self.lat_pos_obj_2 is None:
        self.lat_pos_obj_2 = 0
      if self.long_vel_obj_2 is None:
        self.long_vel_obj_2 = 0
      if self.lat_vel_obj_2 is None:
        self.lat_vel_obj_2 = 0
    else:
      self.long_pos_obj_1 = 0
      self.lat_pos_obj_1 = 0
      self.long_vel_obj_1 = 0
      self.lat_vel_obj_1 = 0
      self.long_pos_obj_2 = 0
      self.lat_pos_obj_2 = 0
      self.long_vel_obj_2 = 0
      self.lat_vel_obj_2 = 0

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
      buff.write(_get_struct_8i().pack(_x.long_pos_obj_1, _x.lat_pos_obj_1, _x.long_vel_obj_1, _x.lat_vel_obj_1, _x.long_pos_obj_2, _x.lat_pos_obj_2, _x.long_vel_obj_2, _x.lat_vel_obj_2))
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
      end += 32
      (_x.long_pos_obj_1, _x.lat_pos_obj_1, _x.long_vel_obj_1, _x.lat_vel_obj_1, _x.long_pos_obj_2, _x.lat_pos_obj_2, _x.long_vel_obj_2, _x.lat_vel_obj_2,) = _get_struct_8i().unpack(str[start:end])
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
      buff.write(_get_struct_8i().pack(_x.long_pos_obj_1, _x.lat_pos_obj_1, _x.long_vel_obj_1, _x.lat_vel_obj_1, _x.long_pos_obj_2, _x.lat_pos_obj_2, _x.long_vel_obj_2, _x.lat_vel_obj_2))
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
      end += 32
      (_x.long_pos_obj_1, _x.lat_pos_obj_1, _x.long_vel_obj_1, _x.lat_vel_obj_1, _x.long_pos_obj_2, _x.lat_pos_obj_2, _x.long_vel_obj_2, _x.lat_vel_obj_2,) = _get_struct_8i().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_8i = None
def _get_struct_8i():
    global _struct_8i
    if _struct_8i is None:
        _struct_8i = struct.Struct("<8i")
    return _struct_8i

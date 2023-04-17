# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from rospy_message_converter/FreeSpaceEuclidean.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class FreeSpaceEuclidean(genpy.Message):
  _md5sum = "cb0efcac02b30f616c45ef0b342340f6"
  _type = "rospy_message_converter/FreeSpaceEuclidean"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """uint32 FSP_Obs_ID
int32 FSP_Lane_Assginment
float32 FSP_x
float32 FSP_y
int32 FSP_Classification_Type
float32 FSP_Height
float32 FSP_z
int32 FSP_Mobility_Status
float32 FSP_Existence_Prob
"""
  __slots__ = ['FSP_Obs_ID','FSP_Lane_Assginment','FSP_x','FSP_y','FSP_Classification_Type','FSP_Height','FSP_z','FSP_Mobility_Status','FSP_Existence_Prob']
  _slot_types = ['uint32','int32','float32','float32','int32','float32','float32','int32','float32']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       FSP_Obs_ID,FSP_Lane_Assginment,FSP_x,FSP_y,FSP_Classification_Type,FSP_Height,FSP_z,FSP_Mobility_Status,FSP_Existence_Prob

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(FreeSpaceEuclidean, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.FSP_Obs_ID is None:
        self.FSP_Obs_ID = 0
      if self.FSP_Lane_Assginment is None:
        self.FSP_Lane_Assginment = 0
      if self.FSP_x is None:
        self.FSP_x = 0.
      if self.FSP_y is None:
        self.FSP_y = 0.
      if self.FSP_Classification_Type is None:
        self.FSP_Classification_Type = 0
      if self.FSP_Height is None:
        self.FSP_Height = 0.
      if self.FSP_z is None:
        self.FSP_z = 0.
      if self.FSP_Mobility_Status is None:
        self.FSP_Mobility_Status = 0
      if self.FSP_Existence_Prob is None:
        self.FSP_Existence_Prob = 0.
    else:
      self.FSP_Obs_ID = 0
      self.FSP_Lane_Assginment = 0
      self.FSP_x = 0.
      self.FSP_y = 0.
      self.FSP_Classification_Type = 0
      self.FSP_Height = 0.
      self.FSP_z = 0.
      self.FSP_Mobility_Status = 0
      self.FSP_Existence_Prob = 0.

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
      buff.write(_get_struct_Ii2fi2fif().pack(_x.FSP_Obs_ID, _x.FSP_Lane_Assginment, _x.FSP_x, _x.FSP_y, _x.FSP_Classification_Type, _x.FSP_Height, _x.FSP_z, _x.FSP_Mobility_Status, _x.FSP_Existence_Prob))
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
      end += 36
      (_x.FSP_Obs_ID, _x.FSP_Lane_Assginment, _x.FSP_x, _x.FSP_y, _x.FSP_Classification_Type, _x.FSP_Height, _x.FSP_z, _x.FSP_Mobility_Status, _x.FSP_Existence_Prob,) = _get_struct_Ii2fi2fif().unpack(str[start:end])
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
      buff.write(_get_struct_Ii2fi2fif().pack(_x.FSP_Obs_ID, _x.FSP_Lane_Assginment, _x.FSP_x, _x.FSP_y, _x.FSP_Classification_Type, _x.FSP_Height, _x.FSP_z, _x.FSP_Mobility_Status, _x.FSP_Existence_Prob))
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
      end += 36
      (_x.FSP_Obs_ID, _x.FSP_Lane_Assginment, _x.FSP_x, _x.FSP_y, _x.FSP_Classification_Type, _x.FSP_Height, _x.FSP_z, _x.FSP_Mobility_Status, _x.FSP_Existence_Prob,) = _get_struct_Ii2fi2fif().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_Ii2fi2fif = None
def _get_struct_Ii2fi2fif():
    global _struct_Ii2fi2fif
    if _struct_Ii2fi2fif is None:
        _struct_Ii2fi2fif = struct.Struct("<Ii2fi2fif")
    return _struct_Ii2fi2fif

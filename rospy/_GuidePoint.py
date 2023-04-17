# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from rospy_message_converter/GuidePoint.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import rospy_message_converter.msg

class GuidePoint(genpy.Message):
  _md5sum = "e542163475b742c8a6b2238e60c33a42"
  _type = "rospy_message_converter/GuidePoint"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """bool INTP_Is_Highway_Merge_Left
bool INTP_Is_Highway_Merge_Right
bool INTP_Is_Highway_Exit_Left
bool INTP_Is_Highway_Exit_Right
InterestPoint[] INTP_Point

================================================================================
MSG: rospy_message_converter/InterestPoint
int32 INTP_Type
uint32 INTP_ID
uint32 INTP_Age
int32 INTP_Line_Role
float32 INTP_Long_Distance
float32 INTP_Lat_Distance
float32 INTP_Exist_Probability
"""
  __slots__ = ['INTP_Is_Highway_Merge_Left','INTP_Is_Highway_Merge_Right','INTP_Is_Highway_Exit_Left','INTP_Is_Highway_Exit_Right','INTP_Point']
  _slot_types = ['bool','bool','bool','bool','rospy_message_converter/InterestPoint[]']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       INTP_Is_Highway_Merge_Left,INTP_Is_Highway_Merge_Right,INTP_Is_Highway_Exit_Left,INTP_Is_Highway_Exit_Right,INTP_Point

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(GuidePoint, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.INTP_Is_Highway_Merge_Left is None:
        self.INTP_Is_Highway_Merge_Left = False
      if self.INTP_Is_Highway_Merge_Right is None:
        self.INTP_Is_Highway_Merge_Right = False
      if self.INTP_Is_Highway_Exit_Left is None:
        self.INTP_Is_Highway_Exit_Left = False
      if self.INTP_Is_Highway_Exit_Right is None:
        self.INTP_Is_Highway_Exit_Right = False
      if self.INTP_Point is None:
        self.INTP_Point = []
    else:
      self.INTP_Is_Highway_Merge_Left = False
      self.INTP_Is_Highway_Merge_Right = False
      self.INTP_Is_Highway_Exit_Left = False
      self.INTP_Is_Highway_Exit_Right = False
      self.INTP_Point = []

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
      buff.write(_get_struct_4B().pack(_x.INTP_Is_Highway_Merge_Left, _x.INTP_Is_Highway_Merge_Right, _x.INTP_Is_Highway_Exit_Left, _x.INTP_Is_Highway_Exit_Right))
      length = len(self.INTP_Point)
      buff.write(_struct_I.pack(length))
      for val1 in self.INTP_Point:
        _x = val1
        buff.write(_get_struct_i2Ii3f().pack(_x.INTP_Type, _x.INTP_ID, _x.INTP_Age, _x.INTP_Line_Role, _x.INTP_Long_Distance, _x.INTP_Lat_Distance, _x.INTP_Exist_Probability))
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
      if self.INTP_Point is None:
        self.INTP_Point = None
      end = 0
      _x = self
      start = end
      end += 4
      (_x.INTP_Is_Highway_Merge_Left, _x.INTP_Is_Highway_Merge_Right, _x.INTP_Is_Highway_Exit_Left, _x.INTP_Is_Highway_Exit_Right,) = _get_struct_4B().unpack(str[start:end])
      self.INTP_Is_Highway_Merge_Left = bool(self.INTP_Is_Highway_Merge_Left)
      self.INTP_Is_Highway_Merge_Right = bool(self.INTP_Is_Highway_Merge_Right)
      self.INTP_Is_Highway_Exit_Left = bool(self.INTP_Is_Highway_Exit_Left)
      self.INTP_Is_Highway_Exit_Right = bool(self.INTP_Is_Highway_Exit_Right)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.INTP_Point = []
      for i in range(0, length):
        val1 = rospy_message_converter.msg.InterestPoint()
        _x = val1
        start = end
        end += 28
        (_x.INTP_Type, _x.INTP_ID, _x.INTP_Age, _x.INTP_Line_Role, _x.INTP_Long_Distance, _x.INTP_Lat_Distance, _x.INTP_Exist_Probability,) = _get_struct_i2Ii3f().unpack(str[start:end])
        self.INTP_Point.append(val1)
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
      buff.write(_get_struct_4B().pack(_x.INTP_Is_Highway_Merge_Left, _x.INTP_Is_Highway_Merge_Right, _x.INTP_Is_Highway_Exit_Left, _x.INTP_Is_Highway_Exit_Right))
      length = len(self.INTP_Point)
      buff.write(_struct_I.pack(length))
      for val1 in self.INTP_Point:
        _x = val1
        buff.write(_get_struct_i2Ii3f().pack(_x.INTP_Type, _x.INTP_ID, _x.INTP_Age, _x.INTP_Line_Role, _x.INTP_Long_Distance, _x.INTP_Lat_Distance, _x.INTP_Exist_Probability))
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
      if self.INTP_Point is None:
        self.INTP_Point = None
      end = 0
      _x = self
      start = end
      end += 4
      (_x.INTP_Is_Highway_Merge_Left, _x.INTP_Is_Highway_Merge_Right, _x.INTP_Is_Highway_Exit_Left, _x.INTP_Is_Highway_Exit_Right,) = _get_struct_4B().unpack(str[start:end])
      self.INTP_Is_Highway_Merge_Left = bool(self.INTP_Is_Highway_Merge_Left)
      self.INTP_Is_Highway_Merge_Right = bool(self.INTP_Is_Highway_Merge_Right)
      self.INTP_Is_Highway_Exit_Left = bool(self.INTP_Is_Highway_Exit_Left)
      self.INTP_Is_Highway_Exit_Right = bool(self.INTP_Is_Highway_Exit_Right)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.INTP_Point = []
      for i in range(0, length):
        val1 = rospy_message_converter.msg.InterestPoint()
        _x = val1
        start = end
        end += 28
        (_x.INTP_Type, _x.INTP_ID, _x.INTP_Age, _x.INTP_Line_Role, _x.INTP_Long_Distance, _x.INTP_Lat_Distance, _x.INTP_Exist_Probability,) = _get_struct_i2Ii3f().unpack(str[start:end])
        self.INTP_Point.append(val1)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_4B = None
def _get_struct_4B():
    global _struct_4B
    if _struct_4B is None:
        _struct_4B = struct.Struct("<4B")
    return _struct_4B
_struct_i2Ii3f = None
def _get_struct_i2Ii3f():
    global _struct_i2Ii3f
    if _struct_i2Ii3f is None:
        _struct_i2Ii3f = struct.Struct("<i2Ii3f")
    return _struct_i2Ii3f

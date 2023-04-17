# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from rospy_message_converter/RoadSlop.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import rospy_message_converter.msg

class RoadSlop(genpy.Message):
  _md5sum = "30ebbda1fcc2c40c283cd00bff150807"
  _type = "rospy_message_converter/RoadSlop"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """bool LD_Road_Vertical_Surface_Available
float32 LD_Road_Vertical_Surface_Start
float32 LD_Road_Vertical_Surface_End
PolyLine LD_Road_Vertical_Surface

================================================================================
MSG: rospy_message_converter/PolyLine
float32 line_C0
float32 line_C1
float32 line_C2
float32 line_C3
"""
  __slots__ = ['LD_Road_Vertical_Surface_Available','LD_Road_Vertical_Surface_Start','LD_Road_Vertical_Surface_End','LD_Road_Vertical_Surface']
  _slot_types = ['bool','float32','float32','rospy_message_converter/PolyLine']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       LD_Road_Vertical_Surface_Available,LD_Road_Vertical_Surface_Start,LD_Road_Vertical_Surface_End,LD_Road_Vertical_Surface

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(RoadSlop, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.LD_Road_Vertical_Surface_Available is None:
        self.LD_Road_Vertical_Surface_Available = False
      if self.LD_Road_Vertical_Surface_Start is None:
        self.LD_Road_Vertical_Surface_Start = 0.
      if self.LD_Road_Vertical_Surface_End is None:
        self.LD_Road_Vertical_Surface_End = 0.
      if self.LD_Road_Vertical_Surface is None:
        self.LD_Road_Vertical_Surface = rospy_message_converter.msg.PolyLine()
    else:
      self.LD_Road_Vertical_Surface_Available = False
      self.LD_Road_Vertical_Surface_Start = 0.
      self.LD_Road_Vertical_Surface_End = 0.
      self.LD_Road_Vertical_Surface = rospy_message_converter.msg.PolyLine()

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
      buff.write(_get_struct_B6f().pack(_x.LD_Road_Vertical_Surface_Available, _x.LD_Road_Vertical_Surface_Start, _x.LD_Road_Vertical_Surface_End, _x.LD_Road_Vertical_Surface.line_C0, _x.LD_Road_Vertical_Surface.line_C1, _x.LD_Road_Vertical_Surface.line_C2, _x.LD_Road_Vertical_Surface.line_C3))
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
      if self.LD_Road_Vertical_Surface is None:
        self.LD_Road_Vertical_Surface = rospy_message_converter.msg.PolyLine()
      end = 0
      _x = self
      start = end
      end += 25
      (_x.LD_Road_Vertical_Surface_Available, _x.LD_Road_Vertical_Surface_Start, _x.LD_Road_Vertical_Surface_End, _x.LD_Road_Vertical_Surface.line_C0, _x.LD_Road_Vertical_Surface.line_C1, _x.LD_Road_Vertical_Surface.line_C2, _x.LD_Road_Vertical_Surface.line_C3,) = _get_struct_B6f().unpack(str[start:end])
      self.LD_Road_Vertical_Surface_Available = bool(self.LD_Road_Vertical_Surface_Available)
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
      buff.write(_get_struct_B6f().pack(_x.LD_Road_Vertical_Surface_Available, _x.LD_Road_Vertical_Surface_Start, _x.LD_Road_Vertical_Surface_End, _x.LD_Road_Vertical_Surface.line_C0, _x.LD_Road_Vertical_Surface.line_C1, _x.LD_Road_Vertical_Surface.line_C2, _x.LD_Road_Vertical_Surface.line_C3))
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
      if self.LD_Road_Vertical_Surface is None:
        self.LD_Road_Vertical_Surface = rospy_message_converter.msg.PolyLine()
      end = 0
      _x = self
      start = end
      end += 25
      (_x.LD_Road_Vertical_Surface_Available, _x.LD_Road_Vertical_Surface_Start, _x.LD_Road_Vertical_Surface_End, _x.LD_Road_Vertical_Surface.line_C0, _x.LD_Road_Vertical_Surface.line_C1, _x.LD_Road_Vertical_Surface.line_C2, _x.LD_Road_Vertical_Surface.line_C3,) = _get_struct_B6f().unpack(str[start:end])
      self.LD_Road_Vertical_Surface_Available = bool(self.LD_Road_Vertical_Surface_Available)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_B6f = None
def _get_struct_B6f():
    global _struct_B6f
    if _struct_B6f is None:
        _struct_B6f = struct.Struct("<B6f")
    return _struct_B6f

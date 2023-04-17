# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from rospy_message_converter/LineProperty.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import rospy_message_converter.msg

class LineProperty(genpy.Message):
  _md5sum = "21f9656c47061b769a0d7fd3480ec2bd"
  _type = "rospy_message_converter/LineProperty"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """int32 LD_Type
int32 LD_Color
PolyLine LD_Line
float32 LD_Start
float32 LD_End
int32 LD_End_Reason

================================================================================
MSG: rospy_message_converter/PolyLine
float32 line_C0
float32 line_C1
float32 line_C2
float32 line_C3
"""
  __slots__ = ['LD_Type','LD_Color','LD_Line','LD_Start','LD_End','LD_End_Reason']
  _slot_types = ['int32','int32','rospy_message_converter/PolyLine','float32','float32','int32']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       LD_Type,LD_Color,LD_Line,LD_Start,LD_End,LD_End_Reason

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(LineProperty, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.LD_Type is None:
        self.LD_Type = 0
      if self.LD_Color is None:
        self.LD_Color = 0
      if self.LD_Line is None:
        self.LD_Line = rospy_message_converter.msg.PolyLine()
      if self.LD_Start is None:
        self.LD_Start = 0.
      if self.LD_End is None:
        self.LD_End = 0.
      if self.LD_End_Reason is None:
        self.LD_End_Reason = 0
    else:
      self.LD_Type = 0
      self.LD_Color = 0
      self.LD_Line = rospy_message_converter.msg.PolyLine()
      self.LD_Start = 0.
      self.LD_End = 0.
      self.LD_End_Reason = 0

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
      buff.write(_get_struct_2i6fi().pack(_x.LD_Type, _x.LD_Color, _x.LD_Line.line_C0, _x.LD_Line.line_C1, _x.LD_Line.line_C2, _x.LD_Line.line_C3, _x.LD_Start, _x.LD_End, _x.LD_End_Reason))
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
      if self.LD_Line is None:
        self.LD_Line = rospy_message_converter.msg.PolyLine()
      end = 0
      _x = self
      start = end
      end += 36
      (_x.LD_Type, _x.LD_Color, _x.LD_Line.line_C0, _x.LD_Line.line_C1, _x.LD_Line.line_C2, _x.LD_Line.line_C3, _x.LD_Start, _x.LD_End, _x.LD_End_Reason,) = _get_struct_2i6fi().unpack(str[start:end])
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
      buff.write(_get_struct_2i6fi().pack(_x.LD_Type, _x.LD_Color, _x.LD_Line.line_C0, _x.LD_Line.line_C1, _x.LD_Line.line_C2, _x.LD_Line.line_C3, _x.LD_Start, _x.LD_End, _x.LD_End_Reason))
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
      if self.LD_Line is None:
        self.LD_Line = rospy_message_converter.msg.PolyLine()
      end = 0
      _x = self
      start = end
      end += 36
      (_x.LD_Type, _x.LD_Color, _x.LD_Line.line_C0, _x.LD_Line.line_C1, _x.LD_Line.line_C2, _x.LD_Line.line_C3, _x.LD_Start, _x.LD_End, _x.LD_End_Reason,) = _get_struct_2i6fi().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_2i6fi = None
def _get_struct_2i6fi():
    global _struct_2i6fi
    if _struct_2i6fi is None:
        _struct_2i6fi = struct.Struct("<2i6fi")
    return _struct_2i6fi

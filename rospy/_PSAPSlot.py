# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from rospy_message_converter/PSAPSlot.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import rospy_message_converter.msg

class PSAPSlot(genpy.Message):
  _md5sum = "57bb5ef6adef9c88c4b9c8350bc93bbc"
  _type = "rospy_message_converter/PSAPSlot"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """SVCPoint pt1
SVCPoint pt2
SVCPoint pt3
SVCPoint pt4
SVCPoint veh_pos
float32 veh_psi
int32 slot_status

================================================================================
MSG: rospy_message_converter/SVCPoint
float32 x
float32 y
"""
  __slots__ = ['pt1','pt2','pt3','pt4','veh_pos','veh_psi','slot_status']
  _slot_types = ['rospy_message_converter/SVCPoint','rospy_message_converter/SVCPoint','rospy_message_converter/SVCPoint','rospy_message_converter/SVCPoint','rospy_message_converter/SVCPoint','float32','int32']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       pt1,pt2,pt3,pt4,veh_pos,veh_psi,slot_status

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(PSAPSlot, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.pt1 is None:
        self.pt1 = rospy_message_converter.msg.SVCPoint()
      if self.pt2 is None:
        self.pt2 = rospy_message_converter.msg.SVCPoint()
      if self.pt3 is None:
        self.pt3 = rospy_message_converter.msg.SVCPoint()
      if self.pt4 is None:
        self.pt4 = rospy_message_converter.msg.SVCPoint()
      if self.veh_pos is None:
        self.veh_pos = rospy_message_converter.msg.SVCPoint()
      if self.veh_psi is None:
        self.veh_psi = 0.
      if self.slot_status is None:
        self.slot_status = 0
    else:
      self.pt1 = rospy_message_converter.msg.SVCPoint()
      self.pt2 = rospy_message_converter.msg.SVCPoint()
      self.pt3 = rospy_message_converter.msg.SVCPoint()
      self.pt4 = rospy_message_converter.msg.SVCPoint()
      self.veh_pos = rospy_message_converter.msg.SVCPoint()
      self.veh_psi = 0.
      self.slot_status = 0

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
      buff.write(_get_struct_11fi().pack(_x.pt1.x, _x.pt1.y, _x.pt2.x, _x.pt2.y, _x.pt3.x, _x.pt3.y, _x.pt4.x, _x.pt4.y, _x.veh_pos.x, _x.veh_pos.y, _x.veh_psi, _x.slot_status))
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
      if self.pt1 is None:
        self.pt1 = rospy_message_converter.msg.SVCPoint()
      if self.pt2 is None:
        self.pt2 = rospy_message_converter.msg.SVCPoint()
      if self.pt3 is None:
        self.pt3 = rospy_message_converter.msg.SVCPoint()
      if self.pt4 is None:
        self.pt4 = rospy_message_converter.msg.SVCPoint()
      if self.veh_pos is None:
        self.veh_pos = rospy_message_converter.msg.SVCPoint()
      end = 0
      _x = self
      start = end
      end += 48
      (_x.pt1.x, _x.pt1.y, _x.pt2.x, _x.pt2.y, _x.pt3.x, _x.pt3.y, _x.pt4.x, _x.pt4.y, _x.veh_pos.x, _x.veh_pos.y, _x.veh_psi, _x.slot_status,) = _get_struct_11fi().unpack(str[start:end])
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
      buff.write(_get_struct_11fi().pack(_x.pt1.x, _x.pt1.y, _x.pt2.x, _x.pt2.y, _x.pt3.x, _x.pt3.y, _x.pt4.x, _x.pt4.y, _x.veh_pos.x, _x.veh_pos.y, _x.veh_psi, _x.slot_status))
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
      if self.pt1 is None:
        self.pt1 = rospy_message_converter.msg.SVCPoint()
      if self.pt2 is None:
        self.pt2 = rospy_message_converter.msg.SVCPoint()
      if self.pt3 is None:
        self.pt3 = rospy_message_converter.msg.SVCPoint()
      if self.pt4 is None:
        self.pt4 = rospy_message_converter.msg.SVCPoint()
      if self.veh_pos is None:
        self.veh_pos = rospy_message_converter.msg.SVCPoint()
      end = 0
      _x = self
      start = end
      end += 48
      (_x.pt1.x, _x.pt1.y, _x.pt2.x, _x.pt2.y, _x.pt3.x, _x.pt3.y, _x.pt4.x, _x.pt4.y, _x.veh_pos.x, _x.veh_pos.y, _x.veh_psi, _x.slot_status,) = _get_struct_11fi().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_11fi = None
def _get_struct_11fi():
    global _struct_11fi
    if _struct_11fi is None:
        _struct_11fi = struct.Struct("<11fi")
    return _struct_11fi

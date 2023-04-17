# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from rospy_message_converter/ParkSlot.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import rospy_message_converter.msg

class ParkSlot(genpy.Message):
  _md5sum = "a06b3b89c105fd5e705fdeb19ed4874a"
  _type = "rospy_message_converter/ParkSlot"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """SlotBase slot
bool left_corner_exist
ParPoint left_corner_pt1
ParPoint left_corner_pt2
bool right_corner_exist
ParPoint right_corner_pt1
ParPoint right_corner_pt2
bool curb_exist
ParPoint curb_pt1
ParPoint curb_pt2
bool slot_bumper
ParPoint slot_bumper_pt1
ParPoint slot_bumper_pt2
ParPoint left_corner_pt3
ParPoint right_corner_pt3
bool corner_pt3_exist
ParPoint virtual_channel_pt1
ParPoint virtual_channel_pt2
bool virtual_channel_exist
int32 left_corner_type
int32 right_corner_type
uint32 slot_update_count
bool replan_suggest

================================================================================
MSG: rospy_message_converter/SlotBase
int32 hmi_index
int32 svc_index
int32 uss_index
ParPoint pt1
ParPoint pt2
ParPoint pt3
ParPoint pt4
int32 type
int32 source
float32 size_x
float32 size_y
ParPoint VehPos
float32 VehPsi
int32 status
int32 fov
int32 planning_result
float32 slot_angle

================================================================================
MSG: rospy_message_converter/ParPoint
float32 x
float32 y
float32 z
"""
  __slots__ = ['slot','left_corner_exist','left_corner_pt1','left_corner_pt2','right_corner_exist','right_corner_pt1','right_corner_pt2','curb_exist','curb_pt1','curb_pt2','slot_bumper','slot_bumper_pt1','slot_bumper_pt2','left_corner_pt3','right_corner_pt3','corner_pt3_exist','virtual_channel_pt1','virtual_channel_pt2','virtual_channel_exist','left_corner_type','right_corner_type','slot_update_count','replan_suggest']
  _slot_types = ['rospy_message_converter/SlotBase','bool','rospy_message_converter/ParPoint','rospy_message_converter/ParPoint','bool','rospy_message_converter/ParPoint','rospy_message_converter/ParPoint','bool','rospy_message_converter/ParPoint','rospy_message_converter/ParPoint','bool','rospy_message_converter/ParPoint','rospy_message_converter/ParPoint','rospy_message_converter/ParPoint','rospy_message_converter/ParPoint','bool','rospy_message_converter/ParPoint','rospy_message_converter/ParPoint','bool','int32','int32','uint32','bool']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       slot,left_corner_exist,left_corner_pt1,left_corner_pt2,right_corner_exist,right_corner_pt1,right_corner_pt2,curb_exist,curb_pt1,curb_pt2,slot_bumper,slot_bumper_pt1,slot_bumper_pt2,left_corner_pt3,right_corner_pt3,corner_pt3_exist,virtual_channel_pt1,virtual_channel_pt2,virtual_channel_exist,left_corner_type,right_corner_type,slot_update_count,replan_suggest

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(ParkSlot, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.slot is None:
        self.slot = rospy_message_converter.msg.SlotBase()
      if self.left_corner_exist is None:
        self.left_corner_exist = False
      if self.left_corner_pt1 is None:
        self.left_corner_pt1 = rospy_message_converter.msg.ParPoint()
      if self.left_corner_pt2 is None:
        self.left_corner_pt2 = rospy_message_converter.msg.ParPoint()
      if self.right_corner_exist is None:
        self.right_corner_exist = False
      if self.right_corner_pt1 is None:
        self.right_corner_pt1 = rospy_message_converter.msg.ParPoint()
      if self.right_corner_pt2 is None:
        self.right_corner_pt2 = rospy_message_converter.msg.ParPoint()
      if self.curb_exist is None:
        self.curb_exist = False
      if self.curb_pt1 is None:
        self.curb_pt1 = rospy_message_converter.msg.ParPoint()
      if self.curb_pt2 is None:
        self.curb_pt2 = rospy_message_converter.msg.ParPoint()
      if self.slot_bumper is None:
        self.slot_bumper = False
      if self.slot_bumper_pt1 is None:
        self.slot_bumper_pt1 = rospy_message_converter.msg.ParPoint()
      if self.slot_bumper_pt2 is None:
        self.slot_bumper_pt2 = rospy_message_converter.msg.ParPoint()
      if self.left_corner_pt3 is None:
        self.left_corner_pt3 = rospy_message_converter.msg.ParPoint()
      if self.right_corner_pt3 is None:
        self.right_corner_pt3 = rospy_message_converter.msg.ParPoint()
      if self.corner_pt3_exist is None:
        self.corner_pt3_exist = False
      if self.virtual_channel_pt1 is None:
        self.virtual_channel_pt1 = rospy_message_converter.msg.ParPoint()
      if self.virtual_channel_pt2 is None:
        self.virtual_channel_pt2 = rospy_message_converter.msg.ParPoint()
      if self.virtual_channel_exist is None:
        self.virtual_channel_exist = False
      if self.left_corner_type is None:
        self.left_corner_type = 0
      if self.right_corner_type is None:
        self.right_corner_type = 0
      if self.slot_update_count is None:
        self.slot_update_count = 0
      if self.replan_suggest is None:
        self.replan_suggest = False
    else:
      self.slot = rospy_message_converter.msg.SlotBase()
      self.left_corner_exist = False
      self.left_corner_pt1 = rospy_message_converter.msg.ParPoint()
      self.left_corner_pt2 = rospy_message_converter.msg.ParPoint()
      self.right_corner_exist = False
      self.right_corner_pt1 = rospy_message_converter.msg.ParPoint()
      self.right_corner_pt2 = rospy_message_converter.msg.ParPoint()
      self.curb_exist = False
      self.curb_pt1 = rospy_message_converter.msg.ParPoint()
      self.curb_pt2 = rospy_message_converter.msg.ParPoint()
      self.slot_bumper = False
      self.slot_bumper_pt1 = rospy_message_converter.msg.ParPoint()
      self.slot_bumper_pt2 = rospy_message_converter.msg.ParPoint()
      self.left_corner_pt3 = rospy_message_converter.msg.ParPoint()
      self.right_corner_pt3 = rospy_message_converter.msg.ParPoint()
      self.corner_pt3_exist = False
      self.virtual_channel_pt1 = rospy_message_converter.msg.ParPoint()
      self.virtual_channel_pt2 = rospy_message_converter.msg.ParPoint()
      self.virtual_channel_exist = False
      self.left_corner_type = 0
      self.right_corner_type = 0
      self.slot_update_count = 0
      self.replan_suggest = False

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
      buff.write(_get_struct_3i12f2i6f3ifB6fB6fB6fB12fB6fB2iIB().pack(_x.slot.hmi_index, _x.slot.svc_index, _x.slot.uss_index, _x.slot.pt1.x, _x.slot.pt1.y, _x.slot.pt1.z, _x.slot.pt2.x, _x.slot.pt2.y, _x.slot.pt2.z, _x.slot.pt3.x, _x.slot.pt3.y, _x.slot.pt3.z, _x.slot.pt4.x, _x.slot.pt4.y, _x.slot.pt4.z, _x.slot.type, _x.slot.source, _x.slot.size_x, _x.slot.size_y, _x.slot.VehPos.x, _x.slot.VehPos.y, _x.slot.VehPos.z, _x.slot.VehPsi, _x.slot.status, _x.slot.fov, _x.slot.planning_result, _x.slot.slot_angle, _x.left_corner_exist, _x.left_corner_pt1.x, _x.left_corner_pt1.y, _x.left_corner_pt1.z, _x.left_corner_pt2.x, _x.left_corner_pt2.y, _x.left_corner_pt2.z, _x.right_corner_exist, _x.right_corner_pt1.x, _x.right_corner_pt1.y, _x.right_corner_pt1.z, _x.right_corner_pt2.x, _x.right_corner_pt2.y, _x.right_corner_pt2.z, _x.curb_exist, _x.curb_pt1.x, _x.curb_pt1.y, _x.curb_pt1.z, _x.curb_pt2.x, _x.curb_pt2.y, _x.curb_pt2.z, _x.slot_bumper, _x.slot_bumper_pt1.x, _x.slot_bumper_pt1.y, _x.slot_bumper_pt1.z, _x.slot_bumper_pt2.x, _x.slot_bumper_pt2.y, _x.slot_bumper_pt2.z, _x.left_corner_pt3.x, _x.left_corner_pt3.y, _x.left_corner_pt3.z, _x.right_corner_pt3.x, _x.right_corner_pt3.y, _x.right_corner_pt3.z, _x.corner_pt3_exist, _x.virtual_channel_pt1.x, _x.virtual_channel_pt1.y, _x.virtual_channel_pt1.z, _x.virtual_channel_pt2.x, _x.virtual_channel_pt2.y, _x.virtual_channel_pt2.z, _x.virtual_channel_exist, _x.left_corner_type, _x.right_corner_type, _x.slot_update_count, _x.replan_suggest))
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
      if self.slot is None:
        self.slot = rospy_message_converter.msg.SlotBase()
      if self.left_corner_pt1 is None:
        self.left_corner_pt1 = rospy_message_converter.msg.ParPoint()
      if self.left_corner_pt2 is None:
        self.left_corner_pt2 = rospy_message_converter.msg.ParPoint()
      if self.right_corner_pt1 is None:
        self.right_corner_pt1 = rospy_message_converter.msg.ParPoint()
      if self.right_corner_pt2 is None:
        self.right_corner_pt2 = rospy_message_converter.msg.ParPoint()
      if self.curb_pt1 is None:
        self.curb_pt1 = rospy_message_converter.msg.ParPoint()
      if self.curb_pt2 is None:
        self.curb_pt2 = rospy_message_converter.msg.ParPoint()
      if self.slot_bumper_pt1 is None:
        self.slot_bumper_pt1 = rospy_message_converter.msg.ParPoint()
      if self.slot_bumper_pt2 is None:
        self.slot_bumper_pt2 = rospy_message_converter.msg.ParPoint()
      if self.left_corner_pt3 is None:
        self.left_corner_pt3 = rospy_message_converter.msg.ParPoint()
      if self.right_corner_pt3 is None:
        self.right_corner_pt3 = rospy_message_converter.msg.ParPoint()
      if self.virtual_channel_pt1 is None:
        self.virtual_channel_pt1 = rospy_message_converter.msg.ParPoint()
      if self.virtual_channel_pt2 is None:
        self.virtual_channel_pt2 = rospy_message_converter.msg.ParPoint()
      end = 0
      _x = self
      start = end
      end += 271
      (_x.slot.hmi_index, _x.slot.svc_index, _x.slot.uss_index, _x.slot.pt1.x, _x.slot.pt1.y, _x.slot.pt1.z, _x.slot.pt2.x, _x.slot.pt2.y, _x.slot.pt2.z, _x.slot.pt3.x, _x.slot.pt3.y, _x.slot.pt3.z, _x.slot.pt4.x, _x.slot.pt4.y, _x.slot.pt4.z, _x.slot.type, _x.slot.source, _x.slot.size_x, _x.slot.size_y, _x.slot.VehPos.x, _x.slot.VehPos.y, _x.slot.VehPos.z, _x.slot.VehPsi, _x.slot.status, _x.slot.fov, _x.slot.planning_result, _x.slot.slot_angle, _x.left_corner_exist, _x.left_corner_pt1.x, _x.left_corner_pt1.y, _x.left_corner_pt1.z, _x.left_corner_pt2.x, _x.left_corner_pt2.y, _x.left_corner_pt2.z, _x.right_corner_exist, _x.right_corner_pt1.x, _x.right_corner_pt1.y, _x.right_corner_pt1.z, _x.right_corner_pt2.x, _x.right_corner_pt2.y, _x.right_corner_pt2.z, _x.curb_exist, _x.curb_pt1.x, _x.curb_pt1.y, _x.curb_pt1.z, _x.curb_pt2.x, _x.curb_pt2.y, _x.curb_pt2.z, _x.slot_bumper, _x.slot_bumper_pt1.x, _x.slot_bumper_pt1.y, _x.slot_bumper_pt1.z, _x.slot_bumper_pt2.x, _x.slot_bumper_pt2.y, _x.slot_bumper_pt2.z, _x.left_corner_pt3.x, _x.left_corner_pt3.y, _x.left_corner_pt3.z, _x.right_corner_pt3.x, _x.right_corner_pt3.y, _x.right_corner_pt3.z, _x.corner_pt3_exist, _x.virtual_channel_pt1.x, _x.virtual_channel_pt1.y, _x.virtual_channel_pt1.z, _x.virtual_channel_pt2.x, _x.virtual_channel_pt2.y, _x.virtual_channel_pt2.z, _x.virtual_channel_exist, _x.left_corner_type, _x.right_corner_type, _x.slot_update_count, _x.replan_suggest,) = _get_struct_3i12f2i6f3ifB6fB6fB6fB12fB6fB2iIB().unpack(str[start:end])
      self.left_corner_exist = bool(self.left_corner_exist)
      self.right_corner_exist = bool(self.right_corner_exist)
      self.curb_exist = bool(self.curb_exist)
      self.slot_bumper = bool(self.slot_bumper)
      self.corner_pt3_exist = bool(self.corner_pt3_exist)
      self.virtual_channel_exist = bool(self.virtual_channel_exist)
      self.replan_suggest = bool(self.replan_suggest)
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
      buff.write(_get_struct_3i12f2i6f3ifB6fB6fB6fB12fB6fB2iIB().pack(_x.slot.hmi_index, _x.slot.svc_index, _x.slot.uss_index, _x.slot.pt1.x, _x.slot.pt1.y, _x.slot.pt1.z, _x.slot.pt2.x, _x.slot.pt2.y, _x.slot.pt2.z, _x.slot.pt3.x, _x.slot.pt3.y, _x.slot.pt3.z, _x.slot.pt4.x, _x.slot.pt4.y, _x.slot.pt4.z, _x.slot.type, _x.slot.source, _x.slot.size_x, _x.slot.size_y, _x.slot.VehPos.x, _x.slot.VehPos.y, _x.slot.VehPos.z, _x.slot.VehPsi, _x.slot.status, _x.slot.fov, _x.slot.planning_result, _x.slot.slot_angle, _x.left_corner_exist, _x.left_corner_pt1.x, _x.left_corner_pt1.y, _x.left_corner_pt1.z, _x.left_corner_pt2.x, _x.left_corner_pt2.y, _x.left_corner_pt2.z, _x.right_corner_exist, _x.right_corner_pt1.x, _x.right_corner_pt1.y, _x.right_corner_pt1.z, _x.right_corner_pt2.x, _x.right_corner_pt2.y, _x.right_corner_pt2.z, _x.curb_exist, _x.curb_pt1.x, _x.curb_pt1.y, _x.curb_pt1.z, _x.curb_pt2.x, _x.curb_pt2.y, _x.curb_pt2.z, _x.slot_bumper, _x.slot_bumper_pt1.x, _x.slot_bumper_pt1.y, _x.slot_bumper_pt1.z, _x.slot_bumper_pt2.x, _x.slot_bumper_pt2.y, _x.slot_bumper_pt2.z, _x.left_corner_pt3.x, _x.left_corner_pt3.y, _x.left_corner_pt3.z, _x.right_corner_pt3.x, _x.right_corner_pt3.y, _x.right_corner_pt3.z, _x.corner_pt3_exist, _x.virtual_channel_pt1.x, _x.virtual_channel_pt1.y, _x.virtual_channel_pt1.z, _x.virtual_channel_pt2.x, _x.virtual_channel_pt2.y, _x.virtual_channel_pt2.z, _x.virtual_channel_exist, _x.left_corner_type, _x.right_corner_type, _x.slot_update_count, _x.replan_suggest))
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
      if self.slot is None:
        self.slot = rospy_message_converter.msg.SlotBase()
      if self.left_corner_pt1 is None:
        self.left_corner_pt1 = rospy_message_converter.msg.ParPoint()
      if self.left_corner_pt2 is None:
        self.left_corner_pt2 = rospy_message_converter.msg.ParPoint()
      if self.right_corner_pt1 is None:
        self.right_corner_pt1 = rospy_message_converter.msg.ParPoint()
      if self.right_corner_pt2 is None:
        self.right_corner_pt2 = rospy_message_converter.msg.ParPoint()
      if self.curb_pt1 is None:
        self.curb_pt1 = rospy_message_converter.msg.ParPoint()
      if self.curb_pt2 is None:
        self.curb_pt2 = rospy_message_converter.msg.ParPoint()
      if self.slot_bumper_pt1 is None:
        self.slot_bumper_pt1 = rospy_message_converter.msg.ParPoint()
      if self.slot_bumper_pt2 is None:
        self.slot_bumper_pt2 = rospy_message_converter.msg.ParPoint()
      if self.left_corner_pt3 is None:
        self.left_corner_pt3 = rospy_message_converter.msg.ParPoint()
      if self.right_corner_pt3 is None:
        self.right_corner_pt3 = rospy_message_converter.msg.ParPoint()
      if self.virtual_channel_pt1 is None:
        self.virtual_channel_pt1 = rospy_message_converter.msg.ParPoint()
      if self.virtual_channel_pt2 is None:
        self.virtual_channel_pt2 = rospy_message_converter.msg.ParPoint()
      end = 0
      _x = self
      start = end
      end += 271
      (_x.slot.hmi_index, _x.slot.svc_index, _x.slot.uss_index, _x.slot.pt1.x, _x.slot.pt1.y, _x.slot.pt1.z, _x.slot.pt2.x, _x.slot.pt2.y, _x.slot.pt2.z, _x.slot.pt3.x, _x.slot.pt3.y, _x.slot.pt3.z, _x.slot.pt4.x, _x.slot.pt4.y, _x.slot.pt4.z, _x.slot.type, _x.slot.source, _x.slot.size_x, _x.slot.size_y, _x.slot.VehPos.x, _x.slot.VehPos.y, _x.slot.VehPos.z, _x.slot.VehPsi, _x.slot.status, _x.slot.fov, _x.slot.planning_result, _x.slot.slot_angle, _x.left_corner_exist, _x.left_corner_pt1.x, _x.left_corner_pt1.y, _x.left_corner_pt1.z, _x.left_corner_pt2.x, _x.left_corner_pt2.y, _x.left_corner_pt2.z, _x.right_corner_exist, _x.right_corner_pt1.x, _x.right_corner_pt1.y, _x.right_corner_pt1.z, _x.right_corner_pt2.x, _x.right_corner_pt2.y, _x.right_corner_pt2.z, _x.curb_exist, _x.curb_pt1.x, _x.curb_pt1.y, _x.curb_pt1.z, _x.curb_pt2.x, _x.curb_pt2.y, _x.curb_pt2.z, _x.slot_bumper, _x.slot_bumper_pt1.x, _x.slot_bumper_pt1.y, _x.slot_bumper_pt1.z, _x.slot_bumper_pt2.x, _x.slot_bumper_pt2.y, _x.slot_bumper_pt2.z, _x.left_corner_pt3.x, _x.left_corner_pt3.y, _x.left_corner_pt3.z, _x.right_corner_pt3.x, _x.right_corner_pt3.y, _x.right_corner_pt3.z, _x.corner_pt3_exist, _x.virtual_channel_pt1.x, _x.virtual_channel_pt1.y, _x.virtual_channel_pt1.z, _x.virtual_channel_pt2.x, _x.virtual_channel_pt2.y, _x.virtual_channel_pt2.z, _x.virtual_channel_exist, _x.left_corner_type, _x.right_corner_type, _x.slot_update_count, _x.replan_suggest,) = _get_struct_3i12f2i6f3ifB6fB6fB6fB12fB6fB2iIB().unpack(str[start:end])
      self.left_corner_exist = bool(self.left_corner_exist)
      self.right_corner_exist = bool(self.right_corner_exist)
      self.curb_exist = bool(self.curb_exist)
      self.slot_bumper = bool(self.slot_bumper)
      self.corner_pt3_exist = bool(self.corner_pt3_exist)
      self.virtual_channel_exist = bool(self.virtual_channel_exist)
      self.replan_suggest = bool(self.replan_suggest)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_3i12f2i6f3ifB6fB6fB6fB12fB6fB2iIB = None
def _get_struct_3i12f2i6f3ifB6fB6fB6fB12fB6fB2iIB():
    global _struct_3i12f2i6f3ifB6fB6fB6fB12fB6fB2iIB
    if _struct_3i12f2i6f3ifB6fB6fB6fB12fB6fB2iIB is None:
        _struct_3i12f2i6f3ifB6fB6fB6fB12fB6fB2iIB = struct.Struct("<3i12f2i6f3ifB6fB6fB6fB12fB6fB2iIB")
    return _struct_3i12f2i6f3ifB6fB6fB6fB12fB6fB2iIB

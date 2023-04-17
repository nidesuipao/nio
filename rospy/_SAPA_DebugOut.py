# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from rospy_message_converter/SAPA_DebugOut.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class SAPA_DebugOut(genpy.Message):
  _md5sum = "042fb71d34912a5ac646a10626c1d2df"
  _type = "rospy_message_converter/SAPA_DebugOut"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """bool SAPA_is_sapa_enabled
int32 SAPA_slot_type
bool SAPA_is_right_slot
float32 SAPA_tf_base2slot_x
float32 SAPA_tf_base2slot_y
float32 SAPA_tf_base2slot_yaw
bool SAPA_is_pose_init
"""
  __slots__ = ['SAPA_is_sapa_enabled','SAPA_slot_type','SAPA_is_right_slot','SAPA_tf_base2slot_x','SAPA_tf_base2slot_y','SAPA_tf_base2slot_yaw','SAPA_is_pose_init']
  _slot_types = ['bool','int32','bool','float32','float32','float32','bool']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       SAPA_is_sapa_enabled,SAPA_slot_type,SAPA_is_right_slot,SAPA_tf_base2slot_x,SAPA_tf_base2slot_y,SAPA_tf_base2slot_yaw,SAPA_is_pose_init

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(SAPA_DebugOut, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.SAPA_is_sapa_enabled is None:
        self.SAPA_is_sapa_enabled = False
      if self.SAPA_slot_type is None:
        self.SAPA_slot_type = 0
      if self.SAPA_is_right_slot is None:
        self.SAPA_is_right_slot = False
      if self.SAPA_tf_base2slot_x is None:
        self.SAPA_tf_base2slot_x = 0.
      if self.SAPA_tf_base2slot_y is None:
        self.SAPA_tf_base2slot_y = 0.
      if self.SAPA_tf_base2slot_yaw is None:
        self.SAPA_tf_base2slot_yaw = 0.
      if self.SAPA_is_pose_init is None:
        self.SAPA_is_pose_init = False
    else:
      self.SAPA_is_sapa_enabled = False
      self.SAPA_slot_type = 0
      self.SAPA_is_right_slot = False
      self.SAPA_tf_base2slot_x = 0.
      self.SAPA_tf_base2slot_y = 0.
      self.SAPA_tf_base2slot_yaw = 0.
      self.SAPA_is_pose_init = False

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
      buff.write(_get_struct_BiB3fB().pack(_x.SAPA_is_sapa_enabled, _x.SAPA_slot_type, _x.SAPA_is_right_slot, _x.SAPA_tf_base2slot_x, _x.SAPA_tf_base2slot_y, _x.SAPA_tf_base2slot_yaw, _x.SAPA_is_pose_init))
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
      end += 19
      (_x.SAPA_is_sapa_enabled, _x.SAPA_slot_type, _x.SAPA_is_right_slot, _x.SAPA_tf_base2slot_x, _x.SAPA_tf_base2slot_y, _x.SAPA_tf_base2slot_yaw, _x.SAPA_is_pose_init,) = _get_struct_BiB3fB().unpack(str[start:end])
      self.SAPA_is_sapa_enabled = bool(self.SAPA_is_sapa_enabled)
      self.SAPA_is_right_slot = bool(self.SAPA_is_right_slot)
      self.SAPA_is_pose_init = bool(self.SAPA_is_pose_init)
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
      buff.write(_get_struct_BiB3fB().pack(_x.SAPA_is_sapa_enabled, _x.SAPA_slot_type, _x.SAPA_is_right_slot, _x.SAPA_tf_base2slot_x, _x.SAPA_tf_base2slot_y, _x.SAPA_tf_base2slot_yaw, _x.SAPA_is_pose_init))
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
      end += 19
      (_x.SAPA_is_sapa_enabled, _x.SAPA_slot_type, _x.SAPA_is_right_slot, _x.SAPA_tf_base2slot_x, _x.SAPA_tf_base2slot_y, _x.SAPA_tf_base2slot_yaw, _x.SAPA_is_pose_init,) = _get_struct_BiB3fB().unpack(str[start:end])
      self.SAPA_is_sapa_enabled = bool(self.SAPA_is_sapa_enabled)
      self.SAPA_is_right_slot = bool(self.SAPA_is_right_slot)
      self.SAPA_is_pose_init = bool(self.SAPA_is_pose_init)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_BiB3fB = None
def _get_struct_BiB3fB():
    global _struct_BiB3fB
    if _struct_BiB3fB is None:
        _struct_BiB3fB = struct.Struct("<BiB3fB")
    return _struct_BiB3fB

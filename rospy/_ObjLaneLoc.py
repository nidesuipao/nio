# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from rospy_message_converter/ObjLaneLoc.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class ObjLaneLoc(genpy.Message):
  _md5sum = "7dd04ed05c96a128114f094b837de1b0"
  _type = "rospy_message_converter/ObjLaneLoc"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """uint32 lane_index
int32 lane_id
int32 lane_id_debounced
uint32 debounced_cnt
float32 vx_ccs
float32 vy_ccs
float32 dy_ccs
float32 hd_angle_2_lane
float32 dy_min
float32 dy_max
"""
  __slots__ = ['lane_index','lane_id','lane_id_debounced','debounced_cnt','vx_ccs','vy_ccs','dy_ccs','hd_angle_2_lane','dy_min','dy_max']
  _slot_types = ['uint32','int32','int32','uint32','float32','float32','float32','float32','float32','float32']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       lane_index,lane_id,lane_id_debounced,debounced_cnt,vx_ccs,vy_ccs,dy_ccs,hd_angle_2_lane,dy_min,dy_max

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(ObjLaneLoc, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.lane_index is None:
        self.lane_index = 0
      if self.lane_id is None:
        self.lane_id = 0
      if self.lane_id_debounced is None:
        self.lane_id_debounced = 0
      if self.debounced_cnt is None:
        self.debounced_cnt = 0
      if self.vx_ccs is None:
        self.vx_ccs = 0.
      if self.vy_ccs is None:
        self.vy_ccs = 0.
      if self.dy_ccs is None:
        self.dy_ccs = 0.
      if self.hd_angle_2_lane is None:
        self.hd_angle_2_lane = 0.
      if self.dy_min is None:
        self.dy_min = 0.
      if self.dy_max is None:
        self.dy_max = 0.
    else:
      self.lane_index = 0
      self.lane_id = 0
      self.lane_id_debounced = 0
      self.debounced_cnt = 0
      self.vx_ccs = 0.
      self.vy_ccs = 0.
      self.dy_ccs = 0.
      self.hd_angle_2_lane = 0.
      self.dy_min = 0.
      self.dy_max = 0.

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
      buff.write(_get_struct_I2iI6f().pack(_x.lane_index, _x.lane_id, _x.lane_id_debounced, _x.debounced_cnt, _x.vx_ccs, _x.vy_ccs, _x.dy_ccs, _x.hd_angle_2_lane, _x.dy_min, _x.dy_max))
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
      end += 40
      (_x.lane_index, _x.lane_id, _x.lane_id_debounced, _x.debounced_cnt, _x.vx_ccs, _x.vy_ccs, _x.dy_ccs, _x.hd_angle_2_lane, _x.dy_min, _x.dy_max,) = _get_struct_I2iI6f().unpack(str[start:end])
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
      buff.write(_get_struct_I2iI6f().pack(_x.lane_index, _x.lane_id, _x.lane_id_debounced, _x.debounced_cnt, _x.vx_ccs, _x.vy_ccs, _x.dy_ccs, _x.hd_angle_2_lane, _x.dy_min, _x.dy_max))
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
      end += 40
      (_x.lane_index, _x.lane_id, _x.lane_id_debounced, _x.debounced_cnt, _x.vx_ccs, _x.vy_ccs, _x.dy_ccs, _x.hd_angle_2_lane, _x.dy_min, _x.dy_max,) = _get_struct_I2iI6f().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_I2iI6f = None
def _get_struct_I2iI6f():
    global _struct_I2iI6f
    if _struct_I2iI6f is None:
        _struct_I2iI6f = struct.Struct("<I2iI6f")
    return _struct_I2iI6f

# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from rospy_message_converter/FeatureFuncData.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import rospy_message_converter.msg

class FeatureFuncData(genpy.Message):
  _md5sum = "ae278bd2352c8c5c88283ddf20ee2898"
  _type = "rospy_message_converter/FeatureFuncData"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """FeatureFuncConditions conditions
FeatureFuncWti wti
FeatureFuncReqOut req_out

================================================================================
MSG: rospy_message_converter/FeatureFuncConditions
bool req_updated
bool general_enable
bool activate_enable
bool blocked
bool actv_trig
bool deactv_trig
bool control_lost

================================================================================
MSG: rospy_message_converter/FeatureFuncWti
bool trig
uint32 wti

================================================================================
MSG: rospy_message_converter/FeatureFuncReqOut
int32 id
string name
int32 req
"""
  __slots__ = ['conditions','wti','req_out']
  _slot_types = ['rospy_message_converter/FeatureFuncConditions','rospy_message_converter/FeatureFuncWti','rospy_message_converter/FeatureFuncReqOut']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       conditions,wti,req_out

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(FeatureFuncData, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.conditions is None:
        self.conditions = rospy_message_converter.msg.FeatureFuncConditions()
      if self.wti is None:
        self.wti = rospy_message_converter.msg.FeatureFuncWti()
      if self.req_out is None:
        self.req_out = rospy_message_converter.msg.FeatureFuncReqOut()
    else:
      self.conditions = rospy_message_converter.msg.FeatureFuncConditions()
      self.wti = rospy_message_converter.msg.FeatureFuncWti()
      self.req_out = rospy_message_converter.msg.FeatureFuncReqOut()

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
      buff.write(_get_struct_8BIi().pack(_x.conditions.req_updated, _x.conditions.general_enable, _x.conditions.activate_enable, _x.conditions.blocked, _x.conditions.actv_trig, _x.conditions.deactv_trig, _x.conditions.control_lost, _x.wti.trig, _x.wti.wti, _x.req_out.id))
      _x = self.req_out.name
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self.req_out.req
      buff.write(_get_struct_i().pack(_x))
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
      if self.conditions is None:
        self.conditions = rospy_message_converter.msg.FeatureFuncConditions()
      if self.wti is None:
        self.wti = rospy_message_converter.msg.FeatureFuncWti()
      if self.req_out is None:
        self.req_out = rospy_message_converter.msg.FeatureFuncReqOut()
      end = 0
      _x = self
      start = end
      end += 16
      (_x.conditions.req_updated, _x.conditions.general_enable, _x.conditions.activate_enable, _x.conditions.blocked, _x.conditions.actv_trig, _x.conditions.deactv_trig, _x.conditions.control_lost, _x.wti.trig, _x.wti.wti, _x.req_out.id,) = _get_struct_8BIi().unpack(str[start:end])
      self.conditions.req_updated = bool(self.conditions.req_updated)
      self.conditions.general_enable = bool(self.conditions.general_enable)
      self.conditions.activate_enable = bool(self.conditions.activate_enable)
      self.conditions.blocked = bool(self.conditions.blocked)
      self.conditions.actv_trig = bool(self.conditions.actv_trig)
      self.conditions.deactv_trig = bool(self.conditions.deactv_trig)
      self.conditions.control_lost = bool(self.conditions.control_lost)
      self.wti.trig = bool(self.wti.trig)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.req_out.name = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.req_out.name = str[start:end]
      start = end
      end += 4
      (self.req_out.req,) = _get_struct_i().unpack(str[start:end])
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
      buff.write(_get_struct_8BIi().pack(_x.conditions.req_updated, _x.conditions.general_enable, _x.conditions.activate_enable, _x.conditions.blocked, _x.conditions.actv_trig, _x.conditions.deactv_trig, _x.conditions.control_lost, _x.wti.trig, _x.wti.wti, _x.req_out.id))
      _x = self.req_out.name
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self.req_out.req
      buff.write(_get_struct_i().pack(_x))
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
      if self.conditions is None:
        self.conditions = rospy_message_converter.msg.FeatureFuncConditions()
      if self.wti is None:
        self.wti = rospy_message_converter.msg.FeatureFuncWti()
      if self.req_out is None:
        self.req_out = rospy_message_converter.msg.FeatureFuncReqOut()
      end = 0
      _x = self
      start = end
      end += 16
      (_x.conditions.req_updated, _x.conditions.general_enable, _x.conditions.activate_enable, _x.conditions.blocked, _x.conditions.actv_trig, _x.conditions.deactv_trig, _x.conditions.control_lost, _x.wti.trig, _x.wti.wti, _x.req_out.id,) = _get_struct_8BIi().unpack(str[start:end])
      self.conditions.req_updated = bool(self.conditions.req_updated)
      self.conditions.general_enable = bool(self.conditions.general_enable)
      self.conditions.activate_enable = bool(self.conditions.activate_enable)
      self.conditions.blocked = bool(self.conditions.blocked)
      self.conditions.actv_trig = bool(self.conditions.actv_trig)
      self.conditions.deactv_trig = bool(self.conditions.deactv_trig)
      self.conditions.control_lost = bool(self.conditions.control_lost)
      self.wti.trig = bool(self.wti.trig)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.req_out.name = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.req_out.name = str[start:end]
      start = end
      end += 4
      (self.req_out.req,) = _get_struct_i().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_8BIi = None
def _get_struct_8BIi():
    global _struct_8BIi
    if _struct_8BIi is None:
        _struct_8BIi = struct.Struct("<8BIi")
    return _struct_8BIi
_struct_i = None
def _get_struct_i():
    global _struct_i
    if _struct_i is None:
        _struct_i = struct.Struct("<i")
    return _struct_i

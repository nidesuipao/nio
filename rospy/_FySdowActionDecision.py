# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from rospy_message_converter/FySdowActionDecision.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class FySdowActionDecision(genpy.Message):
  _md5sum = "39d5ceae5bdf14cc2781c531e3ac886e"
  _type = "rospy_message_converter/FySdowActionDecision"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """uint32 sdow_decision
uint32 trig_obj_id_left
uint32 trig_obj_id_right
uint32[] reserved
"""
  __slots__ = ['sdow_decision','trig_obj_id_left','trig_obj_id_right','reserved']
  _slot_types = ['uint32','uint32','uint32','uint32[]']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       sdow_decision,trig_obj_id_left,trig_obj_id_right,reserved

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(FySdowActionDecision, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.sdow_decision is None:
        self.sdow_decision = 0
      if self.trig_obj_id_left is None:
        self.trig_obj_id_left = 0
      if self.trig_obj_id_right is None:
        self.trig_obj_id_right = 0
      if self.reserved is None:
        self.reserved = []
    else:
      self.sdow_decision = 0
      self.trig_obj_id_left = 0
      self.trig_obj_id_right = 0
      self.reserved = []

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
      buff.write(_get_struct_3I().pack(_x.sdow_decision, _x.trig_obj_id_left, _x.trig_obj_id_right))
      length = len(self.reserved)
      buff.write(_struct_I.pack(length))
      pattern = '<%sI'%length
      buff.write(struct.Struct(pattern).pack(*self.reserved))
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
      end += 12
      (_x.sdow_decision, _x.trig_obj_id_left, _x.trig_obj_id_right,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sI'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.reserved = s.unpack(str[start:end])
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
      buff.write(_get_struct_3I().pack(_x.sdow_decision, _x.trig_obj_id_left, _x.trig_obj_id_right))
      length = len(self.reserved)
      buff.write(_struct_I.pack(length))
      pattern = '<%sI'%length
      buff.write(self.reserved.tostring())
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
      end += 12
      (_x.sdow_decision, _x.trig_obj_id_left, _x.trig_obj_id_right,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sI'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.reserved = numpy.frombuffer(str[start:end], dtype=numpy.uint32, count=length)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_3I = None
def _get_struct_3I():
    global _struct_3I
    if _struct_3I is None:
        _struct_3I = struct.Struct("<3I")
    return _struct_3I

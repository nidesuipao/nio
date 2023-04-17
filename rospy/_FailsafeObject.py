# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from rospy_message_converter/FailsafeObject.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class FailsafeObject(genpy.Message):
  _md5sum = "5e8f367e70e1d4d3e557e6ca0cd72afe"
  _type = "rospy_message_converter/FailsafeObject"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """uint32 full_blockage_pred
float32 full_blockage_score
uint32 low_sun_pred
float32 low_sun_score
uint32 partial_blockage_pred
float32 partial_blockage_score
uint32 rain_pred
float32 rain_score
uint32 windshield_frozen_pred
float32 windshield_frozen_score
"""
  __slots__ = ['full_blockage_pred','full_blockage_score','low_sun_pred','low_sun_score','partial_blockage_pred','partial_blockage_score','rain_pred','rain_score','windshield_frozen_pred','windshield_frozen_score']
  _slot_types = ['uint32','float32','uint32','float32','uint32','float32','uint32','float32','uint32','float32']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       full_blockage_pred,full_blockage_score,low_sun_pred,low_sun_score,partial_blockage_pred,partial_blockage_score,rain_pred,rain_score,windshield_frozen_pred,windshield_frozen_score

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(FailsafeObject, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.full_blockage_pred is None:
        self.full_blockage_pred = 0
      if self.full_blockage_score is None:
        self.full_blockage_score = 0.
      if self.low_sun_pred is None:
        self.low_sun_pred = 0
      if self.low_sun_score is None:
        self.low_sun_score = 0.
      if self.partial_blockage_pred is None:
        self.partial_blockage_pred = 0
      if self.partial_blockage_score is None:
        self.partial_blockage_score = 0.
      if self.rain_pred is None:
        self.rain_pred = 0
      if self.rain_score is None:
        self.rain_score = 0.
      if self.windshield_frozen_pred is None:
        self.windshield_frozen_pred = 0
      if self.windshield_frozen_score is None:
        self.windshield_frozen_score = 0.
    else:
      self.full_blockage_pred = 0
      self.full_blockage_score = 0.
      self.low_sun_pred = 0
      self.low_sun_score = 0.
      self.partial_blockage_pred = 0
      self.partial_blockage_score = 0.
      self.rain_pred = 0
      self.rain_score = 0.
      self.windshield_frozen_pred = 0
      self.windshield_frozen_score = 0.

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
      buff.write(_get_struct_IfIfIfIfIf().pack(_x.full_blockage_pred, _x.full_blockage_score, _x.low_sun_pred, _x.low_sun_score, _x.partial_blockage_pred, _x.partial_blockage_score, _x.rain_pred, _x.rain_score, _x.windshield_frozen_pred, _x.windshield_frozen_score))
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
      (_x.full_blockage_pred, _x.full_blockage_score, _x.low_sun_pred, _x.low_sun_score, _x.partial_blockage_pred, _x.partial_blockage_score, _x.rain_pred, _x.rain_score, _x.windshield_frozen_pred, _x.windshield_frozen_score,) = _get_struct_IfIfIfIfIf().unpack(str[start:end])
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
      buff.write(_get_struct_IfIfIfIfIf().pack(_x.full_blockage_pred, _x.full_blockage_score, _x.low_sun_pred, _x.low_sun_score, _x.partial_blockage_pred, _x.partial_blockage_score, _x.rain_pred, _x.rain_score, _x.windshield_frozen_pred, _x.windshield_frozen_score))
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
      (_x.full_blockage_pred, _x.full_blockage_score, _x.low_sun_pred, _x.low_sun_score, _x.partial_blockage_pred, _x.partial_blockage_score, _x.rain_pred, _x.rain_score, _x.windshield_frozen_pred, _x.windshield_frozen_score,) = _get_struct_IfIfIfIfIf().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_IfIfIfIfIf = None
def _get_struct_IfIfIfIfIf():
    global _struct_IfIfIfIfIf
    if _struct_IfIfIfIfIf is None:
        _struct_IfIfIfIfIf = struct.Struct("<IfIfIfIfIf")
    return _struct_IfIfIfIfIf

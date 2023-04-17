# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from rospy_message_converter/ParkingEvent.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class ParkingEvent(genpy.Message):
  _md5sum = "2e7c0c0121188c6bfb86c1c626d2ab85"
  _type = "rospy_message_converter/ParkingEvent"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """bool psap_event_trigger
bool sapa_event_trigger
uint32 pasp_event_type
uint32 sapa_event_type
uint32[] buffer
"""
  __slots__ = ['psap_event_trigger','sapa_event_trigger','pasp_event_type','sapa_event_type','buffer']
  _slot_types = ['bool','bool','uint32','uint32','uint32[]']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       psap_event_trigger,sapa_event_trigger,pasp_event_type,sapa_event_type,buffer

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(ParkingEvent, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.psap_event_trigger is None:
        self.psap_event_trigger = False
      if self.sapa_event_trigger is None:
        self.sapa_event_trigger = False
      if self.pasp_event_type is None:
        self.pasp_event_type = 0
      if self.sapa_event_type is None:
        self.sapa_event_type = 0
      if self.buffer is None:
        self.buffer = []
    else:
      self.psap_event_trigger = False
      self.sapa_event_trigger = False
      self.pasp_event_type = 0
      self.sapa_event_type = 0
      self.buffer = []

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
      buff.write(_get_struct_2B2I().pack(_x.psap_event_trigger, _x.sapa_event_trigger, _x.pasp_event_type, _x.sapa_event_type))
      length = len(self.buffer)
      buff.write(_struct_I.pack(length))
      pattern = '<%sI'%length
      buff.write(struct.Struct(pattern).pack(*self.buffer))
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
      end += 10
      (_x.psap_event_trigger, _x.sapa_event_trigger, _x.pasp_event_type, _x.sapa_event_type,) = _get_struct_2B2I().unpack(str[start:end])
      self.psap_event_trigger = bool(self.psap_event_trigger)
      self.sapa_event_trigger = bool(self.sapa_event_trigger)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sI'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.buffer = s.unpack(str[start:end])
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
      buff.write(_get_struct_2B2I().pack(_x.psap_event_trigger, _x.sapa_event_trigger, _x.pasp_event_type, _x.sapa_event_type))
      length = len(self.buffer)
      buff.write(_struct_I.pack(length))
      pattern = '<%sI'%length
      buff.write(self.buffer.tostring())
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
      end += 10
      (_x.psap_event_trigger, _x.sapa_event_trigger, _x.pasp_event_type, _x.sapa_event_type,) = _get_struct_2B2I().unpack(str[start:end])
      self.psap_event_trigger = bool(self.psap_event_trigger)
      self.sapa_event_trigger = bool(self.sapa_event_trigger)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sI'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.buffer = numpy.frombuffer(str[start:end], dtype=numpy.uint32, count=length)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_2B2I = None
def _get_struct_2B2I():
    global _struct_2B2I
    if _struct_2B2I is None:
        _struct_2B2I = struct.Struct("<2B2I")
    return _struct_2B2I

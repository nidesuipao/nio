# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from rospy_message_converter/SdReservedSpace.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class SdReservedSpace(genpy.Message):
  _md5sum = "73ed178a95f446a566cace59feaeb2db"
  _type = "rospy_message_converter/SdReservedSpace"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """bool[] sd_boolReserve
uint32[] sd_intReserve
float32[] sd_floatReserve
"""
  __slots__ = ['sd_boolReserve','sd_intReserve','sd_floatReserve']
  _slot_types = ['bool[]','uint32[]','float32[]']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       sd_boolReserve,sd_intReserve,sd_floatReserve

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(SdReservedSpace, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.sd_boolReserve is None:
        self.sd_boolReserve = []
      if self.sd_intReserve is None:
        self.sd_intReserve = []
      if self.sd_floatReserve is None:
        self.sd_floatReserve = []
    else:
      self.sd_boolReserve = []
      self.sd_intReserve = []
      self.sd_floatReserve = []

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
      length = len(self.sd_boolReserve)
      buff.write(_struct_I.pack(length))
      pattern = '<%sB'%length
      buff.write(struct.Struct(pattern).pack(*self.sd_boolReserve))
      length = len(self.sd_intReserve)
      buff.write(_struct_I.pack(length))
      pattern = '<%sI'%length
      buff.write(struct.Struct(pattern).pack(*self.sd_intReserve))
      length = len(self.sd_floatReserve)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(struct.Struct(pattern).pack(*self.sd_floatReserve))
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
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sB'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.sd_boolReserve = s.unpack(str[start:end])
      self.sd_boolReserve = list(map(bool, self.sd_boolReserve))
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sI'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.sd_intReserve = s.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sf'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.sd_floatReserve = s.unpack(str[start:end])
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
      length = len(self.sd_boolReserve)
      buff.write(_struct_I.pack(length))
      pattern = '<%sB'%length
      buff.write(self.sd_boolReserve.tostring())
      length = len(self.sd_intReserve)
      buff.write(_struct_I.pack(length))
      pattern = '<%sI'%length
      buff.write(self.sd_intReserve.tostring())
      length = len(self.sd_floatReserve)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(self.sd_floatReserve.tostring())
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
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sB'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.sd_boolReserve = numpy.frombuffer(str[start:end], dtype=numpy.bool, count=length)
      self.sd_boolReserve = list(map(bool, self.sd_boolReserve))
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sI'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.sd_intReserve = numpy.frombuffer(str[start:end], dtype=numpy.uint32, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sf'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.sd_floatReserve = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=length)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I

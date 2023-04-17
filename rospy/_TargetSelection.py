# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from rospy_message_converter/TargetSelection.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class TargetSelection(genpy.Message):
  _md5sum = "8fddeffcc661aa3d2ec548db31719ac1"
  _type = "rospy_message_converter/TargetSelection"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """uint32[] acc_tar
uint32 aeb_tar
uint32 aeb_conf
"""
  __slots__ = ['acc_tar','aeb_tar','aeb_conf']
  _slot_types = ['uint32[]','uint32','uint32']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       acc_tar,aeb_tar,aeb_conf

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(TargetSelection, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.acc_tar is None:
        self.acc_tar = []
      if self.aeb_tar is None:
        self.aeb_tar = 0
      if self.aeb_conf is None:
        self.aeb_conf = 0
    else:
      self.acc_tar = []
      self.aeb_tar = 0
      self.aeb_conf = 0

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
      length = len(self.acc_tar)
      buff.write(_struct_I.pack(length))
      pattern = '<%sI'%length
      buff.write(struct.Struct(pattern).pack(*self.acc_tar))
      _x = self
      buff.write(_get_struct_2I().pack(_x.aeb_tar, _x.aeb_conf))
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
      pattern = '<%sI'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.acc_tar = s.unpack(str[start:end])
      _x = self
      start = end
      end += 8
      (_x.aeb_tar, _x.aeb_conf,) = _get_struct_2I().unpack(str[start:end])
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
      length = len(self.acc_tar)
      buff.write(_struct_I.pack(length))
      pattern = '<%sI'%length
      buff.write(self.acc_tar.tostring())
      _x = self
      buff.write(_get_struct_2I().pack(_x.aeb_tar, _x.aeb_conf))
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
      pattern = '<%sI'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.acc_tar = numpy.frombuffer(str[start:end], dtype=numpy.uint32, count=length)
      _x = self
      start = end
      end += 8
      (_x.aeb_tar, _x.aeb_conf,) = _get_struct_2I().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_2I = None
def _get_struct_2I():
    global _struct_2I
    if _struct_2I is None:
        _struct_2I = struct.Struct("<2I")
    return _struct_2I

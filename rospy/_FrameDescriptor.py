# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from rospy_message_converter/FrameDescriptor.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class FrameDescriptor(genpy.Message):
  _md5sum = "d1650f8b27ba9bddf41dfb49b87c862a"
  _type = "rospy_message_converter/FrameDescriptor"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """int32[] cids
float32[] scores
int32[] sub_cids
float32[] sub_scores
float32[] embeddings
"""
  __slots__ = ['cids','scores','sub_cids','sub_scores','embeddings']
  _slot_types = ['int32[]','float32[]','int32[]','float32[]','float32[]']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       cids,scores,sub_cids,sub_scores,embeddings

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(FrameDescriptor, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.cids is None:
        self.cids = []
      if self.scores is None:
        self.scores = []
      if self.sub_cids is None:
        self.sub_cids = []
      if self.sub_scores is None:
        self.sub_scores = []
      if self.embeddings is None:
        self.embeddings = []
    else:
      self.cids = []
      self.scores = []
      self.sub_cids = []
      self.sub_scores = []
      self.embeddings = []

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
      length = len(self.cids)
      buff.write(_struct_I.pack(length))
      pattern = '<%si'%length
      buff.write(struct.Struct(pattern).pack(*self.cids))
      length = len(self.scores)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(struct.Struct(pattern).pack(*self.scores))
      length = len(self.sub_cids)
      buff.write(_struct_I.pack(length))
      pattern = '<%si'%length
      buff.write(struct.Struct(pattern).pack(*self.sub_cids))
      length = len(self.sub_scores)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(struct.Struct(pattern).pack(*self.sub_scores))
      length = len(self.embeddings)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(struct.Struct(pattern).pack(*self.embeddings))
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
      pattern = '<%si'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.cids = s.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sf'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.scores = s.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%si'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.sub_cids = s.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sf'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.sub_scores = s.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sf'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.embeddings = s.unpack(str[start:end])
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
      length = len(self.cids)
      buff.write(_struct_I.pack(length))
      pattern = '<%si'%length
      buff.write(self.cids.tostring())
      length = len(self.scores)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(self.scores.tostring())
      length = len(self.sub_cids)
      buff.write(_struct_I.pack(length))
      pattern = '<%si'%length
      buff.write(self.sub_cids.tostring())
      length = len(self.sub_scores)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(self.sub_scores.tostring())
      length = len(self.embeddings)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(self.embeddings.tostring())
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
      pattern = '<%si'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.cids = numpy.frombuffer(str[start:end], dtype=numpy.int32, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sf'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.scores = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%si'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.sub_cids = numpy.frombuffer(str[start:end], dtype=numpy.int32, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sf'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.sub_scores = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sf'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.embeddings = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=length)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I

# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from rospy_message_converter/ObjRelevanceStru.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import rospy_message_converter.msg

class ObjRelevanceStru(genpy.Message):
  _md5sum = "cd5b7afad735ef089053909140cfeda0"
  _type = "rospy_message_converter/ObjRelevanceStru"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """uint32 id
float32 tClose
float32 rangeClose
float32 objSensorErrorExt
float32 objSensorFluctExt
float32 egoFrontEndExt
float32 egoWidthExt
float32 overlapRate
bool flgOverlap
float32 collisionRelevance
ObjBoxStru egoBoxBase
ObjBoxStru egoBoxLengthExt
ObjBoxStru egoBoxExt
ObjBoxStru objBoxBase
ObjBoxStru ObjBoxExt
float32[] reserved
float32 objSensorTotalExt

================================================================================
MSG: rospy_message_converter/ObjBoxStru
float32[] x
float32[] y
float32[] reserved
"""
  __slots__ = ['id','tClose','rangeClose','objSensorErrorExt','objSensorFluctExt','egoFrontEndExt','egoWidthExt','overlapRate','flgOverlap','collisionRelevance','egoBoxBase','egoBoxLengthExt','egoBoxExt','objBoxBase','ObjBoxExt','reserved','objSensorTotalExt']
  _slot_types = ['uint32','float32','float32','float32','float32','float32','float32','float32','bool','float32','rospy_message_converter/ObjBoxStru','rospy_message_converter/ObjBoxStru','rospy_message_converter/ObjBoxStru','rospy_message_converter/ObjBoxStru','rospy_message_converter/ObjBoxStru','float32[]','float32']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       id,tClose,rangeClose,objSensorErrorExt,objSensorFluctExt,egoFrontEndExt,egoWidthExt,overlapRate,flgOverlap,collisionRelevance,egoBoxBase,egoBoxLengthExt,egoBoxExt,objBoxBase,ObjBoxExt,reserved,objSensorTotalExt

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(ObjRelevanceStru, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.id is None:
        self.id = 0
      if self.tClose is None:
        self.tClose = 0.
      if self.rangeClose is None:
        self.rangeClose = 0.
      if self.objSensorErrorExt is None:
        self.objSensorErrorExt = 0.
      if self.objSensorFluctExt is None:
        self.objSensorFluctExt = 0.
      if self.egoFrontEndExt is None:
        self.egoFrontEndExt = 0.
      if self.egoWidthExt is None:
        self.egoWidthExt = 0.
      if self.overlapRate is None:
        self.overlapRate = 0.
      if self.flgOverlap is None:
        self.flgOverlap = False
      if self.collisionRelevance is None:
        self.collisionRelevance = 0.
      if self.egoBoxBase is None:
        self.egoBoxBase = rospy_message_converter.msg.ObjBoxStru()
      if self.egoBoxLengthExt is None:
        self.egoBoxLengthExt = rospy_message_converter.msg.ObjBoxStru()
      if self.egoBoxExt is None:
        self.egoBoxExt = rospy_message_converter.msg.ObjBoxStru()
      if self.objBoxBase is None:
        self.objBoxBase = rospy_message_converter.msg.ObjBoxStru()
      if self.ObjBoxExt is None:
        self.ObjBoxExt = rospy_message_converter.msg.ObjBoxStru()
      if self.reserved is None:
        self.reserved = []
      if self.objSensorTotalExt is None:
        self.objSensorTotalExt = 0.
    else:
      self.id = 0
      self.tClose = 0.
      self.rangeClose = 0.
      self.objSensorErrorExt = 0.
      self.objSensorFluctExt = 0.
      self.egoFrontEndExt = 0.
      self.egoWidthExt = 0.
      self.overlapRate = 0.
      self.flgOverlap = False
      self.collisionRelevance = 0.
      self.egoBoxBase = rospy_message_converter.msg.ObjBoxStru()
      self.egoBoxLengthExt = rospy_message_converter.msg.ObjBoxStru()
      self.egoBoxExt = rospy_message_converter.msg.ObjBoxStru()
      self.objBoxBase = rospy_message_converter.msg.ObjBoxStru()
      self.ObjBoxExt = rospy_message_converter.msg.ObjBoxStru()
      self.reserved = []
      self.objSensorTotalExt = 0.

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
      buff.write(_get_struct_I7fBf().pack(_x.id, _x.tClose, _x.rangeClose, _x.objSensorErrorExt, _x.objSensorFluctExt, _x.egoFrontEndExt, _x.egoWidthExt, _x.overlapRate, _x.flgOverlap, _x.collisionRelevance))
      length = len(self.egoBoxBase.x)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(struct.Struct(pattern).pack(*self.egoBoxBase.x))
      length = len(self.egoBoxBase.y)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(struct.Struct(pattern).pack(*self.egoBoxBase.y))
      length = len(self.egoBoxBase.reserved)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(struct.Struct(pattern).pack(*self.egoBoxBase.reserved))
      length = len(self.egoBoxLengthExt.x)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(struct.Struct(pattern).pack(*self.egoBoxLengthExt.x))
      length = len(self.egoBoxLengthExt.y)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(struct.Struct(pattern).pack(*self.egoBoxLengthExt.y))
      length = len(self.egoBoxLengthExt.reserved)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(struct.Struct(pattern).pack(*self.egoBoxLengthExt.reserved))
      length = len(self.egoBoxExt.x)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(struct.Struct(pattern).pack(*self.egoBoxExt.x))
      length = len(self.egoBoxExt.y)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(struct.Struct(pattern).pack(*self.egoBoxExt.y))
      length = len(self.egoBoxExt.reserved)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(struct.Struct(pattern).pack(*self.egoBoxExt.reserved))
      length = len(self.objBoxBase.x)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(struct.Struct(pattern).pack(*self.objBoxBase.x))
      length = len(self.objBoxBase.y)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(struct.Struct(pattern).pack(*self.objBoxBase.y))
      length = len(self.objBoxBase.reserved)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(struct.Struct(pattern).pack(*self.objBoxBase.reserved))
      length = len(self.ObjBoxExt.x)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(struct.Struct(pattern).pack(*self.ObjBoxExt.x))
      length = len(self.ObjBoxExt.y)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(struct.Struct(pattern).pack(*self.ObjBoxExt.y))
      length = len(self.ObjBoxExt.reserved)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(struct.Struct(pattern).pack(*self.ObjBoxExt.reserved))
      length = len(self.reserved)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(struct.Struct(pattern).pack(*self.reserved))
      _x = self.objSensorTotalExt
      buff.write(_get_struct_f().pack(_x))
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
      if self.egoBoxBase is None:
        self.egoBoxBase = rospy_message_converter.msg.ObjBoxStru()
      if self.egoBoxLengthExt is None:
        self.egoBoxLengthExt = rospy_message_converter.msg.ObjBoxStru()
      if self.egoBoxExt is None:
        self.egoBoxExt = rospy_message_converter.msg.ObjBoxStru()
      if self.objBoxBase is None:
        self.objBoxBase = rospy_message_converter.msg.ObjBoxStru()
      if self.ObjBoxExt is None:
        self.ObjBoxExt = rospy_message_converter.msg.ObjBoxStru()
      end = 0
      _x = self
      start = end
      end += 37
      (_x.id, _x.tClose, _x.rangeClose, _x.objSensorErrorExt, _x.objSensorFluctExt, _x.egoFrontEndExt, _x.egoWidthExt, _x.overlapRate, _x.flgOverlap, _x.collisionRelevance,) = _get_struct_I7fBf().unpack(str[start:end])
      self.flgOverlap = bool(self.flgOverlap)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sf'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.egoBoxBase.x = s.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sf'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.egoBoxBase.y = s.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sf'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.egoBoxBase.reserved = s.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sf'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.egoBoxLengthExt.x = s.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sf'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.egoBoxLengthExt.y = s.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sf'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.egoBoxLengthExt.reserved = s.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sf'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.egoBoxExt.x = s.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sf'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.egoBoxExt.y = s.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sf'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.egoBoxExt.reserved = s.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sf'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.objBoxBase.x = s.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sf'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.objBoxBase.y = s.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sf'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.objBoxBase.reserved = s.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sf'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.ObjBoxExt.x = s.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sf'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.ObjBoxExt.y = s.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sf'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.ObjBoxExt.reserved = s.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sf'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.reserved = s.unpack(str[start:end])
      start = end
      end += 4
      (self.objSensorTotalExt,) = _get_struct_f().unpack(str[start:end])
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
      buff.write(_get_struct_I7fBf().pack(_x.id, _x.tClose, _x.rangeClose, _x.objSensorErrorExt, _x.objSensorFluctExt, _x.egoFrontEndExt, _x.egoWidthExt, _x.overlapRate, _x.flgOverlap, _x.collisionRelevance))
      length = len(self.egoBoxBase.x)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(self.egoBoxBase.x.tostring())
      length = len(self.egoBoxBase.y)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(self.egoBoxBase.y.tostring())
      length = len(self.egoBoxBase.reserved)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(self.egoBoxBase.reserved.tostring())
      length = len(self.egoBoxLengthExt.x)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(self.egoBoxLengthExt.x.tostring())
      length = len(self.egoBoxLengthExt.y)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(self.egoBoxLengthExt.y.tostring())
      length = len(self.egoBoxLengthExt.reserved)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(self.egoBoxLengthExt.reserved.tostring())
      length = len(self.egoBoxExt.x)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(self.egoBoxExt.x.tostring())
      length = len(self.egoBoxExt.y)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(self.egoBoxExt.y.tostring())
      length = len(self.egoBoxExt.reserved)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(self.egoBoxExt.reserved.tostring())
      length = len(self.objBoxBase.x)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(self.objBoxBase.x.tostring())
      length = len(self.objBoxBase.y)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(self.objBoxBase.y.tostring())
      length = len(self.objBoxBase.reserved)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(self.objBoxBase.reserved.tostring())
      length = len(self.ObjBoxExt.x)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(self.ObjBoxExt.x.tostring())
      length = len(self.ObjBoxExt.y)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(self.ObjBoxExt.y.tostring())
      length = len(self.ObjBoxExt.reserved)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(self.ObjBoxExt.reserved.tostring())
      length = len(self.reserved)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(self.reserved.tostring())
      _x = self.objSensorTotalExt
      buff.write(_get_struct_f().pack(_x))
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
      if self.egoBoxBase is None:
        self.egoBoxBase = rospy_message_converter.msg.ObjBoxStru()
      if self.egoBoxLengthExt is None:
        self.egoBoxLengthExt = rospy_message_converter.msg.ObjBoxStru()
      if self.egoBoxExt is None:
        self.egoBoxExt = rospy_message_converter.msg.ObjBoxStru()
      if self.objBoxBase is None:
        self.objBoxBase = rospy_message_converter.msg.ObjBoxStru()
      if self.ObjBoxExt is None:
        self.ObjBoxExt = rospy_message_converter.msg.ObjBoxStru()
      end = 0
      _x = self
      start = end
      end += 37
      (_x.id, _x.tClose, _x.rangeClose, _x.objSensorErrorExt, _x.objSensorFluctExt, _x.egoFrontEndExt, _x.egoWidthExt, _x.overlapRate, _x.flgOverlap, _x.collisionRelevance,) = _get_struct_I7fBf().unpack(str[start:end])
      self.flgOverlap = bool(self.flgOverlap)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sf'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.egoBoxBase.x = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sf'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.egoBoxBase.y = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sf'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.egoBoxBase.reserved = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sf'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.egoBoxLengthExt.x = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sf'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.egoBoxLengthExt.y = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sf'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.egoBoxLengthExt.reserved = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sf'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.egoBoxExt.x = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sf'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.egoBoxExt.y = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sf'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.egoBoxExt.reserved = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sf'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.objBoxBase.x = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sf'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.objBoxBase.y = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sf'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.objBoxBase.reserved = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sf'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.ObjBoxExt.x = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sf'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.ObjBoxExt.y = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sf'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.ObjBoxExt.reserved = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sf'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.reserved = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=length)
      start = end
      end += 4
      (self.objSensorTotalExt,) = _get_struct_f().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_I7fBf = None
def _get_struct_I7fBf():
    global _struct_I7fBf
    if _struct_I7fBf is None:
        _struct_I7fBf = struct.Struct("<I7fBf")
    return _struct_I7fBf
_struct_f = None
def _get_struct_f():
    global _struct_f
    if _struct_f is None:
        _struct_f = struct.Struct("<f")
    return _struct_f

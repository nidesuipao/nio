# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from rospy_message_converter/CarRelevanceMonitorStru.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class CarRelevanceMonitorStru(genpy.Message):
  _md5sum = "16e1ecd986818e9704754e5582cdef49"
  _type = "rospy_message_converter/CarRelevanceMonitorStru"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """uint32 id
uint32 type
uint32 laneLoc
float32 curThw
float32 ttcLgt
float32 tFuture
float32 futRelevance
float32 curLgtDistCorr
float32 curLatDistCorr
float32 futLgtDistCorr
float32 futLatDistCorr
float32 futPosRelevance
float32 corridorHalfWidth
float32 adjLaneBoundary
float32 curPoseLgtDist
float32 curPoseLatDist
float32 curPoseRange
float32 curPoseHeading
float32 futPoseLgtDist
float32 futPoseLatDist
float32 futPoseRange
float32 futPoseHeading
"""
  __slots__ = ['id','type','laneLoc','curThw','ttcLgt','tFuture','futRelevance','curLgtDistCorr','curLatDistCorr','futLgtDistCorr','futLatDistCorr','futPosRelevance','corridorHalfWidth','adjLaneBoundary','curPoseLgtDist','curPoseLatDist','curPoseRange','curPoseHeading','futPoseLgtDist','futPoseLatDist','futPoseRange','futPoseHeading']
  _slot_types = ['uint32','uint32','uint32','float32','float32','float32','float32','float32','float32','float32','float32','float32','float32','float32','float32','float32','float32','float32','float32','float32','float32','float32']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       id,type,laneLoc,curThw,ttcLgt,tFuture,futRelevance,curLgtDistCorr,curLatDistCorr,futLgtDistCorr,futLatDistCorr,futPosRelevance,corridorHalfWidth,adjLaneBoundary,curPoseLgtDist,curPoseLatDist,curPoseRange,curPoseHeading,futPoseLgtDist,futPoseLatDist,futPoseRange,futPoseHeading

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(CarRelevanceMonitorStru, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.id is None:
        self.id = 0
      if self.type is None:
        self.type = 0
      if self.laneLoc is None:
        self.laneLoc = 0
      if self.curThw is None:
        self.curThw = 0.
      if self.ttcLgt is None:
        self.ttcLgt = 0.
      if self.tFuture is None:
        self.tFuture = 0.
      if self.futRelevance is None:
        self.futRelevance = 0.
      if self.curLgtDistCorr is None:
        self.curLgtDistCorr = 0.
      if self.curLatDistCorr is None:
        self.curLatDistCorr = 0.
      if self.futLgtDistCorr is None:
        self.futLgtDistCorr = 0.
      if self.futLatDistCorr is None:
        self.futLatDistCorr = 0.
      if self.futPosRelevance is None:
        self.futPosRelevance = 0.
      if self.corridorHalfWidth is None:
        self.corridorHalfWidth = 0.
      if self.adjLaneBoundary is None:
        self.adjLaneBoundary = 0.
      if self.curPoseLgtDist is None:
        self.curPoseLgtDist = 0.
      if self.curPoseLatDist is None:
        self.curPoseLatDist = 0.
      if self.curPoseRange is None:
        self.curPoseRange = 0.
      if self.curPoseHeading is None:
        self.curPoseHeading = 0.
      if self.futPoseLgtDist is None:
        self.futPoseLgtDist = 0.
      if self.futPoseLatDist is None:
        self.futPoseLatDist = 0.
      if self.futPoseRange is None:
        self.futPoseRange = 0.
      if self.futPoseHeading is None:
        self.futPoseHeading = 0.
    else:
      self.id = 0
      self.type = 0
      self.laneLoc = 0
      self.curThw = 0.
      self.ttcLgt = 0.
      self.tFuture = 0.
      self.futRelevance = 0.
      self.curLgtDistCorr = 0.
      self.curLatDistCorr = 0.
      self.futLgtDistCorr = 0.
      self.futLatDistCorr = 0.
      self.futPosRelevance = 0.
      self.corridorHalfWidth = 0.
      self.adjLaneBoundary = 0.
      self.curPoseLgtDist = 0.
      self.curPoseLatDist = 0.
      self.curPoseRange = 0.
      self.curPoseHeading = 0.
      self.futPoseLgtDist = 0.
      self.futPoseLatDist = 0.
      self.futPoseRange = 0.
      self.futPoseHeading = 0.

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
      buff.write(_get_struct_3I19f().pack(_x.id, _x.type, _x.laneLoc, _x.curThw, _x.ttcLgt, _x.tFuture, _x.futRelevance, _x.curLgtDistCorr, _x.curLatDistCorr, _x.futLgtDistCorr, _x.futLatDistCorr, _x.futPosRelevance, _x.corridorHalfWidth, _x.adjLaneBoundary, _x.curPoseLgtDist, _x.curPoseLatDist, _x.curPoseRange, _x.curPoseHeading, _x.futPoseLgtDist, _x.futPoseLatDist, _x.futPoseRange, _x.futPoseHeading))
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
      end += 88
      (_x.id, _x.type, _x.laneLoc, _x.curThw, _x.ttcLgt, _x.tFuture, _x.futRelevance, _x.curLgtDistCorr, _x.curLatDistCorr, _x.futLgtDistCorr, _x.futLatDistCorr, _x.futPosRelevance, _x.corridorHalfWidth, _x.adjLaneBoundary, _x.curPoseLgtDist, _x.curPoseLatDist, _x.curPoseRange, _x.curPoseHeading, _x.futPoseLgtDist, _x.futPoseLatDist, _x.futPoseRange, _x.futPoseHeading,) = _get_struct_3I19f().unpack(str[start:end])
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
      buff.write(_get_struct_3I19f().pack(_x.id, _x.type, _x.laneLoc, _x.curThw, _x.ttcLgt, _x.tFuture, _x.futRelevance, _x.curLgtDistCorr, _x.curLatDistCorr, _x.futLgtDistCorr, _x.futLatDistCorr, _x.futPosRelevance, _x.corridorHalfWidth, _x.adjLaneBoundary, _x.curPoseLgtDist, _x.curPoseLatDist, _x.curPoseRange, _x.curPoseHeading, _x.futPoseLgtDist, _x.futPoseLatDist, _x.futPoseRange, _x.futPoseHeading))
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
      end += 88
      (_x.id, _x.type, _x.laneLoc, _x.curThw, _x.ttcLgt, _x.tFuture, _x.futRelevance, _x.curLgtDistCorr, _x.curLatDistCorr, _x.futLgtDistCorr, _x.futLatDistCorr, _x.futPosRelevance, _x.corridorHalfWidth, _x.adjLaneBoundary, _x.curPoseLgtDist, _x.curPoseLatDist, _x.curPoseRange, _x.curPoseHeading, _x.futPoseLgtDist, _x.futPoseLatDist, _x.futPoseRange, _x.futPoseHeading,) = _get_struct_3I19f().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_3I19f = None
def _get_struct_3I19f():
    global _struct_3I19f
    if _struct_3I19f is None:
        _struct_3I19f = struct.Struct("<3I19f")
    return _struct_3I19f

# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from rospy_message_converter/CameraObject.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import rospy_message_converter.msg

class CameraObject(genpy.Message):
  _md5sum = "9c3a606dcff4eb9dfe9dddcaad1527a4"
  _type = "rospy_message_converter/CameraObject"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """uint32 sensor_id
uint32 object_id
float32 score
int32 class_type
Mono3D mono3d
float32 batch_id
float32 subtype
float32[] subtype_scores
float32[] occlusion
float32[] box
float32[] kpts
float32[] kpts_score
float32[] uncertainty_2d
float32[] uncertainty_3d
float32[] reid_feature
float32[] theta2d
float32 has_person

================================================================================
MSG: rospy_message_converter/Mono3D
float32 x
float32 y
float32 z
float32 width
float32 height
float32 length
float32 theta
"""
  __slots__ = ['sensor_id','object_id','score','class_type','mono3d','batch_id','subtype','subtype_scores','occlusion','box','kpts','kpts_score','uncertainty_2d','uncertainty_3d','reid_feature','theta2d','has_person']
  _slot_types = ['uint32','uint32','float32','int32','rospy_message_converter/Mono3D','float32','float32','float32[]','float32[]','float32[]','float32[]','float32[]','float32[]','float32[]','float32[]','float32[]','float32']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       sensor_id,object_id,score,class_type,mono3d,batch_id,subtype,subtype_scores,occlusion,box,kpts,kpts_score,uncertainty_2d,uncertainty_3d,reid_feature,theta2d,has_person

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(CameraObject, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.sensor_id is None:
        self.sensor_id = 0
      if self.object_id is None:
        self.object_id = 0
      if self.score is None:
        self.score = 0.
      if self.class_type is None:
        self.class_type = 0
      if self.mono3d is None:
        self.mono3d = rospy_message_converter.msg.Mono3D()
      if self.batch_id is None:
        self.batch_id = 0.
      if self.subtype is None:
        self.subtype = 0.
      if self.subtype_scores is None:
        self.subtype_scores = []
      if self.occlusion is None:
        self.occlusion = []
      if self.box is None:
        self.box = []
      if self.kpts is None:
        self.kpts = []
      if self.kpts_score is None:
        self.kpts_score = []
      if self.uncertainty_2d is None:
        self.uncertainty_2d = []
      if self.uncertainty_3d is None:
        self.uncertainty_3d = []
      if self.reid_feature is None:
        self.reid_feature = []
      if self.theta2d is None:
        self.theta2d = []
      if self.has_person is None:
        self.has_person = 0.
    else:
      self.sensor_id = 0
      self.object_id = 0
      self.score = 0.
      self.class_type = 0
      self.mono3d = rospy_message_converter.msg.Mono3D()
      self.batch_id = 0.
      self.subtype = 0.
      self.subtype_scores = []
      self.occlusion = []
      self.box = []
      self.kpts = []
      self.kpts_score = []
      self.uncertainty_2d = []
      self.uncertainty_3d = []
      self.reid_feature = []
      self.theta2d = []
      self.has_person = 0.

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
      buff.write(_get_struct_2Ifi9f().pack(_x.sensor_id, _x.object_id, _x.score, _x.class_type, _x.mono3d.x, _x.mono3d.y, _x.mono3d.z, _x.mono3d.width, _x.mono3d.height, _x.mono3d.length, _x.mono3d.theta, _x.batch_id, _x.subtype))
      length = len(self.subtype_scores)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(struct.Struct(pattern).pack(*self.subtype_scores))
      length = len(self.occlusion)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(struct.Struct(pattern).pack(*self.occlusion))
      length = len(self.box)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(struct.Struct(pattern).pack(*self.box))
      length = len(self.kpts)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(struct.Struct(pattern).pack(*self.kpts))
      length = len(self.kpts_score)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(struct.Struct(pattern).pack(*self.kpts_score))
      length = len(self.uncertainty_2d)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(struct.Struct(pattern).pack(*self.uncertainty_2d))
      length = len(self.uncertainty_3d)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(struct.Struct(pattern).pack(*self.uncertainty_3d))
      length = len(self.reid_feature)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(struct.Struct(pattern).pack(*self.reid_feature))
      length = len(self.theta2d)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(struct.Struct(pattern).pack(*self.theta2d))
      _x = self.has_person
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
      if self.mono3d is None:
        self.mono3d = rospy_message_converter.msg.Mono3D()
      end = 0
      _x = self
      start = end
      end += 52
      (_x.sensor_id, _x.object_id, _x.score, _x.class_type, _x.mono3d.x, _x.mono3d.y, _x.mono3d.z, _x.mono3d.width, _x.mono3d.height, _x.mono3d.length, _x.mono3d.theta, _x.batch_id, _x.subtype,) = _get_struct_2Ifi9f().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sf'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.subtype_scores = s.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sf'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.occlusion = s.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sf'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.box = s.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sf'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.kpts = s.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sf'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.kpts_score = s.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sf'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.uncertainty_2d = s.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sf'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.uncertainty_3d = s.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sf'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.reid_feature = s.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sf'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.theta2d = s.unpack(str[start:end])
      start = end
      end += 4
      (self.has_person,) = _get_struct_f().unpack(str[start:end])
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
      buff.write(_get_struct_2Ifi9f().pack(_x.sensor_id, _x.object_id, _x.score, _x.class_type, _x.mono3d.x, _x.mono3d.y, _x.mono3d.z, _x.mono3d.width, _x.mono3d.height, _x.mono3d.length, _x.mono3d.theta, _x.batch_id, _x.subtype))
      length = len(self.subtype_scores)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(self.subtype_scores.tostring())
      length = len(self.occlusion)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(self.occlusion.tostring())
      length = len(self.box)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(self.box.tostring())
      length = len(self.kpts)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(self.kpts.tostring())
      length = len(self.kpts_score)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(self.kpts_score.tostring())
      length = len(self.uncertainty_2d)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(self.uncertainty_2d.tostring())
      length = len(self.uncertainty_3d)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(self.uncertainty_3d.tostring())
      length = len(self.reid_feature)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(self.reid_feature.tostring())
      length = len(self.theta2d)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(self.theta2d.tostring())
      _x = self.has_person
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
      if self.mono3d is None:
        self.mono3d = rospy_message_converter.msg.Mono3D()
      end = 0
      _x = self
      start = end
      end += 52
      (_x.sensor_id, _x.object_id, _x.score, _x.class_type, _x.mono3d.x, _x.mono3d.y, _x.mono3d.z, _x.mono3d.width, _x.mono3d.height, _x.mono3d.length, _x.mono3d.theta, _x.batch_id, _x.subtype,) = _get_struct_2Ifi9f().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sf'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.subtype_scores = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sf'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.occlusion = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sf'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.box = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sf'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.kpts = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sf'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.kpts_score = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sf'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.uncertainty_2d = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sf'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.uncertainty_3d = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sf'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.reid_feature = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sf'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.theta2d = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=length)
      start = end
      end += 4
      (self.has_person,) = _get_struct_f().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_2Ifi9f = None
def _get_struct_2Ifi9f():
    global _struct_2Ifi9f
    if _struct_2Ifi9f is None:
        _struct_2Ifi9f = struct.Struct("<2Ifi9f")
    return _struct_2Ifi9f
_struct_f = None
def _get_struct_f():
    global _struct_f
    if _struct_f is None:
        _struct_f = struct.Struct("<f")
    return _struct_f

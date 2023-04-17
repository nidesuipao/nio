# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from rospy_message_converter/CdmModelResult.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import rospy_message_converter.msg

class CdmModelResult(genpy.Message):
  _md5sum = "cb7b9832a09efb95a6ed44d22c0b5082"
  _type = "rospy_message_converter/CdmModelResult"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """int32 sensor_id
uint64 sensor_ts
uint64 cooking_ts
string model_name
int32 im_width
int32 im_height
FrameDescriptor frame_descriptor
Object2D[] object_2d
Object3D[] object_3d
LaneInfo lane_info
SegmentInfo segment_info
uint64 publish_ptp_ts
string publisher_id
uint64 counter
uint64 publish_ts

================================================================================
MSG: rospy_message_converter/FrameDescriptor
int32[] cids
float32[] scores
int32[] sub_cids
float32[] sub_scores
float32[] embeddings

================================================================================
MSG: rospy_message_converter/Object2D
int32 cid
float32 score
int32 sub_cid
float32 sub_score
float32[] box
float32 theta
float32[] keypoints

================================================================================
MSG: rospy_message_converter/Object3D
int32 cid
float32 score
int32 sub_cid
float32 sub_score
float32 cx
float32 cy
float32 cz
float32 width
float32 height
float32 length
float32 theta
float32[] keypoints

================================================================================
MSG: rospy_message_converter/LaneInfo
int32 dims
Lane[] lanes

================================================================================
MSG: rospy_message_converter/Lane
int32 cid
float32 score
int32 sub_cid
float32 sub_score
float32[] points
float32[] coefs

================================================================================
MSG: rospy_message_converter/SegmentInfo
string data_format
string data
"""
  __slots__ = ['sensor_id','sensor_ts','cooking_ts','model_name','im_width','im_height','frame_descriptor','object_2d','object_3d','lane_info','segment_info','publish_ptp_ts','publisher_id','counter','publish_ts']
  _slot_types = ['int32','uint64','uint64','string','int32','int32','rospy_message_converter/FrameDescriptor','rospy_message_converter/Object2D[]','rospy_message_converter/Object3D[]','rospy_message_converter/LaneInfo','rospy_message_converter/SegmentInfo','uint64','string','uint64','uint64']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       sensor_id,sensor_ts,cooking_ts,model_name,im_width,im_height,frame_descriptor,object_2d,object_3d,lane_info,segment_info,publish_ptp_ts,publisher_id,counter,publish_ts

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(CdmModelResult, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.sensor_id is None:
        self.sensor_id = 0
      if self.sensor_ts is None:
        self.sensor_ts = 0
      if self.cooking_ts is None:
        self.cooking_ts = 0
      if self.model_name is None:
        self.model_name = ''
      if self.im_width is None:
        self.im_width = 0
      if self.im_height is None:
        self.im_height = 0
      if self.frame_descriptor is None:
        self.frame_descriptor = rospy_message_converter.msg.FrameDescriptor()
      if self.object_2d is None:
        self.object_2d = []
      if self.object_3d is None:
        self.object_3d = []
      if self.lane_info is None:
        self.lane_info = rospy_message_converter.msg.LaneInfo()
      if self.segment_info is None:
        self.segment_info = rospy_message_converter.msg.SegmentInfo()
      if self.publish_ptp_ts is None:
        self.publish_ptp_ts = 0
      if self.publisher_id is None:
        self.publisher_id = ''
      if self.counter is None:
        self.counter = 0
      if self.publish_ts is None:
        self.publish_ts = 0
    else:
      self.sensor_id = 0
      self.sensor_ts = 0
      self.cooking_ts = 0
      self.model_name = ''
      self.im_width = 0
      self.im_height = 0
      self.frame_descriptor = rospy_message_converter.msg.FrameDescriptor()
      self.object_2d = []
      self.object_3d = []
      self.lane_info = rospy_message_converter.msg.LaneInfo()
      self.segment_info = rospy_message_converter.msg.SegmentInfo()
      self.publish_ptp_ts = 0
      self.publisher_id = ''
      self.counter = 0
      self.publish_ts = 0

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
      buff.write(_get_struct_i2Q().pack(_x.sensor_id, _x.sensor_ts, _x.cooking_ts))
      _x = self.model_name
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_2i().pack(_x.im_width, _x.im_height))
      length = len(self.frame_descriptor.cids)
      buff.write(_struct_I.pack(length))
      pattern = '<%si'%length
      buff.write(struct.Struct(pattern).pack(*self.frame_descriptor.cids))
      length = len(self.frame_descriptor.scores)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(struct.Struct(pattern).pack(*self.frame_descriptor.scores))
      length = len(self.frame_descriptor.sub_cids)
      buff.write(_struct_I.pack(length))
      pattern = '<%si'%length
      buff.write(struct.Struct(pattern).pack(*self.frame_descriptor.sub_cids))
      length = len(self.frame_descriptor.sub_scores)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(struct.Struct(pattern).pack(*self.frame_descriptor.sub_scores))
      length = len(self.frame_descriptor.embeddings)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(struct.Struct(pattern).pack(*self.frame_descriptor.embeddings))
      length = len(self.object_2d)
      buff.write(_struct_I.pack(length))
      for val1 in self.object_2d:
        _x = val1
        buff.write(_get_struct_ifif().pack(_x.cid, _x.score, _x.sub_cid, _x.sub_score))
        length = len(val1.box)
        buff.write(_struct_I.pack(length))
        pattern = '<%sf'%length
        buff.write(struct.Struct(pattern).pack(*val1.box))
        _x = val1.theta
        buff.write(_get_struct_f().pack(_x))
        length = len(val1.keypoints)
        buff.write(_struct_I.pack(length))
        pattern = '<%sf'%length
        buff.write(struct.Struct(pattern).pack(*val1.keypoints))
      length = len(self.object_3d)
      buff.write(_struct_I.pack(length))
      for val1 in self.object_3d:
        _x = val1
        buff.write(_get_struct_ifi8f().pack(_x.cid, _x.score, _x.sub_cid, _x.sub_score, _x.cx, _x.cy, _x.cz, _x.width, _x.height, _x.length, _x.theta))
        length = len(val1.keypoints)
        buff.write(_struct_I.pack(length))
        pattern = '<%sf'%length
        buff.write(struct.Struct(pattern).pack(*val1.keypoints))
      _x = self.lane_info.dims
      buff.write(_get_struct_i().pack(_x))
      length = len(self.lane_info.lanes)
      buff.write(_struct_I.pack(length))
      for val1 in self.lane_info.lanes:
        _x = val1
        buff.write(_get_struct_ifif().pack(_x.cid, _x.score, _x.sub_cid, _x.sub_score))
        length = len(val1.points)
        buff.write(_struct_I.pack(length))
        pattern = '<%sf'%length
        buff.write(struct.Struct(pattern).pack(*val1.points))
        length = len(val1.coefs)
        buff.write(_struct_I.pack(length))
        pattern = '<%sf'%length
        buff.write(struct.Struct(pattern).pack(*val1.coefs))
      _x = self.segment_info.data_format
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self.segment_info.data
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self.publish_ptp_ts
      buff.write(_get_struct_Q().pack(_x))
      _x = self.publisher_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_2Q().pack(_x.counter, _x.publish_ts))
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
      if self.frame_descriptor is None:
        self.frame_descriptor = rospy_message_converter.msg.FrameDescriptor()
      if self.object_2d is None:
        self.object_2d = None
      if self.object_3d is None:
        self.object_3d = None
      if self.lane_info is None:
        self.lane_info = rospy_message_converter.msg.LaneInfo()
      if self.segment_info is None:
        self.segment_info = rospy_message_converter.msg.SegmentInfo()
      end = 0
      _x = self
      start = end
      end += 20
      (_x.sensor_id, _x.sensor_ts, _x.cooking_ts,) = _get_struct_i2Q().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.model_name = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.model_name = str[start:end]
      _x = self
      start = end
      end += 8
      (_x.im_width, _x.im_height,) = _get_struct_2i().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%si'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.frame_descriptor.cids = s.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sf'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.frame_descriptor.scores = s.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%si'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.frame_descriptor.sub_cids = s.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sf'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.frame_descriptor.sub_scores = s.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sf'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.frame_descriptor.embeddings = s.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.object_2d = []
      for i in range(0, length):
        val1 = rospy_message_converter.msg.Object2D()
        _x = val1
        start = end
        end += 16
        (_x.cid, _x.score, _x.sub_cid, _x.sub_score,) = _get_struct_ifif().unpack(str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        pattern = '<%sf'%length
        start = end
        s = struct.Struct(pattern)
        end += s.size
        val1.box = s.unpack(str[start:end])
        start = end
        end += 4
        (val1.theta,) = _get_struct_f().unpack(str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        pattern = '<%sf'%length
        start = end
        s = struct.Struct(pattern)
        end += s.size
        val1.keypoints = s.unpack(str[start:end])
        self.object_2d.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.object_3d = []
      for i in range(0, length):
        val1 = rospy_message_converter.msg.Object3D()
        _x = val1
        start = end
        end += 44
        (_x.cid, _x.score, _x.sub_cid, _x.sub_score, _x.cx, _x.cy, _x.cz, _x.width, _x.height, _x.length, _x.theta,) = _get_struct_ifi8f().unpack(str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        pattern = '<%sf'%length
        start = end
        s = struct.Struct(pattern)
        end += s.size
        val1.keypoints = s.unpack(str[start:end])
        self.object_3d.append(val1)
      start = end
      end += 4
      (self.lane_info.dims,) = _get_struct_i().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.lane_info.lanes = []
      for i in range(0, length):
        val1 = rospy_message_converter.msg.Lane()
        _x = val1
        start = end
        end += 16
        (_x.cid, _x.score, _x.sub_cid, _x.sub_score,) = _get_struct_ifif().unpack(str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        pattern = '<%sf'%length
        start = end
        s = struct.Struct(pattern)
        end += s.size
        val1.points = s.unpack(str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        pattern = '<%sf'%length
        start = end
        s = struct.Struct(pattern)
        end += s.size
        val1.coefs = s.unpack(str[start:end])
        self.lane_info.lanes.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.segment_info.data_format = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.segment_info.data_format = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.segment_info.data = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.segment_info.data = str[start:end]
      start = end
      end += 8
      (self.publish_ptp_ts,) = _get_struct_Q().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.publisher_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.publisher_id = str[start:end]
      _x = self
      start = end
      end += 16
      (_x.counter, _x.publish_ts,) = _get_struct_2Q().unpack(str[start:end])
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
      buff.write(_get_struct_i2Q().pack(_x.sensor_id, _x.sensor_ts, _x.cooking_ts))
      _x = self.model_name
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_2i().pack(_x.im_width, _x.im_height))
      length = len(self.frame_descriptor.cids)
      buff.write(_struct_I.pack(length))
      pattern = '<%si'%length
      buff.write(self.frame_descriptor.cids.tostring())
      length = len(self.frame_descriptor.scores)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(self.frame_descriptor.scores.tostring())
      length = len(self.frame_descriptor.sub_cids)
      buff.write(_struct_I.pack(length))
      pattern = '<%si'%length
      buff.write(self.frame_descriptor.sub_cids.tostring())
      length = len(self.frame_descriptor.sub_scores)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(self.frame_descriptor.sub_scores.tostring())
      length = len(self.frame_descriptor.embeddings)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(self.frame_descriptor.embeddings.tostring())
      length = len(self.object_2d)
      buff.write(_struct_I.pack(length))
      for val1 in self.object_2d:
        _x = val1
        buff.write(_get_struct_ifif().pack(_x.cid, _x.score, _x.sub_cid, _x.sub_score))
        length = len(val1.box)
        buff.write(_struct_I.pack(length))
        pattern = '<%sf'%length
        buff.write(val1.box.tostring())
        _x = val1.theta
        buff.write(_get_struct_f().pack(_x))
        length = len(val1.keypoints)
        buff.write(_struct_I.pack(length))
        pattern = '<%sf'%length
        buff.write(val1.keypoints.tostring())
      length = len(self.object_3d)
      buff.write(_struct_I.pack(length))
      for val1 in self.object_3d:
        _x = val1
        buff.write(_get_struct_ifi8f().pack(_x.cid, _x.score, _x.sub_cid, _x.sub_score, _x.cx, _x.cy, _x.cz, _x.width, _x.height, _x.length, _x.theta))
        length = len(val1.keypoints)
        buff.write(_struct_I.pack(length))
        pattern = '<%sf'%length
        buff.write(val1.keypoints.tostring())
      _x = self.lane_info.dims
      buff.write(_get_struct_i().pack(_x))
      length = len(self.lane_info.lanes)
      buff.write(_struct_I.pack(length))
      for val1 in self.lane_info.lanes:
        _x = val1
        buff.write(_get_struct_ifif().pack(_x.cid, _x.score, _x.sub_cid, _x.sub_score))
        length = len(val1.points)
        buff.write(_struct_I.pack(length))
        pattern = '<%sf'%length
        buff.write(val1.points.tostring())
        length = len(val1.coefs)
        buff.write(_struct_I.pack(length))
        pattern = '<%sf'%length
        buff.write(val1.coefs.tostring())
      _x = self.segment_info.data_format
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self.segment_info.data
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self.publish_ptp_ts
      buff.write(_get_struct_Q().pack(_x))
      _x = self.publisher_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_2Q().pack(_x.counter, _x.publish_ts))
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
      if self.frame_descriptor is None:
        self.frame_descriptor = rospy_message_converter.msg.FrameDescriptor()
      if self.object_2d is None:
        self.object_2d = None
      if self.object_3d is None:
        self.object_3d = None
      if self.lane_info is None:
        self.lane_info = rospy_message_converter.msg.LaneInfo()
      if self.segment_info is None:
        self.segment_info = rospy_message_converter.msg.SegmentInfo()
      end = 0
      _x = self
      start = end
      end += 20
      (_x.sensor_id, _x.sensor_ts, _x.cooking_ts,) = _get_struct_i2Q().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.model_name = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.model_name = str[start:end]
      _x = self
      start = end
      end += 8
      (_x.im_width, _x.im_height,) = _get_struct_2i().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%si'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.frame_descriptor.cids = numpy.frombuffer(str[start:end], dtype=numpy.int32, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sf'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.frame_descriptor.scores = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%si'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.frame_descriptor.sub_cids = numpy.frombuffer(str[start:end], dtype=numpy.int32, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sf'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.frame_descriptor.sub_scores = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sf'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.frame_descriptor.embeddings = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.object_2d = []
      for i in range(0, length):
        val1 = rospy_message_converter.msg.Object2D()
        _x = val1
        start = end
        end += 16
        (_x.cid, _x.score, _x.sub_cid, _x.sub_score,) = _get_struct_ifif().unpack(str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        pattern = '<%sf'%length
        start = end
        s = struct.Struct(pattern)
        end += s.size
        val1.box = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=length)
        start = end
        end += 4
        (val1.theta,) = _get_struct_f().unpack(str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        pattern = '<%sf'%length
        start = end
        s = struct.Struct(pattern)
        end += s.size
        val1.keypoints = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=length)
        self.object_2d.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.object_3d = []
      for i in range(0, length):
        val1 = rospy_message_converter.msg.Object3D()
        _x = val1
        start = end
        end += 44
        (_x.cid, _x.score, _x.sub_cid, _x.sub_score, _x.cx, _x.cy, _x.cz, _x.width, _x.height, _x.length, _x.theta,) = _get_struct_ifi8f().unpack(str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        pattern = '<%sf'%length
        start = end
        s = struct.Struct(pattern)
        end += s.size
        val1.keypoints = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=length)
        self.object_3d.append(val1)
      start = end
      end += 4
      (self.lane_info.dims,) = _get_struct_i().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.lane_info.lanes = []
      for i in range(0, length):
        val1 = rospy_message_converter.msg.Lane()
        _x = val1
        start = end
        end += 16
        (_x.cid, _x.score, _x.sub_cid, _x.sub_score,) = _get_struct_ifif().unpack(str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        pattern = '<%sf'%length
        start = end
        s = struct.Struct(pattern)
        end += s.size
        val1.points = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=length)
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        pattern = '<%sf'%length
        start = end
        s = struct.Struct(pattern)
        end += s.size
        val1.coefs = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=length)
        self.lane_info.lanes.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.segment_info.data_format = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.segment_info.data_format = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.segment_info.data = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.segment_info.data = str[start:end]
      start = end
      end += 8
      (self.publish_ptp_ts,) = _get_struct_Q().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.publisher_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.publisher_id = str[start:end]
      _x = self
      start = end
      end += 16
      (_x.counter, _x.publish_ts,) = _get_struct_2Q().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_2Q = None
def _get_struct_2Q():
    global _struct_2Q
    if _struct_2Q is None:
        _struct_2Q = struct.Struct("<2Q")
    return _struct_2Q
_struct_2i = None
def _get_struct_2i():
    global _struct_2i
    if _struct_2i is None:
        _struct_2i = struct.Struct("<2i")
    return _struct_2i
_struct_Q = None
def _get_struct_Q():
    global _struct_Q
    if _struct_Q is None:
        _struct_Q = struct.Struct("<Q")
    return _struct_Q
_struct_f = None
def _get_struct_f():
    global _struct_f
    if _struct_f is None:
        _struct_f = struct.Struct("<f")
    return _struct_f
_struct_i = None
def _get_struct_i():
    global _struct_i
    if _struct_i is None:
        _struct_i = struct.Struct("<i")
    return _struct_i
_struct_i2Q = None
def _get_struct_i2Q():
    global _struct_i2Q
    if _struct_i2Q is None:
        _struct_i2Q = struct.Struct("<i2Q")
    return _struct_i2Q
_struct_ifi8f = None
def _get_struct_ifi8f():
    global _struct_ifi8f
    if _struct_ifi8f is None:
        _struct_ifi8f = struct.Struct("<ifi8f")
    return _struct_ifi8f
_struct_ifif = None
def _get_struct_ifif():
    global _struct_ifif
    if _struct_ifif is None:
        _struct_ifif = struct.Struct("<ifif")
    return _struct_ifif

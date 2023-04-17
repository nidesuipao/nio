# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from rospy_message_converter/HdLinkSegment.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import rospy_message_converter.msg

class HdLinkSegment(genpy.Message):
  _md5sum = "5d7c37bfb1cf78ac71018e5d793d7301"
  _type = "rospy_message_converter/HdLinkSegment"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """HdLinkContent[] hd_link_contents
float32 segment_length_meter
Point3d hd_match_start_point
Point3d hd_match_end_point
float32 offset

================================================================================
MSG: rospy_message_converter/HdLinkContent
uint64 hd_link_id
float64 hd_link_length
HDLaneGroup[] hd_lane_groups
Point3d link_start_point
Point3d link_end_point
uint32 hd_link_lane_status

================================================================================
MSG: rospy_message_converter/HDLaneGroup
uint64 hd_lane_group_id
HDLaneInfo[] hd_lane_infos

================================================================================
MSG: rospy_message_converter/HDLaneInfo
uint64 hd_lane_id
uint64[] entry_lane_ids
uint64[] exit_lane_ids

================================================================================
MSG: rospy_message_converter/Point3d
float64 longitude
float64 latitude
float64 altitude
"""
  __slots__ = ['hd_link_contents','segment_length_meter','hd_match_start_point','hd_match_end_point','offset']
  _slot_types = ['rospy_message_converter/HdLinkContent[]','float32','rospy_message_converter/Point3d','rospy_message_converter/Point3d','float32']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       hd_link_contents,segment_length_meter,hd_match_start_point,hd_match_end_point,offset

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(HdLinkSegment, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.hd_link_contents is None:
        self.hd_link_contents = []
      if self.segment_length_meter is None:
        self.segment_length_meter = 0.
      if self.hd_match_start_point is None:
        self.hd_match_start_point = rospy_message_converter.msg.Point3d()
      if self.hd_match_end_point is None:
        self.hd_match_end_point = rospy_message_converter.msg.Point3d()
      if self.offset is None:
        self.offset = 0.
    else:
      self.hd_link_contents = []
      self.segment_length_meter = 0.
      self.hd_match_start_point = rospy_message_converter.msg.Point3d()
      self.hd_match_end_point = rospy_message_converter.msg.Point3d()
      self.offset = 0.

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
      length = len(self.hd_link_contents)
      buff.write(_struct_I.pack(length))
      for val1 in self.hd_link_contents:
        _x = val1
        buff.write(_get_struct_Qd().pack(_x.hd_link_id, _x.hd_link_length))
        length = len(val1.hd_lane_groups)
        buff.write(_struct_I.pack(length))
        for val2 in val1.hd_lane_groups:
          _x = val2.hd_lane_group_id
          buff.write(_get_struct_Q().pack(_x))
          length = len(val2.hd_lane_infos)
          buff.write(_struct_I.pack(length))
          for val3 in val2.hd_lane_infos:
            _x = val3.hd_lane_id
            buff.write(_get_struct_Q().pack(_x))
            length = len(val3.entry_lane_ids)
            buff.write(_struct_I.pack(length))
            pattern = '<%sQ'%length
            buff.write(struct.Struct(pattern).pack(*val3.entry_lane_ids))
            length = len(val3.exit_lane_ids)
            buff.write(_struct_I.pack(length))
            pattern = '<%sQ'%length
            buff.write(struct.Struct(pattern).pack(*val3.exit_lane_ids))
        _v1 = val1.link_start_point
        _x = _v1
        buff.write(_get_struct_3d().pack(_x.longitude, _x.latitude, _x.altitude))
        _v2 = val1.link_end_point
        _x = _v2
        buff.write(_get_struct_3d().pack(_x.longitude, _x.latitude, _x.altitude))
        _x = val1.hd_link_lane_status
        buff.write(_get_struct_I().pack(_x))
      _x = self
      buff.write(_get_struct_f6df().pack(_x.segment_length_meter, _x.hd_match_start_point.longitude, _x.hd_match_start_point.latitude, _x.hd_match_start_point.altitude, _x.hd_match_end_point.longitude, _x.hd_match_end_point.latitude, _x.hd_match_end_point.altitude, _x.offset))
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
      if self.hd_link_contents is None:
        self.hd_link_contents = None
      if self.hd_match_start_point is None:
        self.hd_match_start_point = rospy_message_converter.msg.Point3d()
      if self.hd_match_end_point is None:
        self.hd_match_end_point = rospy_message_converter.msg.Point3d()
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.hd_link_contents = []
      for i in range(0, length):
        val1 = rospy_message_converter.msg.HdLinkContent()
        _x = val1
        start = end
        end += 16
        (_x.hd_link_id, _x.hd_link_length,) = _get_struct_Qd().unpack(str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        val1.hd_lane_groups = []
        for i in range(0, length):
          val2 = rospy_message_converter.msg.HDLaneGroup()
          start = end
          end += 8
          (val2.hd_lane_group_id,) = _get_struct_Q().unpack(str[start:end])
          start = end
          end += 4
          (length,) = _struct_I.unpack(str[start:end])
          val2.hd_lane_infos = []
          for i in range(0, length):
            val3 = rospy_message_converter.msg.HDLaneInfo()
            start = end
            end += 8
            (val3.hd_lane_id,) = _get_struct_Q().unpack(str[start:end])
            start = end
            end += 4
            (length,) = _struct_I.unpack(str[start:end])
            pattern = '<%sQ'%length
            start = end
            s = struct.Struct(pattern)
            end += s.size
            val3.entry_lane_ids = s.unpack(str[start:end])
            start = end
            end += 4
            (length,) = _struct_I.unpack(str[start:end])
            pattern = '<%sQ'%length
            start = end
            s = struct.Struct(pattern)
            end += s.size
            val3.exit_lane_ids = s.unpack(str[start:end])
            val2.hd_lane_infos.append(val3)
          val1.hd_lane_groups.append(val2)
        _v3 = val1.link_start_point
        _x = _v3
        start = end
        end += 24
        (_x.longitude, _x.latitude, _x.altitude,) = _get_struct_3d().unpack(str[start:end])
        _v4 = val1.link_end_point
        _x = _v4
        start = end
        end += 24
        (_x.longitude, _x.latitude, _x.altitude,) = _get_struct_3d().unpack(str[start:end])
        start = end
        end += 4
        (val1.hd_link_lane_status,) = _get_struct_I().unpack(str[start:end])
        self.hd_link_contents.append(val1)
      _x = self
      start = end
      end += 56
      (_x.segment_length_meter, _x.hd_match_start_point.longitude, _x.hd_match_start_point.latitude, _x.hd_match_start_point.altitude, _x.hd_match_end_point.longitude, _x.hd_match_end_point.latitude, _x.hd_match_end_point.altitude, _x.offset,) = _get_struct_f6df().unpack(str[start:end])
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
      length = len(self.hd_link_contents)
      buff.write(_struct_I.pack(length))
      for val1 in self.hd_link_contents:
        _x = val1
        buff.write(_get_struct_Qd().pack(_x.hd_link_id, _x.hd_link_length))
        length = len(val1.hd_lane_groups)
        buff.write(_struct_I.pack(length))
        for val2 in val1.hd_lane_groups:
          _x = val2.hd_lane_group_id
          buff.write(_get_struct_Q().pack(_x))
          length = len(val2.hd_lane_infos)
          buff.write(_struct_I.pack(length))
          for val3 in val2.hd_lane_infos:
            _x = val3.hd_lane_id
            buff.write(_get_struct_Q().pack(_x))
            length = len(val3.entry_lane_ids)
            buff.write(_struct_I.pack(length))
            pattern = '<%sQ'%length
            buff.write(val3.entry_lane_ids.tostring())
            length = len(val3.exit_lane_ids)
            buff.write(_struct_I.pack(length))
            pattern = '<%sQ'%length
            buff.write(val3.exit_lane_ids.tostring())
        _v5 = val1.link_start_point
        _x = _v5
        buff.write(_get_struct_3d().pack(_x.longitude, _x.latitude, _x.altitude))
        _v6 = val1.link_end_point
        _x = _v6
        buff.write(_get_struct_3d().pack(_x.longitude, _x.latitude, _x.altitude))
        _x = val1.hd_link_lane_status
        buff.write(_get_struct_I().pack(_x))
      _x = self
      buff.write(_get_struct_f6df().pack(_x.segment_length_meter, _x.hd_match_start_point.longitude, _x.hd_match_start_point.latitude, _x.hd_match_start_point.altitude, _x.hd_match_end_point.longitude, _x.hd_match_end_point.latitude, _x.hd_match_end_point.altitude, _x.offset))
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
      if self.hd_link_contents is None:
        self.hd_link_contents = None
      if self.hd_match_start_point is None:
        self.hd_match_start_point = rospy_message_converter.msg.Point3d()
      if self.hd_match_end_point is None:
        self.hd_match_end_point = rospy_message_converter.msg.Point3d()
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.hd_link_contents = []
      for i in range(0, length):
        val1 = rospy_message_converter.msg.HdLinkContent()
        _x = val1
        start = end
        end += 16
        (_x.hd_link_id, _x.hd_link_length,) = _get_struct_Qd().unpack(str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        val1.hd_lane_groups = []
        for i in range(0, length):
          val2 = rospy_message_converter.msg.HDLaneGroup()
          start = end
          end += 8
          (val2.hd_lane_group_id,) = _get_struct_Q().unpack(str[start:end])
          start = end
          end += 4
          (length,) = _struct_I.unpack(str[start:end])
          val2.hd_lane_infos = []
          for i in range(0, length):
            val3 = rospy_message_converter.msg.HDLaneInfo()
            start = end
            end += 8
            (val3.hd_lane_id,) = _get_struct_Q().unpack(str[start:end])
            start = end
            end += 4
            (length,) = _struct_I.unpack(str[start:end])
            pattern = '<%sQ'%length
            start = end
            s = struct.Struct(pattern)
            end += s.size
            val3.entry_lane_ids = numpy.frombuffer(str[start:end], dtype=numpy.uint64, count=length)
            start = end
            end += 4
            (length,) = _struct_I.unpack(str[start:end])
            pattern = '<%sQ'%length
            start = end
            s = struct.Struct(pattern)
            end += s.size
            val3.exit_lane_ids = numpy.frombuffer(str[start:end], dtype=numpy.uint64, count=length)
            val2.hd_lane_infos.append(val3)
          val1.hd_lane_groups.append(val2)
        _v7 = val1.link_start_point
        _x = _v7
        start = end
        end += 24
        (_x.longitude, _x.latitude, _x.altitude,) = _get_struct_3d().unpack(str[start:end])
        _v8 = val1.link_end_point
        _x = _v8
        start = end
        end += 24
        (_x.longitude, _x.latitude, _x.altitude,) = _get_struct_3d().unpack(str[start:end])
        start = end
        end += 4
        (val1.hd_link_lane_status,) = _get_struct_I().unpack(str[start:end])
        self.hd_link_contents.append(val1)
      _x = self
      start = end
      end += 56
      (_x.segment_length_meter, _x.hd_match_start_point.longitude, _x.hd_match_start_point.latitude, _x.hd_match_start_point.altitude, _x.hd_match_end_point.longitude, _x.hd_match_end_point.latitude, _x.hd_match_end_point.altitude, _x.offset,) = _get_struct_f6df().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_3d = None
def _get_struct_3d():
    global _struct_3d
    if _struct_3d is None:
        _struct_3d = struct.Struct("<3d")
    return _struct_3d
_struct_Q = None
def _get_struct_Q():
    global _struct_Q
    if _struct_Q is None:
        _struct_Q = struct.Struct("<Q")
    return _struct_Q
_struct_Qd = None
def _get_struct_Qd():
    global _struct_Qd
    if _struct_Qd is None:
        _struct_Qd = struct.Struct("<Qd")
    return _struct_Qd
_struct_f6df = None
def _get_struct_f6df():
    global _struct_f6df
    if _struct_f6df is None:
        _struct_f6df = struct.Struct("<f6df")
    return _struct_f6df

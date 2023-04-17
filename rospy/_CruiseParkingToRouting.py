# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from rospy_message_converter/CruiseParkingToRouting.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import rospy_message_converter.msg

class CruiseParkingToRouting(genpy.Message):
  _md5sum = "897c0410f0ddfcf73cbe5f8ab8b07a1d"
  _type = "rospy_message_converter/CruiseParkingToRouting"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """int32 type
Point2d power_swap_station_loc
int32 dest_type
string power_swap_station_id
Point3d current_loc
uint64[] current_lane_id_sequence
uint64 timestamp
uint64 publish_ptp_ts
string publisher_id
uint64 counter
uint64 publish_ts

================================================================================
MSG: rospy_message_converter/Point2d
float64 longitude
float64 latitude

================================================================================
MSG: rospy_message_converter/Point3d
float64 longitude
float64 latitude
float64 altitude
"""
  __slots__ = ['type','power_swap_station_loc','dest_type','power_swap_station_id','current_loc','current_lane_id_sequence','timestamp','publish_ptp_ts','publisher_id','counter','publish_ts']
  _slot_types = ['int32','rospy_message_converter/Point2d','int32','string','rospy_message_converter/Point3d','uint64[]','uint64','uint64','string','uint64','uint64']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       type,power_swap_station_loc,dest_type,power_swap_station_id,current_loc,current_lane_id_sequence,timestamp,publish_ptp_ts,publisher_id,counter,publish_ts

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(CruiseParkingToRouting, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.type is None:
        self.type = 0
      if self.power_swap_station_loc is None:
        self.power_swap_station_loc = rospy_message_converter.msg.Point2d()
      if self.dest_type is None:
        self.dest_type = 0
      if self.power_swap_station_id is None:
        self.power_swap_station_id = ''
      if self.current_loc is None:
        self.current_loc = rospy_message_converter.msg.Point3d()
      if self.current_lane_id_sequence is None:
        self.current_lane_id_sequence = []
      if self.timestamp is None:
        self.timestamp = 0
      if self.publish_ptp_ts is None:
        self.publish_ptp_ts = 0
      if self.publisher_id is None:
        self.publisher_id = ''
      if self.counter is None:
        self.counter = 0
      if self.publish_ts is None:
        self.publish_ts = 0
    else:
      self.type = 0
      self.power_swap_station_loc = rospy_message_converter.msg.Point2d()
      self.dest_type = 0
      self.power_swap_station_id = ''
      self.current_loc = rospy_message_converter.msg.Point3d()
      self.current_lane_id_sequence = []
      self.timestamp = 0
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
      buff.write(_get_struct_i2di().pack(_x.type, _x.power_swap_station_loc.longitude, _x.power_swap_station_loc.latitude, _x.dest_type))
      _x = self.power_swap_station_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_3d().pack(_x.current_loc.longitude, _x.current_loc.latitude, _x.current_loc.altitude))
      length = len(self.current_lane_id_sequence)
      buff.write(_struct_I.pack(length))
      pattern = '<%sQ'%length
      buff.write(struct.Struct(pattern).pack(*self.current_lane_id_sequence))
      _x = self
      buff.write(_get_struct_2Q().pack(_x.timestamp, _x.publish_ptp_ts))
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
      if self.power_swap_station_loc is None:
        self.power_swap_station_loc = rospy_message_converter.msg.Point2d()
      if self.current_loc is None:
        self.current_loc = rospy_message_converter.msg.Point3d()
      end = 0
      _x = self
      start = end
      end += 24
      (_x.type, _x.power_swap_station_loc.longitude, _x.power_swap_station_loc.latitude, _x.dest_type,) = _get_struct_i2di().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.power_swap_station_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.power_swap_station_id = str[start:end]
      _x = self
      start = end
      end += 24
      (_x.current_loc.longitude, _x.current_loc.latitude, _x.current_loc.altitude,) = _get_struct_3d().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sQ'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.current_lane_id_sequence = s.unpack(str[start:end])
      _x = self
      start = end
      end += 16
      (_x.timestamp, _x.publish_ptp_ts,) = _get_struct_2Q().unpack(str[start:end])
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
      buff.write(_get_struct_i2di().pack(_x.type, _x.power_swap_station_loc.longitude, _x.power_swap_station_loc.latitude, _x.dest_type))
      _x = self.power_swap_station_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_3d().pack(_x.current_loc.longitude, _x.current_loc.latitude, _x.current_loc.altitude))
      length = len(self.current_lane_id_sequence)
      buff.write(_struct_I.pack(length))
      pattern = '<%sQ'%length
      buff.write(self.current_lane_id_sequence.tostring())
      _x = self
      buff.write(_get_struct_2Q().pack(_x.timestamp, _x.publish_ptp_ts))
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
      if self.power_swap_station_loc is None:
        self.power_swap_station_loc = rospy_message_converter.msg.Point2d()
      if self.current_loc is None:
        self.current_loc = rospy_message_converter.msg.Point3d()
      end = 0
      _x = self
      start = end
      end += 24
      (_x.type, _x.power_swap_station_loc.longitude, _x.power_swap_station_loc.latitude, _x.dest_type,) = _get_struct_i2di().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.power_swap_station_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.power_swap_station_id = str[start:end]
      _x = self
      start = end
      end += 24
      (_x.current_loc.longitude, _x.current_loc.latitude, _x.current_loc.altitude,) = _get_struct_3d().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sQ'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.current_lane_id_sequence = numpy.frombuffer(str[start:end], dtype=numpy.uint64, count=length)
      _x = self
      start = end
      end += 16
      (_x.timestamp, _x.publish_ptp_ts,) = _get_struct_2Q().unpack(str[start:end])
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
_struct_3d = None
def _get_struct_3d():
    global _struct_3d
    if _struct_3d is None:
        _struct_3d = struct.Struct("<3d")
    return _struct_3d
_struct_i2di = None
def _get_struct_i2di():
    global _struct_i2di
    if _struct_i2di is None:
        _struct_i2di = struct.Struct("<i2di")
    return _struct_i2di

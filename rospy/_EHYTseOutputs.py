# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from rospy_message_converter/EHYTseOutputs.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import rospy_message_converter.msg

class EHYTseOutputs(genpy.Message):
  _md5sum = "986083bb8e6d4a19bf14dd5a7cbbcb12"
  _type = "rospy_message_converter/EHYTseOutputs"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """TgtObj[] tse_obj
bool tsi_flg_cipv_lost
uint64 publish_ptp_ts
string publisher_id
uint64 counter
uint64 publish_ts

================================================================================
MSG: rospy_message_converter/TgtObj
uint32 id
uint32 obj_index
uint32 confidence
float32 lon_pos_ccs
float32 lon_pos_vcs
float32 lon_pos_vcs_std
float32 lon_vel
float32 lon_vel_std
float32 lon_acc
float32 lat_pos_ccs
float32 lat_pos_vcs
float32 lat_pos_vcs_std
float32 lat_vel
float32 lat_vel_std
float32 lat_vel_ccs
float32 lat_acc
int32 status
int32 type
int32 valid
uint32 age
float32 width
float32 length
float32 height
float32 phi_angle
float32 dphi_angle_rate
int32 fusion_source
float32 ttc
int32 blinker_info
uint32 brake_lights
float32 prob_lane_change
int32 dirLaneChange
uint32 age_in_path
"""
  __slots__ = ['tse_obj','tsi_flg_cipv_lost','publish_ptp_ts','publisher_id','counter','publish_ts']
  _slot_types = ['rospy_message_converter/TgtObj[]','bool','uint64','string','uint64','uint64']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       tse_obj,tsi_flg_cipv_lost,publish_ptp_ts,publisher_id,counter,publish_ts

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(EHYTseOutputs, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.tse_obj is None:
        self.tse_obj = []
      if self.tsi_flg_cipv_lost is None:
        self.tsi_flg_cipv_lost = False
      if self.publish_ptp_ts is None:
        self.publish_ptp_ts = 0
      if self.publisher_id is None:
        self.publisher_id = ''
      if self.counter is None:
        self.counter = 0
      if self.publish_ts is None:
        self.publish_ts = 0
    else:
      self.tse_obj = []
      self.tsi_flg_cipv_lost = False
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
      length = len(self.tse_obj)
      buff.write(_struct_I.pack(length))
      for val1 in self.tse_obj:
        _x = val1
        buff.write(_get_struct_3I13f3iI5fifiIfiI().pack(_x.id, _x.obj_index, _x.confidence, _x.lon_pos_ccs, _x.lon_pos_vcs, _x.lon_pos_vcs_std, _x.lon_vel, _x.lon_vel_std, _x.lon_acc, _x.lat_pos_ccs, _x.lat_pos_vcs, _x.lat_pos_vcs_std, _x.lat_vel, _x.lat_vel_std, _x.lat_vel_ccs, _x.lat_acc, _x.status, _x.type, _x.valid, _x.age, _x.width, _x.length, _x.height, _x.phi_angle, _x.dphi_angle_rate, _x.fusion_source, _x.ttc, _x.blinker_info, _x.brake_lights, _x.prob_lane_change, _x.dirLaneChange, _x.age_in_path))
      _x = self
      buff.write(_get_struct_BQ().pack(_x.tsi_flg_cipv_lost, _x.publish_ptp_ts))
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
      if self.tse_obj is None:
        self.tse_obj = None
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.tse_obj = []
      for i in range(0, length):
        val1 = rospy_message_converter.msg.TgtObj()
        _x = val1
        start = end
        end += 128
        (_x.id, _x.obj_index, _x.confidence, _x.lon_pos_ccs, _x.lon_pos_vcs, _x.lon_pos_vcs_std, _x.lon_vel, _x.lon_vel_std, _x.lon_acc, _x.lat_pos_ccs, _x.lat_pos_vcs, _x.lat_pos_vcs_std, _x.lat_vel, _x.lat_vel_std, _x.lat_vel_ccs, _x.lat_acc, _x.status, _x.type, _x.valid, _x.age, _x.width, _x.length, _x.height, _x.phi_angle, _x.dphi_angle_rate, _x.fusion_source, _x.ttc, _x.blinker_info, _x.brake_lights, _x.prob_lane_change, _x.dirLaneChange, _x.age_in_path,) = _get_struct_3I13f3iI5fifiIfiI().unpack(str[start:end])
        self.tse_obj.append(val1)
      _x = self
      start = end
      end += 9
      (_x.tsi_flg_cipv_lost, _x.publish_ptp_ts,) = _get_struct_BQ().unpack(str[start:end])
      self.tsi_flg_cipv_lost = bool(self.tsi_flg_cipv_lost)
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
      length = len(self.tse_obj)
      buff.write(_struct_I.pack(length))
      for val1 in self.tse_obj:
        _x = val1
        buff.write(_get_struct_3I13f3iI5fifiIfiI().pack(_x.id, _x.obj_index, _x.confidence, _x.lon_pos_ccs, _x.lon_pos_vcs, _x.lon_pos_vcs_std, _x.lon_vel, _x.lon_vel_std, _x.lon_acc, _x.lat_pos_ccs, _x.lat_pos_vcs, _x.lat_pos_vcs_std, _x.lat_vel, _x.lat_vel_std, _x.lat_vel_ccs, _x.lat_acc, _x.status, _x.type, _x.valid, _x.age, _x.width, _x.length, _x.height, _x.phi_angle, _x.dphi_angle_rate, _x.fusion_source, _x.ttc, _x.blinker_info, _x.brake_lights, _x.prob_lane_change, _x.dirLaneChange, _x.age_in_path))
      _x = self
      buff.write(_get_struct_BQ().pack(_x.tsi_flg_cipv_lost, _x.publish_ptp_ts))
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
      if self.tse_obj is None:
        self.tse_obj = None
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.tse_obj = []
      for i in range(0, length):
        val1 = rospy_message_converter.msg.TgtObj()
        _x = val1
        start = end
        end += 128
        (_x.id, _x.obj_index, _x.confidence, _x.lon_pos_ccs, _x.lon_pos_vcs, _x.lon_pos_vcs_std, _x.lon_vel, _x.lon_vel_std, _x.lon_acc, _x.lat_pos_ccs, _x.lat_pos_vcs, _x.lat_pos_vcs_std, _x.lat_vel, _x.lat_vel_std, _x.lat_vel_ccs, _x.lat_acc, _x.status, _x.type, _x.valid, _x.age, _x.width, _x.length, _x.height, _x.phi_angle, _x.dphi_angle_rate, _x.fusion_source, _x.ttc, _x.blinker_info, _x.brake_lights, _x.prob_lane_change, _x.dirLaneChange, _x.age_in_path,) = _get_struct_3I13f3iI5fifiIfiI().unpack(str[start:end])
        self.tse_obj.append(val1)
      _x = self
      start = end
      end += 9
      (_x.tsi_flg_cipv_lost, _x.publish_ptp_ts,) = _get_struct_BQ().unpack(str[start:end])
      self.tsi_flg_cipv_lost = bool(self.tsi_flg_cipv_lost)
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
_struct_3I13f3iI5fifiIfiI = None
def _get_struct_3I13f3iI5fifiIfiI():
    global _struct_3I13f3iI5fifiIfiI
    if _struct_3I13f3iI5fifiIfiI is None:
        _struct_3I13f3iI5fifiIfiI = struct.Struct("<3I13f3iI5fifiIfiI")
    return _struct_3I13f3iI5fifiIfiI
_struct_BQ = None
def _get_struct_BQ():
    global _struct_BQ
    if _struct_BQ is None:
        _struct_BQ = struct.Struct("<BQ")
    return _struct_BQ

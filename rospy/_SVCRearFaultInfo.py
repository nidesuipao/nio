# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from rospy_message_converter/SVCRearFaultInfo.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class SVCRearFaultInfo(genpy.Message):
  _md5sum = "1a0675b96dc4ae32e471596eca388d5f"
  _type = "rospy_message_converter/SVCRearFaultInfo"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """bool FS_rain_3
bool FS_fog_3
bool FS_snow_3
bool FS_partialBlockage_3
bool FS_lowSun_3
bool FS_sunRay_3
bool FS_splashes_3
bool FS_frozenWindshield_3
bool FS_out_of_focus_3
bool FS_blurredImage_3
bool FS_Smeared_Halo_3
"""
  __slots__ = ['FS_rain_3','FS_fog_3','FS_snow_3','FS_partialBlockage_3','FS_lowSun_3','FS_sunRay_3','FS_splashes_3','FS_frozenWindshield_3','FS_out_of_focus_3','FS_blurredImage_3','FS_Smeared_Halo_3']
  _slot_types = ['bool','bool','bool','bool','bool','bool','bool','bool','bool','bool','bool']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       FS_rain_3,FS_fog_3,FS_snow_3,FS_partialBlockage_3,FS_lowSun_3,FS_sunRay_3,FS_splashes_3,FS_frozenWindshield_3,FS_out_of_focus_3,FS_blurredImage_3,FS_Smeared_Halo_3

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(SVCRearFaultInfo, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.FS_rain_3 is None:
        self.FS_rain_3 = False
      if self.FS_fog_3 is None:
        self.FS_fog_3 = False
      if self.FS_snow_3 is None:
        self.FS_snow_3 = False
      if self.FS_partialBlockage_3 is None:
        self.FS_partialBlockage_3 = False
      if self.FS_lowSun_3 is None:
        self.FS_lowSun_3 = False
      if self.FS_sunRay_3 is None:
        self.FS_sunRay_3 = False
      if self.FS_splashes_3 is None:
        self.FS_splashes_3 = False
      if self.FS_frozenWindshield_3 is None:
        self.FS_frozenWindshield_3 = False
      if self.FS_out_of_focus_3 is None:
        self.FS_out_of_focus_3 = False
      if self.FS_blurredImage_3 is None:
        self.FS_blurredImage_3 = False
      if self.FS_Smeared_Halo_3 is None:
        self.FS_Smeared_Halo_3 = False
    else:
      self.FS_rain_3 = False
      self.FS_fog_3 = False
      self.FS_snow_3 = False
      self.FS_partialBlockage_3 = False
      self.FS_lowSun_3 = False
      self.FS_sunRay_3 = False
      self.FS_splashes_3 = False
      self.FS_frozenWindshield_3 = False
      self.FS_out_of_focus_3 = False
      self.FS_blurredImage_3 = False
      self.FS_Smeared_Halo_3 = False

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
      buff.write(_get_struct_11B().pack(_x.FS_rain_3, _x.FS_fog_3, _x.FS_snow_3, _x.FS_partialBlockage_3, _x.FS_lowSun_3, _x.FS_sunRay_3, _x.FS_splashes_3, _x.FS_frozenWindshield_3, _x.FS_out_of_focus_3, _x.FS_blurredImage_3, _x.FS_Smeared_Halo_3))
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
      end += 11
      (_x.FS_rain_3, _x.FS_fog_3, _x.FS_snow_3, _x.FS_partialBlockage_3, _x.FS_lowSun_3, _x.FS_sunRay_3, _x.FS_splashes_3, _x.FS_frozenWindshield_3, _x.FS_out_of_focus_3, _x.FS_blurredImage_3, _x.FS_Smeared_Halo_3,) = _get_struct_11B().unpack(str[start:end])
      self.FS_rain_3 = bool(self.FS_rain_3)
      self.FS_fog_3 = bool(self.FS_fog_3)
      self.FS_snow_3 = bool(self.FS_snow_3)
      self.FS_partialBlockage_3 = bool(self.FS_partialBlockage_3)
      self.FS_lowSun_3 = bool(self.FS_lowSun_3)
      self.FS_sunRay_3 = bool(self.FS_sunRay_3)
      self.FS_splashes_3 = bool(self.FS_splashes_3)
      self.FS_frozenWindshield_3 = bool(self.FS_frozenWindshield_3)
      self.FS_out_of_focus_3 = bool(self.FS_out_of_focus_3)
      self.FS_blurredImage_3 = bool(self.FS_blurredImage_3)
      self.FS_Smeared_Halo_3 = bool(self.FS_Smeared_Halo_3)
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
      buff.write(_get_struct_11B().pack(_x.FS_rain_3, _x.FS_fog_3, _x.FS_snow_3, _x.FS_partialBlockage_3, _x.FS_lowSun_3, _x.FS_sunRay_3, _x.FS_splashes_3, _x.FS_frozenWindshield_3, _x.FS_out_of_focus_3, _x.FS_blurredImage_3, _x.FS_Smeared_Halo_3))
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
      end += 11
      (_x.FS_rain_3, _x.FS_fog_3, _x.FS_snow_3, _x.FS_partialBlockage_3, _x.FS_lowSun_3, _x.FS_sunRay_3, _x.FS_splashes_3, _x.FS_frozenWindshield_3, _x.FS_out_of_focus_3, _x.FS_blurredImage_3, _x.FS_Smeared_Halo_3,) = _get_struct_11B().unpack(str[start:end])
      self.FS_rain_3 = bool(self.FS_rain_3)
      self.FS_fog_3 = bool(self.FS_fog_3)
      self.FS_snow_3 = bool(self.FS_snow_3)
      self.FS_partialBlockage_3 = bool(self.FS_partialBlockage_3)
      self.FS_lowSun_3 = bool(self.FS_lowSun_3)
      self.FS_sunRay_3 = bool(self.FS_sunRay_3)
      self.FS_splashes_3 = bool(self.FS_splashes_3)
      self.FS_frozenWindshield_3 = bool(self.FS_frozenWindshield_3)
      self.FS_out_of_focus_3 = bool(self.FS_out_of_focus_3)
      self.FS_blurredImage_3 = bool(self.FS_blurredImage_3)
      self.FS_Smeared_Halo_3 = bool(self.FS_Smeared_Halo_3)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_11B = None
def _get_struct_11B():
    global _struct_11B
    if _struct_11B is None:
        _struct_11B = struct.Struct("<11B")
    return _struct_11B

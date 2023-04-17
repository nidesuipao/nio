# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from rospy_message_converter/DMSAdcFimInfo.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class DMSAdcFimInfo(genpy.Message):
  _md5sum = "02741287e28793daabe103d78fe042a5"
  _type = "rospy_message_converter/DMSAdcFimInfo"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """bool FIM_DMSPhysicalLinkage_Error
bool FIM_DMS_License_NotAvailable
bool FIM_DMS_Function_NotAvailable
bool FIM_DMS_Camera_Occluded
bool FIM_DMS_No_Image_Recv
"""
  __slots__ = ['FIM_DMSPhysicalLinkage_Error','FIM_DMS_License_NotAvailable','FIM_DMS_Function_NotAvailable','FIM_DMS_Camera_Occluded','FIM_DMS_No_Image_Recv']
  _slot_types = ['bool','bool','bool','bool','bool']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       FIM_DMSPhysicalLinkage_Error,FIM_DMS_License_NotAvailable,FIM_DMS_Function_NotAvailable,FIM_DMS_Camera_Occluded,FIM_DMS_No_Image_Recv

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(DMSAdcFimInfo, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.FIM_DMSPhysicalLinkage_Error is None:
        self.FIM_DMSPhysicalLinkage_Error = False
      if self.FIM_DMS_License_NotAvailable is None:
        self.FIM_DMS_License_NotAvailable = False
      if self.FIM_DMS_Function_NotAvailable is None:
        self.FIM_DMS_Function_NotAvailable = False
      if self.FIM_DMS_Camera_Occluded is None:
        self.FIM_DMS_Camera_Occluded = False
      if self.FIM_DMS_No_Image_Recv is None:
        self.FIM_DMS_No_Image_Recv = False
    else:
      self.FIM_DMSPhysicalLinkage_Error = False
      self.FIM_DMS_License_NotAvailable = False
      self.FIM_DMS_Function_NotAvailable = False
      self.FIM_DMS_Camera_Occluded = False
      self.FIM_DMS_No_Image_Recv = False

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
      buff.write(_get_struct_5B().pack(_x.FIM_DMSPhysicalLinkage_Error, _x.FIM_DMS_License_NotAvailable, _x.FIM_DMS_Function_NotAvailable, _x.FIM_DMS_Camera_Occluded, _x.FIM_DMS_No_Image_Recv))
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
      end += 5
      (_x.FIM_DMSPhysicalLinkage_Error, _x.FIM_DMS_License_NotAvailable, _x.FIM_DMS_Function_NotAvailable, _x.FIM_DMS_Camera_Occluded, _x.FIM_DMS_No_Image_Recv,) = _get_struct_5B().unpack(str[start:end])
      self.FIM_DMSPhysicalLinkage_Error = bool(self.FIM_DMSPhysicalLinkage_Error)
      self.FIM_DMS_License_NotAvailable = bool(self.FIM_DMS_License_NotAvailable)
      self.FIM_DMS_Function_NotAvailable = bool(self.FIM_DMS_Function_NotAvailable)
      self.FIM_DMS_Camera_Occluded = bool(self.FIM_DMS_Camera_Occluded)
      self.FIM_DMS_No_Image_Recv = bool(self.FIM_DMS_No_Image_Recv)
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
      buff.write(_get_struct_5B().pack(_x.FIM_DMSPhysicalLinkage_Error, _x.FIM_DMS_License_NotAvailable, _x.FIM_DMS_Function_NotAvailable, _x.FIM_DMS_Camera_Occluded, _x.FIM_DMS_No_Image_Recv))
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
      end += 5
      (_x.FIM_DMSPhysicalLinkage_Error, _x.FIM_DMS_License_NotAvailable, _x.FIM_DMS_Function_NotAvailable, _x.FIM_DMS_Camera_Occluded, _x.FIM_DMS_No_Image_Recv,) = _get_struct_5B().unpack(str[start:end])
      self.FIM_DMSPhysicalLinkage_Error = bool(self.FIM_DMSPhysicalLinkage_Error)
      self.FIM_DMS_License_NotAvailable = bool(self.FIM_DMS_License_NotAvailable)
      self.FIM_DMS_Function_NotAvailable = bool(self.FIM_DMS_Function_NotAvailable)
      self.FIM_DMS_Camera_Occluded = bool(self.FIM_DMS_Camera_Occluded)
      self.FIM_DMS_No_Image_Recv = bool(self.FIM_DMS_No_Image_Recv)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_5B = None
def _get_struct_5B():
    global _struct_5B
    if _struct_5B is None:
        _struct_5B = struct.Struct("<5B")
    return _struct_5B

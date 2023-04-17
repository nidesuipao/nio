# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from rospy_message_converter/RADFRFaultInfo.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class RADFRFaultInfo(genpy.Message):
  _md5sum = "3597362ca02ccd4c654ea97e61ad01e9"
  _type = "rospy_message_converter/RADFRFaultInfo"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """bool FrontSide_CAN_RADFR_LossCom
bool RADFR_Failure
bool FrontRAD_CAN_RADFR_InternalFault
bool FrontRAD_CAN_RADFR_AlignmentIncomplete
bool FrontRAD_CAN_RADFR_Voltage_Above_Threshold
bool FrontRAD_CAN_RADFR_Voltage_Below_Threshold
bool FrontRAD_CAN_RADFR_Temp_High_Fault
bool FrontRAD_CAN_RADFR_Alignment_Out_of_Range
bool FrontRAD_CAN_RADFR_LossComm_with_ADC
bool FrontRAD_CAN_RADFR_Invalid_Data_from_ADC
bool FrontRAD_CAN_RADFR_Blindness
bool FrontRAD_CAN_RADFR_MRR_Detection_001_006_MsgError
bool FrontRAD_CAN_RADFR_MRR_Detection_007_012_MsgError
bool FrontRAD_CAN_RADFR_MRR_Detection_013_018_MsgError
bool FrontRAD_CAN_RADFR_MRR_Detection_019_024_MsgError
bool FrontRAD_CAN_RADFR_MRR_Detection_025_030_MsgError
bool FrontRAD_CAN_RADFR_MRR_Detection_031_036_MsgError
bool FrontRAD_CAN_RADFR_MRR_Detection_037_042_MsgError
bool FrontRAD_CAN_RADFR_MRR_Detection_043_048_MsgError
bool FrontRAD_CAN_RADFR_MRR_Detection_049_054_MsgError
bool FrontRAD_CAN_RADFR_MRR_Detection_055_060_MsgError
bool FrontRAD_CAN_RADFR_MRR_Detection_061_064_MsgError
bool FrontRAD_CAN_RADFR_MRR_Header_AlignmentState_MsgError
bool FrontRAD_CAN_RADFR_MRR_Header_SensorCoverage_MsgError
bool FrontRAD_CAN_RADFR_MRR_Header_Timestamps_MsgError
bool FrontRAD_CAN_RADFR_MRR_CANVersion_MsgError
bool FrontRAD_CAN_RADFR_MRR_Status_Radar_MsgError
"""
  __slots__ = ['FrontSide_CAN_RADFR_LossCom','RADFR_Failure','FrontRAD_CAN_RADFR_InternalFault','FrontRAD_CAN_RADFR_AlignmentIncomplete','FrontRAD_CAN_RADFR_Voltage_Above_Threshold','FrontRAD_CAN_RADFR_Voltage_Below_Threshold','FrontRAD_CAN_RADFR_Temp_High_Fault','FrontRAD_CAN_RADFR_Alignment_Out_of_Range','FrontRAD_CAN_RADFR_LossComm_with_ADC','FrontRAD_CAN_RADFR_Invalid_Data_from_ADC','FrontRAD_CAN_RADFR_Blindness','FrontRAD_CAN_RADFR_MRR_Detection_001_006_MsgError','FrontRAD_CAN_RADFR_MRR_Detection_007_012_MsgError','FrontRAD_CAN_RADFR_MRR_Detection_013_018_MsgError','FrontRAD_CAN_RADFR_MRR_Detection_019_024_MsgError','FrontRAD_CAN_RADFR_MRR_Detection_025_030_MsgError','FrontRAD_CAN_RADFR_MRR_Detection_031_036_MsgError','FrontRAD_CAN_RADFR_MRR_Detection_037_042_MsgError','FrontRAD_CAN_RADFR_MRR_Detection_043_048_MsgError','FrontRAD_CAN_RADFR_MRR_Detection_049_054_MsgError','FrontRAD_CAN_RADFR_MRR_Detection_055_060_MsgError','FrontRAD_CAN_RADFR_MRR_Detection_061_064_MsgError','FrontRAD_CAN_RADFR_MRR_Header_AlignmentState_MsgError','FrontRAD_CAN_RADFR_MRR_Header_SensorCoverage_MsgError','FrontRAD_CAN_RADFR_MRR_Header_Timestamps_MsgError','FrontRAD_CAN_RADFR_MRR_CANVersion_MsgError','FrontRAD_CAN_RADFR_MRR_Status_Radar_MsgError']
  _slot_types = ['bool','bool','bool','bool','bool','bool','bool','bool','bool','bool','bool','bool','bool','bool','bool','bool','bool','bool','bool','bool','bool','bool','bool','bool','bool','bool','bool']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       FrontSide_CAN_RADFR_LossCom,RADFR_Failure,FrontRAD_CAN_RADFR_InternalFault,FrontRAD_CAN_RADFR_AlignmentIncomplete,FrontRAD_CAN_RADFR_Voltage_Above_Threshold,FrontRAD_CAN_RADFR_Voltage_Below_Threshold,FrontRAD_CAN_RADFR_Temp_High_Fault,FrontRAD_CAN_RADFR_Alignment_Out_of_Range,FrontRAD_CAN_RADFR_LossComm_with_ADC,FrontRAD_CAN_RADFR_Invalid_Data_from_ADC,FrontRAD_CAN_RADFR_Blindness,FrontRAD_CAN_RADFR_MRR_Detection_001_006_MsgError,FrontRAD_CAN_RADFR_MRR_Detection_007_012_MsgError,FrontRAD_CAN_RADFR_MRR_Detection_013_018_MsgError,FrontRAD_CAN_RADFR_MRR_Detection_019_024_MsgError,FrontRAD_CAN_RADFR_MRR_Detection_025_030_MsgError,FrontRAD_CAN_RADFR_MRR_Detection_031_036_MsgError,FrontRAD_CAN_RADFR_MRR_Detection_037_042_MsgError,FrontRAD_CAN_RADFR_MRR_Detection_043_048_MsgError,FrontRAD_CAN_RADFR_MRR_Detection_049_054_MsgError,FrontRAD_CAN_RADFR_MRR_Detection_055_060_MsgError,FrontRAD_CAN_RADFR_MRR_Detection_061_064_MsgError,FrontRAD_CAN_RADFR_MRR_Header_AlignmentState_MsgError,FrontRAD_CAN_RADFR_MRR_Header_SensorCoverage_MsgError,FrontRAD_CAN_RADFR_MRR_Header_Timestamps_MsgError,FrontRAD_CAN_RADFR_MRR_CANVersion_MsgError,FrontRAD_CAN_RADFR_MRR_Status_Radar_MsgError

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(RADFRFaultInfo, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.FrontSide_CAN_RADFR_LossCom is None:
        self.FrontSide_CAN_RADFR_LossCom = False
      if self.RADFR_Failure is None:
        self.RADFR_Failure = False
      if self.FrontRAD_CAN_RADFR_InternalFault is None:
        self.FrontRAD_CAN_RADFR_InternalFault = False
      if self.FrontRAD_CAN_RADFR_AlignmentIncomplete is None:
        self.FrontRAD_CAN_RADFR_AlignmentIncomplete = False
      if self.FrontRAD_CAN_RADFR_Voltage_Above_Threshold is None:
        self.FrontRAD_CAN_RADFR_Voltage_Above_Threshold = False
      if self.FrontRAD_CAN_RADFR_Voltage_Below_Threshold is None:
        self.FrontRAD_CAN_RADFR_Voltage_Below_Threshold = False
      if self.FrontRAD_CAN_RADFR_Temp_High_Fault is None:
        self.FrontRAD_CAN_RADFR_Temp_High_Fault = False
      if self.FrontRAD_CAN_RADFR_Alignment_Out_of_Range is None:
        self.FrontRAD_CAN_RADFR_Alignment_Out_of_Range = False
      if self.FrontRAD_CAN_RADFR_LossComm_with_ADC is None:
        self.FrontRAD_CAN_RADFR_LossComm_with_ADC = False
      if self.FrontRAD_CAN_RADFR_Invalid_Data_from_ADC is None:
        self.FrontRAD_CAN_RADFR_Invalid_Data_from_ADC = False
      if self.FrontRAD_CAN_RADFR_Blindness is None:
        self.FrontRAD_CAN_RADFR_Blindness = False
      if self.FrontRAD_CAN_RADFR_MRR_Detection_001_006_MsgError is None:
        self.FrontRAD_CAN_RADFR_MRR_Detection_001_006_MsgError = False
      if self.FrontRAD_CAN_RADFR_MRR_Detection_007_012_MsgError is None:
        self.FrontRAD_CAN_RADFR_MRR_Detection_007_012_MsgError = False
      if self.FrontRAD_CAN_RADFR_MRR_Detection_013_018_MsgError is None:
        self.FrontRAD_CAN_RADFR_MRR_Detection_013_018_MsgError = False
      if self.FrontRAD_CAN_RADFR_MRR_Detection_019_024_MsgError is None:
        self.FrontRAD_CAN_RADFR_MRR_Detection_019_024_MsgError = False
      if self.FrontRAD_CAN_RADFR_MRR_Detection_025_030_MsgError is None:
        self.FrontRAD_CAN_RADFR_MRR_Detection_025_030_MsgError = False
      if self.FrontRAD_CAN_RADFR_MRR_Detection_031_036_MsgError is None:
        self.FrontRAD_CAN_RADFR_MRR_Detection_031_036_MsgError = False
      if self.FrontRAD_CAN_RADFR_MRR_Detection_037_042_MsgError is None:
        self.FrontRAD_CAN_RADFR_MRR_Detection_037_042_MsgError = False
      if self.FrontRAD_CAN_RADFR_MRR_Detection_043_048_MsgError is None:
        self.FrontRAD_CAN_RADFR_MRR_Detection_043_048_MsgError = False
      if self.FrontRAD_CAN_RADFR_MRR_Detection_049_054_MsgError is None:
        self.FrontRAD_CAN_RADFR_MRR_Detection_049_054_MsgError = False
      if self.FrontRAD_CAN_RADFR_MRR_Detection_055_060_MsgError is None:
        self.FrontRAD_CAN_RADFR_MRR_Detection_055_060_MsgError = False
      if self.FrontRAD_CAN_RADFR_MRR_Detection_061_064_MsgError is None:
        self.FrontRAD_CAN_RADFR_MRR_Detection_061_064_MsgError = False
      if self.FrontRAD_CAN_RADFR_MRR_Header_AlignmentState_MsgError is None:
        self.FrontRAD_CAN_RADFR_MRR_Header_AlignmentState_MsgError = False
      if self.FrontRAD_CAN_RADFR_MRR_Header_SensorCoverage_MsgError is None:
        self.FrontRAD_CAN_RADFR_MRR_Header_SensorCoverage_MsgError = False
      if self.FrontRAD_CAN_RADFR_MRR_Header_Timestamps_MsgError is None:
        self.FrontRAD_CAN_RADFR_MRR_Header_Timestamps_MsgError = False
      if self.FrontRAD_CAN_RADFR_MRR_CANVersion_MsgError is None:
        self.FrontRAD_CAN_RADFR_MRR_CANVersion_MsgError = False
      if self.FrontRAD_CAN_RADFR_MRR_Status_Radar_MsgError is None:
        self.FrontRAD_CAN_RADFR_MRR_Status_Radar_MsgError = False
    else:
      self.FrontSide_CAN_RADFR_LossCom = False
      self.RADFR_Failure = False
      self.FrontRAD_CAN_RADFR_InternalFault = False
      self.FrontRAD_CAN_RADFR_AlignmentIncomplete = False
      self.FrontRAD_CAN_RADFR_Voltage_Above_Threshold = False
      self.FrontRAD_CAN_RADFR_Voltage_Below_Threshold = False
      self.FrontRAD_CAN_RADFR_Temp_High_Fault = False
      self.FrontRAD_CAN_RADFR_Alignment_Out_of_Range = False
      self.FrontRAD_CAN_RADFR_LossComm_with_ADC = False
      self.FrontRAD_CAN_RADFR_Invalid_Data_from_ADC = False
      self.FrontRAD_CAN_RADFR_Blindness = False
      self.FrontRAD_CAN_RADFR_MRR_Detection_001_006_MsgError = False
      self.FrontRAD_CAN_RADFR_MRR_Detection_007_012_MsgError = False
      self.FrontRAD_CAN_RADFR_MRR_Detection_013_018_MsgError = False
      self.FrontRAD_CAN_RADFR_MRR_Detection_019_024_MsgError = False
      self.FrontRAD_CAN_RADFR_MRR_Detection_025_030_MsgError = False
      self.FrontRAD_CAN_RADFR_MRR_Detection_031_036_MsgError = False
      self.FrontRAD_CAN_RADFR_MRR_Detection_037_042_MsgError = False
      self.FrontRAD_CAN_RADFR_MRR_Detection_043_048_MsgError = False
      self.FrontRAD_CAN_RADFR_MRR_Detection_049_054_MsgError = False
      self.FrontRAD_CAN_RADFR_MRR_Detection_055_060_MsgError = False
      self.FrontRAD_CAN_RADFR_MRR_Detection_061_064_MsgError = False
      self.FrontRAD_CAN_RADFR_MRR_Header_AlignmentState_MsgError = False
      self.FrontRAD_CAN_RADFR_MRR_Header_SensorCoverage_MsgError = False
      self.FrontRAD_CAN_RADFR_MRR_Header_Timestamps_MsgError = False
      self.FrontRAD_CAN_RADFR_MRR_CANVersion_MsgError = False
      self.FrontRAD_CAN_RADFR_MRR_Status_Radar_MsgError = False

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
      buff.write(_get_struct_27B().pack(_x.FrontSide_CAN_RADFR_LossCom, _x.RADFR_Failure, _x.FrontRAD_CAN_RADFR_InternalFault, _x.FrontRAD_CAN_RADFR_AlignmentIncomplete, _x.FrontRAD_CAN_RADFR_Voltage_Above_Threshold, _x.FrontRAD_CAN_RADFR_Voltage_Below_Threshold, _x.FrontRAD_CAN_RADFR_Temp_High_Fault, _x.FrontRAD_CAN_RADFR_Alignment_Out_of_Range, _x.FrontRAD_CAN_RADFR_LossComm_with_ADC, _x.FrontRAD_CAN_RADFR_Invalid_Data_from_ADC, _x.FrontRAD_CAN_RADFR_Blindness, _x.FrontRAD_CAN_RADFR_MRR_Detection_001_006_MsgError, _x.FrontRAD_CAN_RADFR_MRR_Detection_007_012_MsgError, _x.FrontRAD_CAN_RADFR_MRR_Detection_013_018_MsgError, _x.FrontRAD_CAN_RADFR_MRR_Detection_019_024_MsgError, _x.FrontRAD_CAN_RADFR_MRR_Detection_025_030_MsgError, _x.FrontRAD_CAN_RADFR_MRR_Detection_031_036_MsgError, _x.FrontRAD_CAN_RADFR_MRR_Detection_037_042_MsgError, _x.FrontRAD_CAN_RADFR_MRR_Detection_043_048_MsgError, _x.FrontRAD_CAN_RADFR_MRR_Detection_049_054_MsgError, _x.FrontRAD_CAN_RADFR_MRR_Detection_055_060_MsgError, _x.FrontRAD_CAN_RADFR_MRR_Detection_061_064_MsgError, _x.FrontRAD_CAN_RADFR_MRR_Header_AlignmentState_MsgError, _x.FrontRAD_CAN_RADFR_MRR_Header_SensorCoverage_MsgError, _x.FrontRAD_CAN_RADFR_MRR_Header_Timestamps_MsgError, _x.FrontRAD_CAN_RADFR_MRR_CANVersion_MsgError, _x.FrontRAD_CAN_RADFR_MRR_Status_Radar_MsgError))
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
      end += 27
      (_x.FrontSide_CAN_RADFR_LossCom, _x.RADFR_Failure, _x.FrontRAD_CAN_RADFR_InternalFault, _x.FrontRAD_CAN_RADFR_AlignmentIncomplete, _x.FrontRAD_CAN_RADFR_Voltage_Above_Threshold, _x.FrontRAD_CAN_RADFR_Voltage_Below_Threshold, _x.FrontRAD_CAN_RADFR_Temp_High_Fault, _x.FrontRAD_CAN_RADFR_Alignment_Out_of_Range, _x.FrontRAD_CAN_RADFR_LossComm_with_ADC, _x.FrontRAD_CAN_RADFR_Invalid_Data_from_ADC, _x.FrontRAD_CAN_RADFR_Blindness, _x.FrontRAD_CAN_RADFR_MRR_Detection_001_006_MsgError, _x.FrontRAD_CAN_RADFR_MRR_Detection_007_012_MsgError, _x.FrontRAD_CAN_RADFR_MRR_Detection_013_018_MsgError, _x.FrontRAD_CAN_RADFR_MRR_Detection_019_024_MsgError, _x.FrontRAD_CAN_RADFR_MRR_Detection_025_030_MsgError, _x.FrontRAD_CAN_RADFR_MRR_Detection_031_036_MsgError, _x.FrontRAD_CAN_RADFR_MRR_Detection_037_042_MsgError, _x.FrontRAD_CAN_RADFR_MRR_Detection_043_048_MsgError, _x.FrontRAD_CAN_RADFR_MRR_Detection_049_054_MsgError, _x.FrontRAD_CAN_RADFR_MRR_Detection_055_060_MsgError, _x.FrontRAD_CAN_RADFR_MRR_Detection_061_064_MsgError, _x.FrontRAD_CAN_RADFR_MRR_Header_AlignmentState_MsgError, _x.FrontRAD_CAN_RADFR_MRR_Header_SensorCoverage_MsgError, _x.FrontRAD_CAN_RADFR_MRR_Header_Timestamps_MsgError, _x.FrontRAD_CAN_RADFR_MRR_CANVersion_MsgError, _x.FrontRAD_CAN_RADFR_MRR_Status_Radar_MsgError,) = _get_struct_27B().unpack(str[start:end])
      self.FrontSide_CAN_RADFR_LossCom = bool(self.FrontSide_CAN_RADFR_LossCom)
      self.RADFR_Failure = bool(self.RADFR_Failure)
      self.FrontRAD_CAN_RADFR_InternalFault = bool(self.FrontRAD_CAN_RADFR_InternalFault)
      self.FrontRAD_CAN_RADFR_AlignmentIncomplete = bool(self.FrontRAD_CAN_RADFR_AlignmentIncomplete)
      self.FrontRAD_CAN_RADFR_Voltage_Above_Threshold = bool(self.FrontRAD_CAN_RADFR_Voltage_Above_Threshold)
      self.FrontRAD_CAN_RADFR_Voltage_Below_Threshold = bool(self.FrontRAD_CAN_RADFR_Voltage_Below_Threshold)
      self.FrontRAD_CAN_RADFR_Temp_High_Fault = bool(self.FrontRAD_CAN_RADFR_Temp_High_Fault)
      self.FrontRAD_CAN_RADFR_Alignment_Out_of_Range = bool(self.FrontRAD_CAN_RADFR_Alignment_Out_of_Range)
      self.FrontRAD_CAN_RADFR_LossComm_with_ADC = bool(self.FrontRAD_CAN_RADFR_LossComm_with_ADC)
      self.FrontRAD_CAN_RADFR_Invalid_Data_from_ADC = bool(self.FrontRAD_CAN_RADFR_Invalid_Data_from_ADC)
      self.FrontRAD_CAN_RADFR_Blindness = bool(self.FrontRAD_CAN_RADFR_Blindness)
      self.FrontRAD_CAN_RADFR_MRR_Detection_001_006_MsgError = bool(self.FrontRAD_CAN_RADFR_MRR_Detection_001_006_MsgError)
      self.FrontRAD_CAN_RADFR_MRR_Detection_007_012_MsgError = bool(self.FrontRAD_CAN_RADFR_MRR_Detection_007_012_MsgError)
      self.FrontRAD_CAN_RADFR_MRR_Detection_013_018_MsgError = bool(self.FrontRAD_CAN_RADFR_MRR_Detection_013_018_MsgError)
      self.FrontRAD_CAN_RADFR_MRR_Detection_019_024_MsgError = bool(self.FrontRAD_CAN_RADFR_MRR_Detection_019_024_MsgError)
      self.FrontRAD_CAN_RADFR_MRR_Detection_025_030_MsgError = bool(self.FrontRAD_CAN_RADFR_MRR_Detection_025_030_MsgError)
      self.FrontRAD_CAN_RADFR_MRR_Detection_031_036_MsgError = bool(self.FrontRAD_CAN_RADFR_MRR_Detection_031_036_MsgError)
      self.FrontRAD_CAN_RADFR_MRR_Detection_037_042_MsgError = bool(self.FrontRAD_CAN_RADFR_MRR_Detection_037_042_MsgError)
      self.FrontRAD_CAN_RADFR_MRR_Detection_043_048_MsgError = bool(self.FrontRAD_CAN_RADFR_MRR_Detection_043_048_MsgError)
      self.FrontRAD_CAN_RADFR_MRR_Detection_049_054_MsgError = bool(self.FrontRAD_CAN_RADFR_MRR_Detection_049_054_MsgError)
      self.FrontRAD_CAN_RADFR_MRR_Detection_055_060_MsgError = bool(self.FrontRAD_CAN_RADFR_MRR_Detection_055_060_MsgError)
      self.FrontRAD_CAN_RADFR_MRR_Detection_061_064_MsgError = bool(self.FrontRAD_CAN_RADFR_MRR_Detection_061_064_MsgError)
      self.FrontRAD_CAN_RADFR_MRR_Header_AlignmentState_MsgError = bool(self.FrontRAD_CAN_RADFR_MRR_Header_AlignmentState_MsgError)
      self.FrontRAD_CAN_RADFR_MRR_Header_SensorCoverage_MsgError = bool(self.FrontRAD_CAN_RADFR_MRR_Header_SensorCoverage_MsgError)
      self.FrontRAD_CAN_RADFR_MRR_Header_Timestamps_MsgError = bool(self.FrontRAD_CAN_RADFR_MRR_Header_Timestamps_MsgError)
      self.FrontRAD_CAN_RADFR_MRR_CANVersion_MsgError = bool(self.FrontRAD_CAN_RADFR_MRR_CANVersion_MsgError)
      self.FrontRAD_CAN_RADFR_MRR_Status_Radar_MsgError = bool(self.FrontRAD_CAN_RADFR_MRR_Status_Radar_MsgError)
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
      buff.write(_get_struct_27B().pack(_x.FrontSide_CAN_RADFR_LossCom, _x.RADFR_Failure, _x.FrontRAD_CAN_RADFR_InternalFault, _x.FrontRAD_CAN_RADFR_AlignmentIncomplete, _x.FrontRAD_CAN_RADFR_Voltage_Above_Threshold, _x.FrontRAD_CAN_RADFR_Voltage_Below_Threshold, _x.FrontRAD_CAN_RADFR_Temp_High_Fault, _x.FrontRAD_CAN_RADFR_Alignment_Out_of_Range, _x.FrontRAD_CAN_RADFR_LossComm_with_ADC, _x.FrontRAD_CAN_RADFR_Invalid_Data_from_ADC, _x.FrontRAD_CAN_RADFR_Blindness, _x.FrontRAD_CAN_RADFR_MRR_Detection_001_006_MsgError, _x.FrontRAD_CAN_RADFR_MRR_Detection_007_012_MsgError, _x.FrontRAD_CAN_RADFR_MRR_Detection_013_018_MsgError, _x.FrontRAD_CAN_RADFR_MRR_Detection_019_024_MsgError, _x.FrontRAD_CAN_RADFR_MRR_Detection_025_030_MsgError, _x.FrontRAD_CAN_RADFR_MRR_Detection_031_036_MsgError, _x.FrontRAD_CAN_RADFR_MRR_Detection_037_042_MsgError, _x.FrontRAD_CAN_RADFR_MRR_Detection_043_048_MsgError, _x.FrontRAD_CAN_RADFR_MRR_Detection_049_054_MsgError, _x.FrontRAD_CAN_RADFR_MRR_Detection_055_060_MsgError, _x.FrontRAD_CAN_RADFR_MRR_Detection_061_064_MsgError, _x.FrontRAD_CAN_RADFR_MRR_Header_AlignmentState_MsgError, _x.FrontRAD_CAN_RADFR_MRR_Header_SensorCoverage_MsgError, _x.FrontRAD_CAN_RADFR_MRR_Header_Timestamps_MsgError, _x.FrontRAD_CAN_RADFR_MRR_CANVersion_MsgError, _x.FrontRAD_CAN_RADFR_MRR_Status_Radar_MsgError))
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
      end += 27
      (_x.FrontSide_CAN_RADFR_LossCom, _x.RADFR_Failure, _x.FrontRAD_CAN_RADFR_InternalFault, _x.FrontRAD_CAN_RADFR_AlignmentIncomplete, _x.FrontRAD_CAN_RADFR_Voltage_Above_Threshold, _x.FrontRAD_CAN_RADFR_Voltage_Below_Threshold, _x.FrontRAD_CAN_RADFR_Temp_High_Fault, _x.FrontRAD_CAN_RADFR_Alignment_Out_of_Range, _x.FrontRAD_CAN_RADFR_LossComm_with_ADC, _x.FrontRAD_CAN_RADFR_Invalid_Data_from_ADC, _x.FrontRAD_CAN_RADFR_Blindness, _x.FrontRAD_CAN_RADFR_MRR_Detection_001_006_MsgError, _x.FrontRAD_CAN_RADFR_MRR_Detection_007_012_MsgError, _x.FrontRAD_CAN_RADFR_MRR_Detection_013_018_MsgError, _x.FrontRAD_CAN_RADFR_MRR_Detection_019_024_MsgError, _x.FrontRAD_CAN_RADFR_MRR_Detection_025_030_MsgError, _x.FrontRAD_CAN_RADFR_MRR_Detection_031_036_MsgError, _x.FrontRAD_CAN_RADFR_MRR_Detection_037_042_MsgError, _x.FrontRAD_CAN_RADFR_MRR_Detection_043_048_MsgError, _x.FrontRAD_CAN_RADFR_MRR_Detection_049_054_MsgError, _x.FrontRAD_CAN_RADFR_MRR_Detection_055_060_MsgError, _x.FrontRAD_CAN_RADFR_MRR_Detection_061_064_MsgError, _x.FrontRAD_CAN_RADFR_MRR_Header_AlignmentState_MsgError, _x.FrontRAD_CAN_RADFR_MRR_Header_SensorCoverage_MsgError, _x.FrontRAD_CAN_RADFR_MRR_Header_Timestamps_MsgError, _x.FrontRAD_CAN_RADFR_MRR_CANVersion_MsgError, _x.FrontRAD_CAN_RADFR_MRR_Status_Radar_MsgError,) = _get_struct_27B().unpack(str[start:end])
      self.FrontSide_CAN_RADFR_LossCom = bool(self.FrontSide_CAN_RADFR_LossCom)
      self.RADFR_Failure = bool(self.RADFR_Failure)
      self.FrontRAD_CAN_RADFR_InternalFault = bool(self.FrontRAD_CAN_RADFR_InternalFault)
      self.FrontRAD_CAN_RADFR_AlignmentIncomplete = bool(self.FrontRAD_CAN_RADFR_AlignmentIncomplete)
      self.FrontRAD_CAN_RADFR_Voltage_Above_Threshold = bool(self.FrontRAD_CAN_RADFR_Voltage_Above_Threshold)
      self.FrontRAD_CAN_RADFR_Voltage_Below_Threshold = bool(self.FrontRAD_CAN_RADFR_Voltage_Below_Threshold)
      self.FrontRAD_CAN_RADFR_Temp_High_Fault = bool(self.FrontRAD_CAN_RADFR_Temp_High_Fault)
      self.FrontRAD_CAN_RADFR_Alignment_Out_of_Range = bool(self.FrontRAD_CAN_RADFR_Alignment_Out_of_Range)
      self.FrontRAD_CAN_RADFR_LossComm_with_ADC = bool(self.FrontRAD_CAN_RADFR_LossComm_with_ADC)
      self.FrontRAD_CAN_RADFR_Invalid_Data_from_ADC = bool(self.FrontRAD_CAN_RADFR_Invalid_Data_from_ADC)
      self.FrontRAD_CAN_RADFR_Blindness = bool(self.FrontRAD_CAN_RADFR_Blindness)
      self.FrontRAD_CAN_RADFR_MRR_Detection_001_006_MsgError = bool(self.FrontRAD_CAN_RADFR_MRR_Detection_001_006_MsgError)
      self.FrontRAD_CAN_RADFR_MRR_Detection_007_012_MsgError = bool(self.FrontRAD_CAN_RADFR_MRR_Detection_007_012_MsgError)
      self.FrontRAD_CAN_RADFR_MRR_Detection_013_018_MsgError = bool(self.FrontRAD_CAN_RADFR_MRR_Detection_013_018_MsgError)
      self.FrontRAD_CAN_RADFR_MRR_Detection_019_024_MsgError = bool(self.FrontRAD_CAN_RADFR_MRR_Detection_019_024_MsgError)
      self.FrontRAD_CAN_RADFR_MRR_Detection_025_030_MsgError = bool(self.FrontRAD_CAN_RADFR_MRR_Detection_025_030_MsgError)
      self.FrontRAD_CAN_RADFR_MRR_Detection_031_036_MsgError = bool(self.FrontRAD_CAN_RADFR_MRR_Detection_031_036_MsgError)
      self.FrontRAD_CAN_RADFR_MRR_Detection_037_042_MsgError = bool(self.FrontRAD_CAN_RADFR_MRR_Detection_037_042_MsgError)
      self.FrontRAD_CAN_RADFR_MRR_Detection_043_048_MsgError = bool(self.FrontRAD_CAN_RADFR_MRR_Detection_043_048_MsgError)
      self.FrontRAD_CAN_RADFR_MRR_Detection_049_054_MsgError = bool(self.FrontRAD_CAN_RADFR_MRR_Detection_049_054_MsgError)
      self.FrontRAD_CAN_RADFR_MRR_Detection_055_060_MsgError = bool(self.FrontRAD_CAN_RADFR_MRR_Detection_055_060_MsgError)
      self.FrontRAD_CAN_RADFR_MRR_Detection_061_064_MsgError = bool(self.FrontRAD_CAN_RADFR_MRR_Detection_061_064_MsgError)
      self.FrontRAD_CAN_RADFR_MRR_Header_AlignmentState_MsgError = bool(self.FrontRAD_CAN_RADFR_MRR_Header_AlignmentState_MsgError)
      self.FrontRAD_CAN_RADFR_MRR_Header_SensorCoverage_MsgError = bool(self.FrontRAD_CAN_RADFR_MRR_Header_SensorCoverage_MsgError)
      self.FrontRAD_CAN_RADFR_MRR_Header_Timestamps_MsgError = bool(self.FrontRAD_CAN_RADFR_MRR_Header_Timestamps_MsgError)
      self.FrontRAD_CAN_RADFR_MRR_CANVersion_MsgError = bool(self.FrontRAD_CAN_RADFR_MRR_CANVersion_MsgError)
      self.FrontRAD_CAN_RADFR_MRR_Status_Radar_MsgError = bool(self.FrontRAD_CAN_RADFR_MRR_Status_Radar_MsgError)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_27B = None
def _get_struct_27B():
    global _struct_27B
    if _struct_27B is None:
        _struct_27B = struct.Struct("<27B")
    return _struct_27B

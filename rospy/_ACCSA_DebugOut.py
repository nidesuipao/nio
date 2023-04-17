# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from rospy_message_converter/ACCSA_DebugOut.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class ACCSA_DebugOut(genpy.Message):
  _md5sum = "744b5fb9f031304e4650485e4addbb46"
  _type = "rospy_message_converter/ACCSA_DebugOut"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """float64 ACCSA_aVMCLgtAccCp_mp
float64 ACCSA_aVMCLgtDecCp_mp
bool ACCSA_flgAbsActv_mp
uint32 ACCSA_idxLnSpdLimIdC_mp
uint32 ACCSA_idxLnSpdLimIdNN_mp
uint32 ACCSA_idxLnSpdLimIdN_mp
float64 ACCSA_kphLnSpdLimC_mp
float64 ACCSA_kphLnSpdLimNN_mp
float64 ACCSA_kphLnSpdLimN_mp
uint32 ACCSA_mLnGpTypeC_mp
uint32 ACCSA_mLnGpTypeNN_mp
uint32 ACCSA_mLnGpTypeN_mp
float64 ACCSA_mLnSpdLimDistC_mp
float64 ACCSA_mLnSpdLimDistNN_mp
float64 ACCSA_mLnSpdLimDistN_mp
float64 ACCSA_mpssLgtAcc_mp
uint32 ACCSA_nabigation_state_mp
float64 ACCSA_nop_colllision_risk_mp
float64 ACCSA_nop_freeSpace_intrusion_go_notifier_mp
float64 ACCSA_nop_freespaceintrusionatstandstill_mp
uint32 ACCSA_nop_function_status_nop_sts_mp
uint32 ACCSA_nop_lat_ctrl_tarLe_mp
uint32 ACCSA_nop_lat_ctrl_tarRi_mp
uint32 ACCSA_nop_long_ctrl_tar_mp
uint32 ACCSA_nop_sldf_state_mp
uint32 ACCSA_nop_spdlimt_supsignType_mp
uint32 ACCSA_nop_spdlmt_unit_mp
uint32 ACCSA_nop_spdlmt_value_mp
uint32 ACCSA_nop_turn_indicator_req_mp
bool ACCSA_nop_vlc_frive_off_req_mp
uint32 ACCSA_numFAM_ID10_mp
uint32 ACCSA_numFAM_ID1_mp
uint32 ACCSA_numFAM_ID7_mp
uint32 ACCSA_reliable_state_mp
uint32 ACCSA_seg0formofway_state_mp
uint32 ACCSA_seg0offset_state_mp
uint32 ACCSA_stFAM_Req10_mp
uint32 ACCSA_stFAM_Req1_mp
uint32 ACCSA_stFAM_Req7_mp
uint32 ACCSA_stLnSpdLimConfC_mp
uint32 ACCSA_stLnSpdLimConfNN_mp
uint32 ACCSA_stLnSpdLimConfN_mp
uint32 ACCSA_stLnSpdLimSrcC_mp
uint32 ACCSA_stLnSpdLimSrcNN_mp
uint32 ACCSA_stLnSpdLimSrcN_mp
uint32 ACCSA_stLnSpdLimSupSignAttrC_mp
uint32 ACCSA_stLnSpdLimSupSignAttrNN_mp
uint32 ACCSA_stLnSpdLimSupSignAttrN_mp
uint32 ACCSA_stLnSpdLimSupSignTypeC_mp
uint32 ACCSA_stLnSpdLimSupSignTypeNN_mp
uint32 ACCSA_stLnSpdLimSupSignTypeN_mp
uint32 ACCSA_stLnSpdLimUnitC_mp
uint32 ACCSA_stLnSpdLimUnitNN_mp
uint32 ACCSA_stLnSpdLimUnitN_mp
float64 ACCSA_stSpdDecBtn_mp
float64 ACCSA_stSpdIncBtn_mp
uint32 ACCSA_uFCC1LgtSts_mp
uint32 ACCSA_uVMCLgtSts_mp
"""
  __slots__ = ['ACCSA_aVMCLgtAccCp_mp','ACCSA_aVMCLgtDecCp_mp','ACCSA_flgAbsActv_mp','ACCSA_idxLnSpdLimIdC_mp','ACCSA_idxLnSpdLimIdNN_mp','ACCSA_idxLnSpdLimIdN_mp','ACCSA_kphLnSpdLimC_mp','ACCSA_kphLnSpdLimNN_mp','ACCSA_kphLnSpdLimN_mp','ACCSA_mLnGpTypeC_mp','ACCSA_mLnGpTypeNN_mp','ACCSA_mLnGpTypeN_mp','ACCSA_mLnSpdLimDistC_mp','ACCSA_mLnSpdLimDistNN_mp','ACCSA_mLnSpdLimDistN_mp','ACCSA_mpssLgtAcc_mp','ACCSA_nabigation_state_mp','ACCSA_nop_colllision_risk_mp','ACCSA_nop_freeSpace_intrusion_go_notifier_mp','ACCSA_nop_freespaceintrusionatstandstill_mp','ACCSA_nop_function_status_nop_sts_mp','ACCSA_nop_lat_ctrl_tarLe_mp','ACCSA_nop_lat_ctrl_tarRi_mp','ACCSA_nop_long_ctrl_tar_mp','ACCSA_nop_sldf_state_mp','ACCSA_nop_spdlimt_supsignType_mp','ACCSA_nop_spdlmt_unit_mp','ACCSA_nop_spdlmt_value_mp','ACCSA_nop_turn_indicator_req_mp','ACCSA_nop_vlc_frive_off_req_mp','ACCSA_numFAM_ID10_mp','ACCSA_numFAM_ID1_mp','ACCSA_numFAM_ID7_mp','ACCSA_reliable_state_mp','ACCSA_seg0formofway_state_mp','ACCSA_seg0offset_state_mp','ACCSA_stFAM_Req10_mp','ACCSA_stFAM_Req1_mp','ACCSA_stFAM_Req7_mp','ACCSA_stLnSpdLimConfC_mp','ACCSA_stLnSpdLimConfNN_mp','ACCSA_stLnSpdLimConfN_mp','ACCSA_stLnSpdLimSrcC_mp','ACCSA_stLnSpdLimSrcNN_mp','ACCSA_stLnSpdLimSrcN_mp','ACCSA_stLnSpdLimSupSignAttrC_mp','ACCSA_stLnSpdLimSupSignAttrNN_mp','ACCSA_stLnSpdLimSupSignAttrN_mp','ACCSA_stLnSpdLimSupSignTypeC_mp','ACCSA_stLnSpdLimSupSignTypeNN_mp','ACCSA_stLnSpdLimSupSignTypeN_mp','ACCSA_stLnSpdLimUnitC_mp','ACCSA_stLnSpdLimUnitNN_mp','ACCSA_stLnSpdLimUnitN_mp','ACCSA_stSpdDecBtn_mp','ACCSA_stSpdIncBtn_mp','ACCSA_uFCC1LgtSts_mp','ACCSA_uVMCLgtSts_mp']
  _slot_types = ['float64','float64','bool','uint32','uint32','uint32','float64','float64','float64','uint32','uint32','uint32','float64','float64','float64','float64','uint32','float64','float64','float64','uint32','uint32','uint32','uint32','uint32','uint32','uint32','uint32','uint32','bool','uint32','uint32','uint32','uint32','uint32','uint32','uint32','uint32','uint32','uint32','uint32','uint32','uint32','uint32','uint32','uint32','uint32','uint32','uint32','uint32','uint32','uint32','uint32','uint32','float64','float64','uint32','uint32']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       ACCSA_aVMCLgtAccCp_mp,ACCSA_aVMCLgtDecCp_mp,ACCSA_flgAbsActv_mp,ACCSA_idxLnSpdLimIdC_mp,ACCSA_idxLnSpdLimIdNN_mp,ACCSA_idxLnSpdLimIdN_mp,ACCSA_kphLnSpdLimC_mp,ACCSA_kphLnSpdLimNN_mp,ACCSA_kphLnSpdLimN_mp,ACCSA_mLnGpTypeC_mp,ACCSA_mLnGpTypeNN_mp,ACCSA_mLnGpTypeN_mp,ACCSA_mLnSpdLimDistC_mp,ACCSA_mLnSpdLimDistNN_mp,ACCSA_mLnSpdLimDistN_mp,ACCSA_mpssLgtAcc_mp,ACCSA_nabigation_state_mp,ACCSA_nop_colllision_risk_mp,ACCSA_nop_freeSpace_intrusion_go_notifier_mp,ACCSA_nop_freespaceintrusionatstandstill_mp,ACCSA_nop_function_status_nop_sts_mp,ACCSA_nop_lat_ctrl_tarLe_mp,ACCSA_nop_lat_ctrl_tarRi_mp,ACCSA_nop_long_ctrl_tar_mp,ACCSA_nop_sldf_state_mp,ACCSA_nop_spdlimt_supsignType_mp,ACCSA_nop_spdlmt_unit_mp,ACCSA_nop_spdlmt_value_mp,ACCSA_nop_turn_indicator_req_mp,ACCSA_nop_vlc_frive_off_req_mp,ACCSA_numFAM_ID10_mp,ACCSA_numFAM_ID1_mp,ACCSA_numFAM_ID7_mp,ACCSA_reliable_state_mp,ACCSA_seg0formofway_state_mp,ACCSA_seg0offset_state_mp,ACCSA_stFAM_Req10_mp,ACCSA_stFAM_Req1_mp,ACCSA_stFAM_Req7_mp,ACCSA_stLnSpdLimConfC_mp,ACCSA_stLnSpdLimConfNN_mp,ACCSA_stLnSpdLimConfN_mp,ACCSA_stLnSpdLimSrcC_mp,ACCSA_stLnSpdLimSrcNN_mp,ACCSA_stLnSpdLimSrcN_mp,ACCSA_stLnSpdLimSupSignAttrC_mp,ACCSA_stLnSpdLimSupSignAttrNN_mp,ACCSA_stLnSpdLimSupSignAttrN_mp,ACCSA_stLnSpdLimSupSignTypeC_mp,ACCSA_stLnSpdLimSupSignTypeNN_mp,ACCSA_stLnSpdLimSupSignTypeN_mp,ACCSA_stLnSpdLimUnitC_mp,ACCSA_stLnSpdLimUnitNN_mp,ACCSA_stLnSpdLimUnitN_mp,ACCSA_stSpdDecBtn_mp,ACCSA_stSpdIncBtn_mp,ACCSA_uFCC1LgtSts_mp,ACCSA_uVMCLgtSts_mp

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(ACCSA_DebugOut, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.ACCSA_aVMCLgtAccCp_mp is None:
        self.ACCSA_aVMCLgtAccCp_mp = 0.
      if self.ACCSA_aVMCLgtDecCp_mp is None:
        self.ACCSA_aVMCLgtDecCp_mp = 0.
      if self.ACCSA_flgAbsActv_mp is None:
        self.ACCSA_flgAbsActv_mp = False
      if self.ACCSA_idxLnSpdLimIdC_mp is None:
        self.ACCSA_idxLnSpdLimIdC_mp = 0
      if self.ACCSA_idxLnSpdLimIdNN_mp is None:
        self.ACCSA_idxLnSpdLimIdNN_mp = 0
      if self.ACCSA_idxLnSpdLimIdN_mp is None:
        self.ACCSA_idxLnSpdLimIdN_mp = 0
      if self.ACCSA_kphLnSpdLimC_mp is None:
        self.ACCSA_kphLnSpdLimC_mp = 0.
      if self.ACCSA_kphLnSpdLimNN_mp is None:
        self.ACCSA_kphLnSpdLimNN_mp = 0.
      if self.ACCSA_kphLnSpdLimN_mp is None:
        self.ACCSA_kphLnSpdLimN_mp = 0.
      if self.ACCSA_mLnGpTypeC_mp is None:
        self.ACCSA_mLnGpTypeC_mp = 0
      if self.ACCSA_mLnGpTypeNN_mp is None:
        self.ACCSA_mLnGpTypeNN_mp = 0
      if self.ACCSA_mLnGpTypeN_mp is None:
        self.ACCSA_mLnGpTypeN_mp = 0
      if self.ACCSA_mLnSpdLimDistC_mp is None:
        self.ACCSA_mLnSpdLimDistC_mp = 0.
      if self.ACCSA_mLnSpdLimDistNN_mp is None:
        self.ACCSA_mLnSpdLimDistNN_mp = 0.
      if self.ACCSA_mLnSpdLimDistN_mp is None:
        self.ACCSA_mLnSpdLimDistN_mp = 0.
      if self.ACCSA_mpssLgtAcc_mp is None:
        self.ACCSA_mpssLgtAcc_mp = 0.
      if self.ACCSA_nabigation_state_mp is None:
        self.ACCSA_nabigation_state_mp = 0
      if self.ACCSA_nop_colllision_risk_mp is None:
        self.ACCSA_nop_colllision_risk_mp = 0.
      if self.ACCSA_nop_freeSpace_intrusion_go_notifier_mp is None:
        self.ACCSA_nop_freeSpace_intrusion_go_notifier_mp = 0.
      if self.ACCSA_nop_freespaceintrusionatstandstill_mp is None:
        self.ACCSA_nop_freespaceintrusionatstandstill_mp = 0.
      if self.ACCSA_nop_function_status_nop_sts_mp is None:
        self.ACCSA_nop_function_status_nop_sts_mp = 0
      if self.ACCSA_nop_lat_ctrl_tarLe_mp is None:
        self.ACCSA_nop_lat_ctrl_tarLe_mp = 0
      if self.ACCSA_nop_lat_ctrl_tarRi_mp is None:
        self.ACCSA_nop_lat_ctrl_tarRi_mp = 0
      if self.ACCSA_nop_long_ctrl_tar_mp is None:
        self.ACCSA_nop_long_ctrl_tar_mp = 0
      if self.ACCSA_nop_sldf_state_mp is None:
        self.ACCSA_nop_sldf_state_mp = 0
      if self.ACCSA_nop_spdlimt_supsignType_mp is None:
        self.ACCSA_nop_spdlimt_supsignType_mp = 0
      if self.ACCSA_nop_spdlmt_unit_mp is None:
        self.ACCSA_nop_spdlmt_unit_mp = 0
      if self.ACCSA_nop_spdlmt_value_mp is None:
        self.ACCSA_nop_spdlmt_value_mp = 0
      if self.ACCSA_nop_turn_indicator_req_mp is None:
        self.ACCSA_nop_turn_indicator_req_mp = 0
      if self.ACCSA_nop_vlc_frive_off_req_mp is None:
        self.ACCSA_nop_vlc_frive_off_req_mp = False
      if self.ACCSA_numFAM_ID10_mp is None:
        self.ACCSA_numFAM_ID10_mp = 0
      if self.ACCSA_numFAM_ID1_mp is None:
        self.ACCSA_numFAM_ID1_mp = 0
      if self.ACCSA_numFAM_ID7_mp is None:
        self.ACCSA_numFAM_ID7_mp = 0
      if self.ACCSA_reliable_state_mp is None:
        self.ACCSA_reliable_state_mp = 0
      if self.ACCSA_seg0formofway_state_mp is None:
        self.ACCSA_seg0formofway_state_mp = 0
      if self.ACCSA_seg0offset_state_mp is None:
        self.ACCSA_seg0offset_state_mp = 0
      if self.ACCSA_stFAM_Req10_mp is None:
        self.ACCSA_stFAM_Req10_mp = 0
      if self.ACCSA_stFAM_Req1_mp is None:
        self.ACCSA_stFAM_Req1_mp = 0
      if self.ACCSA_stFAM_Req7_mp is None:
        self.ACCSA_stFAM_Req7_mp = 0
      if self.ACCSA_stLnSpdLimConfC_mp is None:
        self.ACCSA_stLnSpdLimConfC_mp = 0
      if self.ACCSA_stLnSpdLimConfNN_mp is None:
        self.ACCSA_stLnSpdLimConfNN_mp = 0
      if self.ACCSA_stLnSpdLimConfN_mp is None:
        self.ACCSA_stLnSpdLimConfN_mp = 0
      if self.ACCSA_stLnSpdLimSrcC_mp is None:
        self.ACCSA_stLnSpdLimSrcC_mp = 0
      if self.ACCSA_stLnSpdLimSrcNN_mp is None:
        self.ACCSA_stLnSpdLimSrcNN_mp = 0
      if self.ACCSA_stLnSpdLimSrcN_mp is None:
        self.ACCSA_stLnSpdLimSrcN_mp = 0
      if self.ACCSA_stLnSpdLimSupSignAttrC_mp is None:
        self.ACCSA_stLnSpdLimSupSignAttrC_mp = 0
      if self.ACCSA_stLnSpdLimSupSignAttrNN_mp is None:
        self.ACCSA_stLnSpdLimSupSignAttrNN_mp = 0
      if self.ACCSA_stLnSpdLimSupSignAttrN_mp is None:
        self.ACCSA_stLnSpdLimSupSignAttrN_mp = 0
      if self.ACCSA_stLnSpdLimSupSignTypeC_mp is None:
        self.ACCSA_stLnSpdLimSupSignTypeC_mp = 0
      if self.ACCSA_stLnSpdLimSupSignTypeNN_mp is None:
        self.ACCSA_stLnSpdLimSupSignTypeNN_mp = 0
      if self.ACCSA_stLnSpdLimSupSignTypeN_mp is None:
        self.ACCSA_stLnSpdLimSupSignTypeN_mp = 0
      if self.ACCSA_stLnSpdLimUnitC_mp is None:
        self.ACCSA_stLnSpdLimUnitC_mp = 0
      if self.ACCSA_stLnSpdLimUnitNN_mp is None:
        self.ACCSA_stLnSpdLimUnitNN_mp = 0
      if self.ACCSA_stLnSpdLimUnitN_mp is None:
        self.ACCSA_stLnSpdLimUnitN_mp = 0
      if self.ACCSA_stSpdDecBtn_mp is None:
        self.ACCSA_stSpdDecBtn_mp = 0.
      if self.ACCSA_stSpdIncBtn_mp is None:
        self.ACCSA_stSpdIncBtn_mp = 0.
      if self.ACCSA_uFCC1LgtSts_mp is None:
        self.ACCSA_uFCC1LgtSts_mp = 0
      if self.ACCSA_uVMCLgtSts_mp is None:
        self.ACCSA_uVMCLgtSts_mp = 0
    else:
      self.ACCSA_aVMCLgtAccCp_mp = 0.
      self.ACCSA_aVMCLgtDecCp_mp = 0.
      self.ACCSA_flgAbsActv_mp = False
      self.ACCSA_idxLnSpdLimIdC_mp = 0
      self.ACCSA_idxLnSpdLimIdNN_mp = 0
      self.ACCSA_idxLnSpdLimIdN_mp = 0
      self.ACCSA_kphLnSpdLimC_mp = 0.
      self.ACCSA_kphLnSpdLimNN_mp = 0.
      self.ACCSA_kphLnSpdLimN_mp = 0.
      self.ACCSA_mLnGpTypeC_mp = 0
      self.ACCSA_mLnGpTypeNN_mp = 0
      self.ACCSA_mLnGpTypeN_mp = 0
      self.ACCSA_mLnSpdLimDistC_mp = 0.
      self.ACCSA_mLnSpdLimDistNN_mp = 0.
      self.ACCSA_mLnSpdLimDistN_mp = 0.
      self.ACCSA_mpssLgtAcc_mp = 0.
      self.ACCSA_nabigation_state_mp = 0
      self.ACCSA_nop_colllision_risk_mp = 0.
      self.ACCSA_nop_freeSpace_intrusion_go_notifier_mp = 0.
      self.ACCSA_nop_freespaceintrusionatstandstill_mp = 0.
      self.ACCSA_nop_function_status_nop_sts_mp = 0
      self.ACCSA_nop_lat_ctrl_tarLe_mp = 0
      self.ACCSA_nop_lat_ctrl_tarRi_mp = 0
      self.ACCSA_nop_long_ctrl_tar_mp = 0
      self.ACCSA_nop_sldf_state_mp = 0
      self.ACCSA_nop_spdlimt_supsignType_mp = 0
      self.ACCSA_nop_spdlmt_unit_mp = 0
      self.ACCSA_nop_spdlmt_value_mp = 0
      self.ACCSA_nop_turn_indicator_req_mp = 0
      self.ACCSA_nop_vlc_frive_off_req_mp = False
      self.ACCSA_numFAM_ID10_mp = 0
      self.ACCSA_numFAM_ID1_mp = 0
      self.ACCSA_numFAM_ID7_mp = 0
      self.ACCSA_reliable_state_mp = 0
      self.ACCSA_seg0formofway_state_mp = 0
      self.ACCSA_seg0offset_state_mp = 0
      self.ACCSA_stFAM_Req10_mp = 0
      self.ACCSA_stFAM_Req1_mp = 0
      self.ACCSA_stFAM_Req7_mp = 0
      self.ACCSA_stLnSpdLimConfC_mp = 0
      self.ACCSA_stLnSpdLimConfNN_mp = 0
      self.ACCSA_stLnSpdLimConfN_mp = 0
      self.ACCSA_stLnSpdLimSrcC_mp = 0
      self.ACCSA_stLnSpdLimSrcNN_mp = 0
      self.ACCSA_stLnSpdLimSrcN_mp = 0
      self.ACCSA_stLnSpdLimSupSignAttrC_mp = 0
      self.ACCSA_stLnSpdLimSupSignAttrNN_mp = 0
      self.ACCSA_stLnSpdLimSupSignAttrN_mp = 0
      self.ACCSA_stLnSpdLimSupSignTypeC_mp = 0
      self.ACCSA_stLnSpdLimSupSignTypeNN_mp = 0
      self.ACCSA_stLnSpdLimSupSignTypeN_mp = 0
      self.ACCSA_stLnSpdLimUnitC_mp = 0
      self.ACCSA_stLnSpdLimUnitNN_mp = 0
      self.ACCSA_stLnSpdLimUnitN_mp = 0
      self.ACCSA_stSpdDecBtn_mp = 0.
      self.ACCSA_stSpdIncBtn_mp = 0.
      self.ACCSA_uFCC1LgtSts_mp = 0
      self.ACCSA_uVMCLgtSts_mp = 0

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
      buff.write(_get_struct_2dB3I3d3I4dI3d9IB24I2d2I().pack(_x.ACCSA_aVMCLgtAccCp_mp, _x.ACCSA_aVMCLgtDecCp_mp, _x.ACCSA_flgAbsActv_mp, _x.ACCSA_idxLnSpdLimIdC_mp, _x.ACCSA_idxLnSpdLimIdNN_mp, _x.ACCSA_idxLnSpdLimIdN_mp, _x.ACCSA_kphLnSpdLimC_mp, _x.ACCSA_kphLnSpdLimNN_mp, _x.ACCSA_kphLnSpdLimN_mp, _x.ACCSA_mLnGpTypeC_mp, _x.ACCSA_mLnGpTypeNN_mp, _x.ACCSA_mLnGpTypeN_mp, _x.ACCSA_mLnSpdLimDistC_mp, _x.ACCSA_mLnSpdLimDistNN_mp, _x.ACCSA_mLnSpdLimDistN_mp, _x.ACCSA_mpssLgtAcc_mp, _x.ACCSA_nabigation_state_mp, _x.ACCSA_nop_colllision_risk_mp, _x.ACCSA_nop_freeSpace_intrusion_go_notifier_mp, _x.ACCSA_nop_freespaceintrusionatstandstill_mp, _x.ACCSA_nop_function_status_nop_sts_mp, _x.ACCSA_nop_lat_ctrl_tarLe_mp, _x.ACCSA_nop_lat_ctrl_tarRi_mp, _x.ACCSA_nop_long_ctrl_tar_mp, _x.ACCSA_nop_sldf_state_mp, _x.ACCSA_nop_spdlimt_supsignType_mp, _x.ACCSA_nop_spdlmt_unit_mp, _x.ACCSA_nop_spdlmt_value_mp, _x.ACCSA_nop_turn_indicator_req_mp, _x.ACCSA_nop_vlc_frive_off_req_mp, _x.ACCSA_numFAM_ID10_mp, _x.ACCSA_numFAM_ID1_mp, _x.ACCSA_numFAM_ID7_mp, _x.ACCSA_reliable_state_mp, _x.ACCSA_seg0formofway_state_mp, _x.ACCSA_seg0offset_state_mp, _x.ACCSA_stFAM_Req10_mp, _x.ACCSA_stFAM_Req1_mp, _x.ACCSA_stFAM_Req7_mp, _x.ACCSA_stLnSpdLimConfC_mp, _x.ACCSA_stLnSpdLimConfNN_mp, _x.ACCSA_stLnSpdLimConfN_mp, _x.ACCSA_stLnSpdLimSrcC_mp, _x.ACCSA_stLnSpdLimSrcNN_mp, _x.ACCSA_stLnSpdLimSrcN_mp, _x.ACCSA_stLnSpdLimSupSignAttrC_mp, _x.ACCSA_stLnSpdLimSupSignAttrNN_mp, _x.ACCSA_stLnSpdLimSupSignAttrN_mp, _x.ACCSA_stLnSpdLimSupSignTypeC_mp, _x.ACCSA_stLnSpdLimSupSignTypeNN_mp, _x.ACCSA_stLnSpdLimSupSignTypeN_mp, _x.ACCSA_stLnSpdLimUnitC_mp, _x.ACCSA_stLnSpdLimUnitNN_mp, _x.ACCSA_stLnSpdLimUnitN_mp, _x.ACCSA_stSpdDecBtn_mp, _x.ACCSA_stSpdIncBtn_mp, _x.ACCSA_uFCC1LgtSts_mp, _x.ACCSA_uVMCLgtSts_mp))
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
      end += 282
      (_x.ACCSA_aVMCLgtAccCp_mp, _x.ACCSA_aVMCLgtDecCp_mp, _x.ACCSA_flgAbsActv_mp, _x.ACCSA_idxLnSpdLimIdC_mp, _x.ACCSA_idxLnSpdLimIdNN_mp, _x.ACCSA_idxLnSpdLimIdN_mp, _x.ACCSA_kphLnSpdLimC_mp, _x.ACCSA_kphLnSpdLimNN_mp, _x.ACCSA_kphLnSpdLimN_mp, _x.ACCSA_mLnGpTypeC_mp, _x.ACCSA_mLnGpTypeNN_mp, _x.ACCSA_mLnGpTypeN_mp, _x.ACCSA_mLnSpdLimDistC_mp, _x.ACCSA_mLnSpdLimDistNN_mp, _x.ACCSA_mLnSpdLimDistN_mp, _x.ACCSA_mpssLgtAcc_mp, _x.ACCSA_nabigation_state_mp, _x.ACCSA_nop_colllision_risk_mp, _x.ACCSA_nop_freeSpace_intrusion_go_notifier_mp, _x.ACCSA_nop_freespaceintrusionatstandstill_mp, _x.ACCSA_nop_function_status_nop_sts_mp, _x.ACCSA_nop_lat_ctrl_tarLe_mp, _x.ACCSA_nop_lat_ctrl_tarRi_mp, _x.ACCSA_nop_long_ctrl_tar_mp, _x.ACCSA_nop_sldf_state_mp, _x.ACCSA_nop_spdlimt_supsignType_mp, _x.ACCSA_nop_spdlmt_unit_mp, _x.ACCSA_nop_spdlmt_value_mp, _x.ACCSA_nop_turn_indicator_req_mp, _x.ACCSA_nop_vlc_frive_off_req_mp, _x.ACCSA_numFAM_ID10_mp, _x.ACCSA_numFAM_ID1_mp, _x.ACCSA_numFAM_ID7_mp, _x.ACCSA_reliable_state_mp, _x.ACCSA_seg0formofway_state_mp, _x.ACCSA_seg0offset_state_mp, _x.ACCSA_stFAM_Req10_mp, _x.ACCSA_stFAM_Req1_mp, _x.ACCSA_stFAM_Req7_mp, _x.ACCSA_stLnSpdLimConfC_mp, _x.ACCSA_stLnSpdLimConfNN_mp, _x.ACCSA_stLnSpdLimConfN_mp, _x.ACCSA_stLnSpdLimSrcC_mp, _x.ACCSA_stLnSpdLimSrcNN_mp, _x.ACCSA_stLnSpdLimSrcN_mp, _x.ACCSA_stLnSpdLimSupSignAttrC_mp, _x.ACCSA_stLnSpdLimSupSignAttrNN_mp, _x.ACCSA_stLnSpdLimSupSignAttrN_mp, _x.ACCSA_stLnSpdLimSupSignTypeC_mp, _x.ACCSA_stLnSpdLimSupSignTypeNN_mp, _x.ACCSA_stLnSpdLimSupSignTypeN_mp, _x.ACCSA_stLnSpdLimUnitC_mp, _x.ACCSA_stLnSpdLimUnitNN_mp, _x.ACCSA_stLnSpdLimUnitN_mp, _x.ACCSA_stSpdDecBtn_mp, _x.ACCSA_stSpdIncBtn_mp, _x.ACCSA_uFCC1LgtSts_mp, _x.ACCSA_uVMCLgtSts_mp,) = _get_struct_2dB3I3d3I4dI3d9IB24I2d2I().unpack(str[start:end])
      self.ACCSA_flgAbsActv_mp = bool(self.ACCSA_flgAbsActv_mp)
      self.ACCSA_nop_vlc_frive_off_req_mp = bool(self.ACCSA_nop_vlc_frive_off_req_mp)
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
      buff.write(_get_struct_2dB3I3d3I4dI3d9IB24I2d2I().pack(_x.ACCSA_aVMCLgtAccCp_mp, _x.ACCSA_aVMCLgtDecCp_mp, _x.ACCSA_flgAbsActv_mp, _x.ACCSA_idxLnSpdLimIdC_mp, _x.ACCSA_idxLnSpdLimIdNN_mp, _x.ACCSA_idxLnSpdLimIdN_mp, _x.ACCSA_kphLnSpdLimC_mp, _x.ACCSA_kphLnSpdLimNN_mp, _x.ACCSA_kphLnSpdLimN_mp, _x.ACCSA_mLnGpTypeC_mp, _x.ACCSA_mLnGpTypeNN_mp, _x.ACCSA_mLnGpTypeN_mp, _x.ACCSA_mLnSpdLimDistC_mp, _x.ACCSA_mLnSpdLimDistNN_mp, _x.ACCSA_mLnSpdLimDistN_mp, _x.ACCSA_mpssLgtAcc_mp, _x.ACCSA_nabigation_state_mp, _x.ACCSA_nop_colllision_risk_mp, _x.ACCSA_nop_freeSpace_intrusion_go_notifier_mp, _x.ACCSA_nop_freespaceintrusionatstandstill_mp, _x.ACCSA_nop_function_status_nop_sts_mp, _x.ACCSA_nop_lat_ctrl_tarLe_mp, _x.ACCSA_nop_lat_ctrl_tarRi_mp, _x.ACCSA_nop_long_ctrl_tar_mp, _x.ACCSA_nop_sldf_state_mp, _x.ACCSA_nop_spdlimt_supsignType_mp, _x.ACCSA_nop_spdlmt_unit_mp, _x.ACCSA_nop_spdlmt_value_mp, _x.ACCSA_nop_turn_indicator_req_mp, _x.ACCSA_nop_vlc_frive_off_req_mp, _x.ACCSA_numFAM_ID10_mp, _x.ACCSA_numFAM_ID1_mp, _x.ACCSA_numFAM_ID7_mp, _x.ACCSA_reliable_state_mp, _x.ACCSA_seg0formofway_state_mp, _x.ACCSA_seg0offset_state_mp, _x.ACCSA_stFAM_Req10_mp, _x.ACCSA_stFAM_Req1_mp, _x.ACCSA_stFAM_Req7_mp, _x.ACCSA_stLnSpdLimConfC_mp, _x.ACCSA_stLnSpdLimConfNN_mp, _x.ACCSA_stLnSpdLimConfN_mp, _x.ACCSA_stLnSpdLimSrcC_mp, _x.ACCSA_stLnSpdLimSrcNN_mp, _x.ACCSA_stLnSpdLimSrcN_mp, _x.ACCSA_stLnSpdLimSupSignAttrC_mp, _x.ACCSA_stLnSpdLimSupSignAttrNN_mp, _x.ACCSA_stLnSpdLimSupSignAttrN_mp, _x.ACCSA_stLnSpdLimSupSignTypeC_mp, _x.ACCSA_stLnSpdLimSupSignTypeNN_mp, _x.ACCSA_stLnSpdLimSupSignTypeN_mp, _x.ACCSA_stLnSpdLimUnitC_mp, _x.ACCSA_stLnSpdLimUnitNN_mp, _x.ACCSA_stLnSpdLimUnitN_mp, _x.ACCSA_stSpdDecBtn_mp, _x.ACCSA_stSpdIncBtn_mp, _x.ACCSA_uFCC1LgtSts_mp, _x.ACCSA_uVMCLgtSts_mp))
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
      end += 282
      (_x.ACCSA_aVMCLgtAccCp_mp, _x.ACCSA_aVMCLgtDecCp_mp, _x.ACCSA_flgAbsActv_mp, _x.ACCSA_idxLnSpdLimIdC_mp, _x.ACCSA_idxLnSpdLimIdNN_mp, _x.ACCSA_idxLnSpdLimIdN_mp, _x.ACCSA_kphLnSpdLimC_mp, _x.ACCSA_kphLnSpdLimNN_mp, _x.ACCSA_kphLnSpdLimN_mp, _x.ACCSA_mLnGpTypeC_mp, _x.ACCSA_mLnGpTypeNN_mp, _x.ACCSA_mLnGpTypeN_mp, _x.ACCSA_mLnSpdLimDistC_mp, _x.ACCSA_mLnSpdLimDistNN_mp, _x.ACCSA_mLnSpdLimDistN_mp, _x.ACCSA_mpssLgtAcc_mp, _x.ACCSA_nabigation_state_mp, _x.ACCSA_nop_colllision_risk_mp, _x.ACCSA_nop_freeSpace_intrusion_go_notifier_mp, _x.ACCSA_nop_freespaceintrusionatstandstill_mp, _x.ACCSA_nop_function_status_nop_sts_mp, _x.ACCSA_nop_lat_ctrl_tarLe_mp, _x.ACCSA_nop_lat_ctrl_tarRi_mp, _x.ACCSA_nop_long_ctrl_tar_mp, _x.ACCSA_nop_sldf_state_mp, _x.ACCSA_nop_spdlimt_supsignType_mp, _x.ACCSA_nop_spdlmt_unit_mp, _x.ACCSA_nop_spdlmt_value_mp, _x.ACCSA_nop_turn_indicator_req_mp, _x.ACCSA_nop_vlc_frive_off_req_mp, _x.ACCSA_numFAM_ID10_mp, _x.ACCSA_numFAM_ID1_mp, _x.ACCSA_numFAM_ID7_mp, _x.ACCSA_reliable_state_mp, _x.ACCSA_seg0formofway_state_mp, _x.ACCSA_seg0offset_state_mp, _x.ACCSA_stFAM_Req10_mp, _x.ACCSA_stFAM_Req1_mp, _x.ACCSA_stFAM_Req7_mp, _x.ACCSA_stLnSpdLimConfC_mp, _x.ACCSA_stLnSpdLimConfNN_mp, _x.ACCSA_stLnSpdLimConfN_mp, _x.ACCSA_stLnSpdLimSrcC_mp, _x.ACCSA_stLnSpdLimSrcNN_mp, _x.ACCSA_stLnSpdLimSrcN_mp, _x.ACCSA_stLnSpdLimSupSignAttrC_mp, _x.ACCSA_stLnSpdLimSupSignAttrNN_mp, _x.ACCSA_stLnSpdLimSupSignAttrN_mp, _x.ACCSA_stLnSpdLimSupSignTypeC_mp, _x.ACCSA_stLnSpdLimSupSignTypeNN_mp, _x.ACCSA_stLnSpdLimSupSignTypeN_mp, _x.ACCSA_stLnSpdLimUnitC_mp, _x.ACCSA_stLnSpdLimUnitNN_mp, _x.ACCSA_stLnSpdLimUnitN_mp, _x.ACCSA_stSpdDecBtn_mp, _x.ACCSA_stSpdIncBtn_mp, _x.ACCSA_uFCC1LgtSts_mp, _x.ACCSA_uVMCLgtSts_mp,) = _get_struct_2dB3I3d3I4dI3d9IB24I2d2I().unpack(str[start:end])
      self.ACCSA_flgAbsActv_mp = bool(self.ACCSA_flgAbsActv_mp)
      self.ACCSA_nop_vlc_frive_off_req_mp = bool(self.ACCSA_nop_vlc_frive_off_req_mp)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_2dB3I3d3I4dI3d9IB24I2d2I = None
def _get_struct_2dB3I3d3I4dI3d9IB24I2d2I():
    global _struct_2dB3I3d3I4dI3d9IB24I2d2I
    if _struct_2dB3I3d3I4dI3d9IB24I2d2I is None:
        _struct_2dB3I3d3I4dI3d9IB24I2d2I = struct.Struct("<2dB3I3d3I4dI3d9IB24I2d2I")
    return _struct_2dB3I3d3I4dI3d9IB24I2d2I

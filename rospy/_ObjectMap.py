# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from rospy_message_converter/ObjectMap.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import rospy_message_converter.msg

class ObjectMap(genpy.Message):
  _md5sum = "9295e5ba5a26f786df94f4dee2405996"
  _type = "rospy_message_converter/ObjectMap"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """CrenStru[] car
CrenStru[] pedstrain
CrenStru[] bicyclist
CrenStru[] motor
CrenStru[] obstacle

================================================================================
MSG: rospy_message_converter/CrenStru
ObjectStru objInfo
ObhcStru obhcInfo
OthaStru othaInfo
float32[] reserved

================================================================================
MSG: rospy_message_converter/ObjectStru
uint32 id
uint32 visionId
uint32 radarId
uint32 age
float32 longDist
float32 latDist
float32 longVel
float32 latVel
float32 longAccel
float32 latAccel
float32 heading
float32 curvature
float32 existConfidence
float32 length
float32 width
float32 longDistStd
float32 latDistStd
float32 longVelStd
float32 latVelStd
float32 longAccelStd
float32 latAccelStd
uint32 motionStatus
uint32 detectionSensor
uint32 type
uint32 refPoint
uint32 trackerStatus
uint32 visionDetectionSnesor

================================================================================
MSG: rospy_message_converter/ObhcStru
float32 hypoProb
float32 collProb
float32 ttb
uint32 hypoLabel

================================================================================
MSG: rospy_message_converter/OthaStru
float32 aLgtNec
float32 aLatNec
float32 ttc
bool inPathNow
"""
  __slots__ = ['car','pedstrain','bicyclist','motor','obstacle']
  _slot_types = ['rospy_message_converter/CrenStru[]','rospy_message_converter/CrenStru[]','rospy_message_converter/CrenStru[]','rospy_message_converter/CrenStru[]','rospy_message_converter/CrenStru[]']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       car,pedstrain,bicyclist,motor,obstacle

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(ObjectMap, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.car is None:
        self.car = []
      if self.pedstrain is None:
        self.pedstrain = []
      if self.bicyclist is None:
        self.bicyclist = []
      if self.motor is None:
        self.motor = []
      if self.obstacle is None:
        self.obstacle = []
    else:
      self.car = []
      self.pedstrain = []
      self.bicyclist = []
      self.motor = []
      self.obstacle = []

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
      length = len(self.car)
      buff.write(_struct_I.pack(length))
      for val1 in self.car:
        _v1 = val1.objInfo
        _x = _v1
        buff.write(_get_struct_4I17f6I().pack(_x.id, _x.visionId, _x.radarId, _x.age, _x.longDist, _x.latDist, _x.longVel, _x.latVel, _x.longAccel, _x.latAccel, _x.heading, _x.curvature, _x.existConfidence, _x.length, _x.width, _x.longDistStd, _x.latDistStd, _x.longVelStd, _x.latVelStd, _x.longAccelStd, _x.latAccelStd, _x.motionStatus, _x.detectionSensor, _x.type, _x.refPoint, _x.trackerStatus, _x.visionDetectionSnesor))
        _v2 = val1.obhcInfo
        _x = _v2
        buff.write(_get_struct_3fI().pack(_x.hypoProb, _x.collProb, _x.ttb, _x.hypoLabel))
        _v3 = val1.othaInfo
        _x = _v3
        buff.write(_get_struct_3fB().pack(_x.aLgtNec, _x.aLatNec, _x.ttc, _x.inPathNow))
        length = len(val1.reserved)
        buff.write(_struct_I.pack(length))
        pattern = '<%sf'%length
        buff.write(struct.Struct(pattern).pack(*val1.reserved))
      length = len(self.pedstrain)
      buff.write(_struct_I.pack(length))
      for val1 in self.pedstrain:
        _v4 = val1.objInfo
        _x = _v4
        buff.write(_get_struct_4I17f6I().pack(_x.id, _x.visionId, _x.radarId, _x.age, _x.longDist, _x.latDist, _x.longVel, _x.latVel, _x.longAccel, _x.latAccel, _x.heading, _x.curvature, _x.existConfidence, _x.length, _x.width, _x.longDistStd, _x.latDistStd, _x.longVelStd, _x.latVelStd, _x.longAccelStd, _x.latAccelStd, _x.motionStatus, _x.detectionSensor, _x.type, _x.refPoint, _x.trackerStatus, _x.visionDetectionSnesor))
        _v5 = val1.obhcInfo
        _x = _v5
        buff.write(_get_struct_3fI().pack(_x.hypoProb, _x.collProb, _x.ttb, _x.hypoLabel))
        _v6 = val1.othaInfo
        _x = _v6
        buff.write(_get_struct_3fB().pack(_x.aLgtNec, _x.aLatNec, _x.ttc, _x.inPathNow))
        length = len(val1.reserved)
        buff.write(_struct_I.pack(length))
        pattern = '<%sf'%length
        buff.write(struct.Struct(pattern).pack(*val1.reserved))
      length = len(self.bicyclist)
      buff.write(_struct_I.pack(length))
      for val1 in self.bicyclist:
        _v7 = val1.objInfo
        _x = _v7
        buff.write(_get_struct_4I17f6I().pack(_x.id, _x.visionId, _x.radarId, _x.age, _x.longDist, _x.latDist, _x.longVel, _x.latVel, _x.longAccel, _x.latAccel, _x.heading, _x.curvature, _x.existConfidence, _x.length, _x.width, _x.longDistStd, _x.latDistStd, _x.longVelStd, _x.latVelStd, _x.longAccelStd, _x.latAccelStd, _x.motionStatus, _x.detectionSensor, _x.type, _x.refPoint, _x.trackerStatus, _x.visionDetectionSnesor))
        _v8 = val1.obhcInfo
        _x = _v8
        buff.write(_get_struct_3fI().pack(_x.hypoProb, _x.collProb, _x.ttb, _x.hypoLabel))
        _v9 = val1.othaInfo
        _x = _v9
        buff.write(_get_struct_3fB().pack(_x.aLgtNec, _x.aLatNec, _x.ttc, _x.inPathNow))
        length = len(val1.reserved)
        buff.write(_struct_I.pack(length))
        pattern = '<%sf'%length
        buff.write(struct.Struct(pattern).pack(*val1.reserved))
      length = len(self.motor)
      buff.write(_struct_I.pack(length))
      for val1 in self.motor:
        _v10 = val1.objInfo
        _x = _v10
        buff.write(_get_struct_4I17f6I().pack(_x.id, _x.visionId, _x.radarId, _x.age, _x.longDist, _x.latDist, _x.longVel, _x.latVel, _x.longAccel, _x.latAccel, _x.heading, _x.curvature, _x.existConfidence, _x.length, _x.width, _x.longDistStd, _x.latDistStd, _x.longVelStd, _x.latVelStd, _x.longAccelStd, _x.latAccelStd, _x.motionStatus, _x.detectionSensor, _x.type, _x.refPoint, _x.trackerStatus, _x.visionDetectionSnesor))
        _v11 = val1.obhcInfo
        _x = _v11
        buff.write(_get_struct_3fI().pack(_x.hypoProb, _x.collProb, _x.ttb, _x.hypoLabel))
        _v12 = val1.othaInfo
        _x = _v12
        buff.write(_get_struct_3fB().pack(_x.aLgtNec, _x.aLatNec, _x.ttc, _x.inPathNow))
        length = len(val1.reserved)
        buff.write(_struct_I.pack(length))
        pattern = '<%sf'%length
        buff.write(struct.Struct(pattern).pack(*val1.reserved))
      length = len(self.obstacle)
      buff.write(_struct_I.pack(length))
      for val1 in self.obstacle:
        _v13 = val1.objInfo
        _x = _v13
        buff.write(_get_struct_4I17f6I().pack(_x.id, _x.visionId, _x.radarId, _x.age, _x.longDist, _x.latDist, _x.longVel, _x.latVel, _x.longAccel, _x.latAccel, _x.heading, _x.curvature, _x.existConfidence, _x.length, _x.width, _x.longDistStd, _x.latDistStd, _x.longVelStd, _x.latVelStd, _x.longAccelStd, _x.latAccelStd, _x.motionStatus, _x.detectionSensor, _x.type, _x.refPoint, _x.trackerStatus, _x.visionDetectionSnesor))
        _v14 = val1.obhcInfo
        _x = _v14
        buff.write(_get_struct_3fI().pack(_x.hypoProb, _x.collProb, _x.ttb, _x.hypoLabel))
        _v15 = val1.othaInfo
        _x = _v15
        buff.write(_get_struct_3fB().pack(_x.aLgtNec, _x.aLatNec, _x.ttc, _x.inPathNow))
        length = len(val1.reserved)
        buff.write(_struct_I.pack(length))
        pattern = '<%sf'%length
        buff.write(struct.Struct(pattern).pack(*val1.reserved))
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
      if self.car is None:
        self.car = None
      if self.pedstrain is None:
        self.pedstrain = None
      if self.bicyclist is None:
        self.bicyclist = None
      if self.motor is None:
        self.motor = None
      if self.obstacle is None:
        self.obstacle = None
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.car = []
      for i in range(0, length):
        val1 = rospy_message_converter.msg.CrenStru()
        _v16 = val1.objInfo
        _x = _v16
        start = end
        end += 108
        (_x.id, _x.visionId, _x.radarId, _x.age, _x.longDist, _x.latDist, _x.longVel, _x.latVel, _x.longAccel, _x.latAccel, _x.heading, _x.curvature, _x.existConfidence, _x.length, _x.width, _x.longDistStd, _x.latDistStd, _x.longVelStd, _x.latVelStd, _x.longAccelStd, _x.latAccelStd, _x.motionStatus, _x.detectionSensor, _x.type, _x.refPoint, _x.trackerStatus, _x.visionDetectionSnesor,) = _get_struct_4I17f6I().unpack(str[start:end])
        _v17 = val1.obhcInfo
        _x = _v17
        start = end
        end += 16
        (_x.hypoProb, _x.collProb, _x.ttb, _x.hypoLabel,) = _get_struct_3fI().unpack(str[start:end])
        _v18 = val1.othaInfo
        _x = _v18
        start = end
        end += 13
        (_x.aLgtNec, _x.aLatNec, _x.ttc, _x.inPathNow,) = _get_struct_3fB().unpack(str[start:end])
        _v18.inPathNow = bool(_v18.inPathNow)
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        pattern = '<%sf'%length
        start = end
        s = struct.Struct(pattern)
        end += s.size
        val1.reserved = s.unpack(str[start:end])
        self.car.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.pedstrain = []
      for i in range(0, length):
        val1 = rospy_message_converter.msg.CrenStru()
        _v19 = val1.objInfo
        _x = _v19
        start = end
        end += 108
        (_x.id, _x.visionId, _x.radarId, _x.age, _x.longDist, _x.latDist, _x.longVel, _x.latVel, _x.longAccel, _x.latAccel, _x.heading, _x.curvature, _x.existConfidence, _x.length, _x.width, _x.longDistStd, _x.latDistStd, _x.longVelStd, _x.latVelStd, _x.longAccelStd, _x.latAccelStd, _x.motionStatus, _x.detectionSensor, _x.type, _x.refPoint, _x.trackerStatus, _x.visionDetectionSnesor,) = _get_struct_4I17f6I().unpack(str[start:end])
        _v20 = val1.obhcInfo
        _x = _v20
        start = end
        end += 16
        (_x.hypoProb, _x.collProb, _x.ttb, _x.hypoLabel,) = _get_struct_3fI().unpack(str[start:end])
        _v21 = val1.othaInfo
        _x = _v21
        start = end
        end += 13
        (_x.aLgtNec, _x.aLatNec, _x.ttc, _x.inPathNow,) = _get_struct_3fB().unpack(str[start:end])
        _v21.inPathNow = bool(_v21.inPathNow)
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        pattern = '<%sf'%length
        start = end
        s = struct.Struct(pattern)
        end += s.size
        val1.reserved = s.unpack(str[start:end])
        self.pedstrain.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.bicyclist = []
      for i in range(0, length):
        val1 = rospy_message_converter.msg.CrenStru()
        _v22 = val1.objInfo
        _x = _v22
        start = end
        end += 108
        (_x.id, _x.visionId, _x.radarId, _x.age, _x.longDist, _x.latDist, _x.longVel, _x.latVel, _x.longAccel, _x.latAccel, _x.heading, _x.curvature, _x.existConfidence, _x.length, _x.width, _x.longDistStd, _x.latDistStd, _x.longVelStd, _x.latVelStd, _x.longAccelStd, _x.latAccelStd, _x.motionStatus, _x.detectionSensor, _x.type, _x.refPoint, _x.trackerStatus, _x.visionDetectionSnesor,) = _get_struct_4I17f6I().unpack(str[start:end])
        _v23 = val1.obhcInfo
        _x = _v23
        start = end
        end += 16
        (_x.hypoProb, _x.collProb, _x.ttb, _x.hypoLabel,) = _get_struct_3fI().unpack(str[start:end])
        _v24 = val1.othaInfo
        _x = _v24
        start = end
        end += 13
        (_x.aLgtNec, _x.aLatNec, _x.ttc, _x.inPathNow,) = _get_struct_3fB().unpack(str[start:end])
        _v24.inPathNow = bool(_v24.inPathNow)
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        pattern = '<%sf'%length
        start = end
        s = struct.Struct(pattern)
        end += s.size
        val1.reserved = s.unpack(str[start:end])
        self.bicyclist.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.motor = []
      for i in range(0, length):
        val1 = rospy_message_converter.msg.CrenStru()
        _v25 = val1.objInfo
        _x = _v25
        start = end
        end += 108
        (_x.id, _x.visionId, _x.radarId, _x.age, _x.longDist, _x.latDist, _x.longVel, _x.latVel, _x.longAccel, _x.latAccel, _x.heading, _x.curvature, _x.existConfidence, _x.length, _x.width, _x.longDistStd, _x.latDistStd, _x.longVelStd, _x.latVelStd, _x.longAccelStd, _x.latAccelStd, _x.motionStatus, _x.detectionSensor, _x.type, _x.refPoint, _x.trackerStatus, _x.visionDetectionSnesor,) = _get_struct_4I17f6I().unpack(str[start:end])
        _v26 = val1.obhcInfo
        _x = _v26
        start = end
        end += 16
        (_x.hypoProb, _x.collProb, _x.ttb, _x.hypoLabel,) = _get_struct_3fI().unpack(str[start:end])
        _v27 = val1.othaInfo
        _x = _v27
        start = end
        end += 13
        (_x.aLgtNec, _x.aLatNec, _x.ttc, _x.inPathNow,) = _get_struct_3fB().unpack(str[start:end])
        _v27.inPathNow = bool(_v27.inPathNow)
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        pattern = '<%sf'%length
        start = end
        s = struct.Struct(pattern)
        end += s.size
        val1.reserved = s.unpack(str[start:end])
        self.motor.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.obstacle = []
      for i in range(0, length):
        val1 = rospy_message_converter.msg.CrenStru()
        _v28 = val1.objInfo
        _x = _v28
        start = end
        end += 108
        (_x.id, _x.visionId, _x.radarId, _x.age, _x.longDist, _x.latDist, _x.longVel, _x.latVel, _x.longAccel, _x.latAccel, _x.heading, _x.curvature, _x.existConfidence, _x.length, _x.width, _x.longDistStd, _x.latDistStd, _x.longVelStd, _x.latVelStd, _x.longAccelStd, _x.latAccelStd, _x.motionStatus, _x.detectionSensor, _x.type, _x.refPoint, _x.trackerStatus, _x.visionDetectionSnesor,) = _get_struct_4I17f6I().unpack(str[start:end])
        _v29 = val1.obhcInfo
        _x = _v29
        start = end
        end += 16
        (_x.hypoProb, _x.collProb, _x.ttb, _x.hypoLabel,) = _get_struct_3fI().unpack(str[start:end])
        _v30 = val1.othaInfo
        _x = _v30
        start = end
        end += 13
        (_x.aLgtNec, _x.aLatNec, _x.ttc, _x.inPathNow,) = _get_struct_3fB().unpack(str[start:end])
        _v30.inPathNow = bool(_v30.inPathNow)
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        pattern = '<%sf'%length
        start = end
        s = struct.Struct(pattern)
        end += s.size
        val1.reserved = s.unpack(str[start:end])
        self.obstacle.append(val1)
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
      length = len(self.car)
      buff.write(_struct_I.pack(length))
      for val1 in self.car:
        _v31 = val1.objInfo
        _x = _v31
        buff.write(_get_struct_4I17f6I().pack(_x.id, _x.visionId, _x.radarId, _x.age, _x.longDist, _x.latDist, _x.longVel, _x.latVel, _x.longAccel, _x.latAccel, _x.heading, _x.curvature, _x.existConfidence, _x.length, _x.width, _x.longDistStd, _x.latDistStd, _x.longVelStd, _x.latVelStd, _x.longAccelStd, _x.latAccelStd, _x.motionStatus, _x.detectionSensor, _x.type, _x.refPoint, _x.trackerStatus, _x.visionDetectionSnesor))
        _v32 = val1.obhcInfo
        _x = _v32
        buff.write(_get_struct_3fI().pack(_x.hypoProb, _x.collProb, _x.ttb, _x.hypoLabel))
        _v33 = val1.othaInfo
        _x = _v33
        buff.write(_get_struct_3fB().pack(_x.aLgtNec, _x.aLatNec, _x.ttc, _x.inPathNow))
        length = len(val1.reserved)
        buff.write(_struct_I.pack(length))
        pattern = '<%sf'%length
        buff.write(val1.reserved.tostring())
      length = len(self.pedstrain)
      buff.write(_struct_I.pack(length))
      for val1 in self.pedstrain:
        _v34 = val1.objInfo
        _x = _v34
        buff.write(_get_struct_4I17f6I().pack(_x.id, _x.visionId, _x.radarId, _x.age, _x.longDist, _x.latDist, _x.longVel, _x.latVel, _x.longAccel, _x.latAccel, _x.heading, _x.curvature, _x.existConfidence, _x.length, _x.width, _x.longDistStd, _x.latDistStd, _x.longVelStd, _x.latVelStd, _x.longAccelStd, _x.latAccelStd, _x.motionStatus, _x.detectionSensor, _x.type, _x.refPoint, _x.trackerStatus, _x.visionDetectionSnesor))
        _v35 = val1.obhcInfo
        _x = _v35
        buff.write(_get_struct_3fI().pack(_x.hypoProb, _x.collProb, _x.ttb, _x.hypoLabel))
        _v36 = val1.othaInfo
        _x = _v36
        buff.write(_get_struct_3fB().pack(_x.aLgtNec, _x.aLatNec, _x.ttc, _x.inPathNow))
        length = len(val1.reserved)
        buff.write(_struct_I.pack(length))
        pattern = '<%sf'%length
        buff.write(val1.reserved.tostring())
      length = len(self.bicyclist)
      buff.write(_struct_I.pack(length))
      for val1 in self.bicyclist:
        _v37 = val1.objInfo
        _x = _v37
        buff.write(_get_struct_4I17f6I().pack(_x.id, _x.visionId, _x.radarId, _x.age, _x.longDist, _x.latDist, _x.longVel, _x.latVel, _x.longAccel, _x.latAccel, _x.heading, _x.curvature, _x.existConfidence, _x.length, _x.width, _x.longDistStd, _x.latDistStd, _x.longVelStd, _x.latVelStd, _x.longAccelStd, _x.latAccelStd, _x.motionStatus, _x.detectionSensor, _x.type, _x.refPoint, _x.trackerStatus, _x.visionDetectionSnesor))
        _v38 = val1.obhcInfo
        _x = _v38
        buff.write(_get_struct_3fI().pack(_x.hypoProb, _x.collProb, _x.ttb, _x.hypoLabel))
        _v39 = val1.othaInfo
        _x = _v39
        buff.write(_get_struct_3fB().pack(_x.aLgtNec, _x.aLatNec, _x.ttc, _x.inPathNow))
        length = len(val1.reserved)
        buff.write(_struct_I.pack(length))
        pattern = '<%sf'%length
        buff.write(val1.reserved.tostring())
      length = len(self.motor)
      buff.write(_struct_I.pack(length))
      for val1 in self.motor:
        _v40 = val1.objInfo
        _x = _v40
        buff.write(_get_struct_4I17f6I().pack(_x.id, _x.visionId, _x.radarId, _x.age, _x.longDist, _x.latDist, _x.longVel, _x.latVel, _x.longAccel, _x.latAccel, _x.heading, _x.curvature, _x.existConfidence, _x.length, _x.width, _x.longDistStd, _x.latDistStd, _x.longVelStd, _x.latVelStd, _x.longAccelStd, _x.latAccelStd, _x.motionStatus, _x.detectionSensor, _x.type, _x.refPoint, _x.trackerStatus, _x.visionDetectionSnesor))
        _v41 = val1.obhcInfo
        _x = _v41
        buff.write(_get_struct_3fI().pack(_x.hypoProb, _x.collProb, _x.ttb, _x.hypoLabel))
        _v42 = val1.othaInfo
        _x = _v42
        buff.write(_get_struct_3fB().pack(_x.aLgtNec, _x.aLatNec, _x.ttc, _x.inPathNow))
        length = len(val1.reserved)
        buff.write(_struct_I.pack(length))
        pattern = '<%sf'%length
        buff.write(val1.reserved.tostring())
      length = len(self.obstacle)
      buff.write(_struct_I.pack(length))
      for val1 in self.obstacle:
        _v43 = val1.objInfo
        _x = _v43
        buff.write(_get_struct_4I17f6I().pack(_x.id, _x.visionId, _x.radarId, _x.age, _x.longDist, _x.latDist, _x.longVel, _x.latVel, _x.longAccel, _x.latAccel, _x.heading, _x.curvature, _x.existConfidence, _x.length, _x.width, _x.longDistStd, _x.latDistStd, _x.longVelStd, _x.latVelStd, _x.longAccelStd, _x.latAccelStd, _x.motionStatus, _x.detectionSensor, _x.type, _x.refPoint, _x.trackerStatus, _x.visionDetectionSnesor))
        _v44 = val1.obhcInfo
        _x = _v44
        buff.write(_get_struct_3fI().pack(_x.hypoProb, _x.collProb, _x.ttb, _x.hypoLabel))
        _v45 = val1.othaInfo
        _x = _v45
        buff.write(_get_struct_3fB().pack(_x.aLgtNec, _x.aLatNec, _x.ttc, _x.inPathNow))
        length = len(val1.reserved)
        buff.write(_struct_I.pack(length))
        pattern = '<%sf'%length
        buff.write(val1.reserved.tostring())
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
      if self.car is None:
        self.car = None
      if self.pedstrain is None:
        self.pedstrain = None
      if self.bicyclist is None:
        self.bicyclist = None
      if self.motor is None:
        self.motor = None
      if self.obstacle is None:
        self.obstacle = None
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.car = []
      for i in range(0, length):
        val1 = rospy_message_converter.msg.CrenStru()
        _v46 = val1.objInfo
        _x = _v46
        start = end
        end += 108
        (_x.id, _x.visionId, _x.radarId, _x.age, _x.longDist, _x.latDist, _x.longVel, _x.latVel, _x.longAccel, _x.latAccel, _x.heading, _x.curvature, _x.existConfidence, _x.length, _x.width, _x.longDistStd, _x.latDistStd, _x.longVelStd, _x.latVelStd, _x.longAccelStd, _x.latAccelStd, _x.motionStatus, _x.detectionSensor, _x.type, _x.refPoint, _x.trackerStatus, _x.visionDetectionSnesor,) = _get_struct_4I17f6I().unpack(str[start:end])
        _v47 = val1.obhcInfo
        _x = _v47
        start = end
        end += 16
        (_x.hypoProb, _x.collProb, _x.ttb, _x.hypoLabel,) = _get_struct_3fI().unpack(str[start:end])
        _v48 = val1.othaInfo
        _x = _v48
        start = end
        end += 13
        (_x.aLgtNec, _x.aLatNec, _x.ttc, _x.inPathNow,) = _get_struct_3fB().unpack(str[start:end])
        _v48.inPathNow = bool(_v48.inPathNow)
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        pattern = '<%sf'%length
        start = end
        s = struct.Struct(pattern)
        end += s.size
        val1.reserved = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=length)
        self.car.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.pedstrain = []
      for i in range(0, length):
        val1 = rospy_message_converter.msg.CrenStru()
        _v49 = val1.objInfo
        _x = _v49
        start = end
        end += 108
        (_x.id, _x.visionId, _x.radarId, _x.age, _x.longDist, _x.latDist, _x.longVel, _x.latVel, _x.longAccel, _x.latAccel, _x.heading, _x.curvature, _x.existConfidence, _x.length, _x.width, _x.longDistStd, _x.latDistStd, _x.longVelStd, _x.latVelStd, _x.longAccelStd, _x.latAccelStd, _x.motionStatus, _x.detectionSensor, _x.type, _x.refPoint, _x.trackerStatus, _x.visionDetectionSnesor,) = _get_struct_4I17f6I().unpack(str[start:end])
        _v50 = val1.obhcInfo
        _x = _v50
        start = end
        end += 16
        (_x.hypoProb, _x.collProb, _x.ttb, _x.hypoLabel,) = _get_struct_3fI().unpack(str[start:end])
        _v51 = val1.othaInfo
        _x = _v51
        start = end
        end += 13
        (_x.aLgtNec, _x.aLatNec, _x.ttc, _x.inPathNow,) = _get_struct_3fB().unpack(str[start:end])
        _v51.inPathNow = bool(_v51.inPathNow)
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        pattern = '<%sf'%length
        start = end
        s = struct.Struct(pattern)
        end += s.size
        val1.reserved = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=length)
        self.pedstrain.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.bicyclist = []
      for i in range(0, length):
        val1 = rospy_message_converter.msg.CrenStru()
        _v52 = val1.objInfo
        _x = _v52
        start = end
        end += 108
        (_x.id, _x.visionId, _x.radarId, _x.age, _x.longDist, _x.latDist, _x.longVel, _x.latVel, _x.longAccel, _x.latAccel, _x.heading, _x.curvature, _x.existConfidence, _x.length, _x.width, _x.longDistStd, _x.latDistStd, _x.longVelStd, _x.latVelStd, _x.longAccelStd, _x.latAccelStd, _x.motionStatus, _x.detectionSensor, _x.type, _x.refPoint, _x.trackerStatus, _x.visionDetectionSnesor,) = _get_struct_4I17f6I().unpack(str[start:end])
        _v53 = val1.obhcInfo
        _x = _v53
        start = end
        end += 16
        (_x.hypoProb, _x.collProb, _x.ttb, _x.hypoLabel,) = _get_struct_3fI().unpack(str[start:end])
        _v54 = val1.othaInfo
        _x = _v54
        start = end
        end += 13
        (_x.aLgtNec, _x.aLatNec, _x.ttc, _x.inPathNow,) = _get_struct_3fB().unpack(str[start:end])
        _v54.inPathNow = bool(_v54.inPathNow)
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        pattern = '<%sf'%length
        start = end
        s = struct.Struct(pattern)
        end += s.size
        val1.reserved = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=length)
        self.bicyclist.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.motor = []
      for i in range(0, length):
        val1 = rospy_message_converter.msg.CrenStru()
        _v55 = val1.objInfo
        _x = _v55
        start = end
        end += 108
        (_x.id, _x.visionId, _x.radarId, _x.age, _x.longDist, _x.latDist, _x.longVel, _x.latVel, _x.longAccel, _x.latAccel, _x.heading, _x.curvature, _x.existConfidence, _x.length, _x.width, _x.longDistStd, _x.latDistStd, _x.longVelStd, _x.latVelStd, _x.longAccelStd, _x.latAccelStd, _x.motionStatus, _x.detectionSensor, _x.type, _x.refPoint, _x.trackerStatus, _x.visionDetectionSnesor,) = _get_struct_4I17f6I().unpack(str[start:end])
        _v56 = val1.obhcInfo
        _x = _v56
        start = end
        end += 16
        (_x.hypoProb, _x.collProb, _x.ttb, _x.hypoLabel,) = _get_struct_3fI().unpack(str[start:end])
        _v57 = val1.othaInfo
        _x = _v57
        start = end
        end += 13
        (_x.aLgtNec, _x.aLatNec, _x.ttc, _x.inPathNow,) = _get_struct_3fB().unpack(str[start:end])
        _v57.inPathNow = bool(_v57.inPathNow)
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        pattern = '<%sf'%length
        start = end
        s = struct.Struct(pattern)
        end += s.size
        val1.reserved = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=length)
        self.motor.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.obstacle = []
      for i in range(0, length):
        val1 = rospy_message_converter.msg.CrenStru()
        _v58 = val1.objInfo
        _x = _v58
        start = end
        end += 108
        (_x.id, _x.visionId, _x.radarId, _x.age, _x.longDist, _x.latDist, _x.longVel, _x.latVel, _x.longAccel, _x.latAccel, _x.heading, _x.curvature, _x.existConfidence, _x.length, _x.width, _x.longDistStd, _x.latDistStd, _x.longVelStd, _x.latVelStd, _x.longAccelStd, _x.latAccelStd, _x.motionStatus, _x.detectionSensor, _x.type, _x.refPoint, _x.trackerStatus, _x.visionDetectionSnesor,) = _get_struct_4I17f6I().unpack(str[start:end])
        _v59 = val1.obhcInfo
        _x = _v59
        start = end
        end += 16
        (_x.hypoProb, _x.collProb, _x.ttb, _x.hypoLabel,) = _get_struct_3fI().unpack(str[start:end])
        _v60 = val1.othaInfo
        _x = _v60
        start = end
        end += 13
        (_x.aLgtNec, _x.aLatNec, _x.ttc, _x.inPathNow,) = _get_struct_3fB().unpack(str[start:end])
        _v60.inPathNow = bool(_v60.inPathNow)
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        pattern = '<%sf'%length
        start = end
        s = struct.Struct(pattern)
        end += s.size
        val1.reserved = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=length)
        self.obstacle.append(val1)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_3fB = None
def _get_struct_3fB():
    global _struct_3fB
    if _struct_3fB is None:
        _struct_3fB = struct.Struct("<3fB")
    return _struct_3fB
_struct_3fI = None
def _get_struct_3fI():
    global _struct_3fI
    if _struct_3fI is None:
        _struct_3fI = struct.Struct("<3fI")
    return _struct_3fI
_struct_4I17f6I = None
def _get_struct_4I17f6I():
    global _struct_4I17f6I
    if _struct_4I17f6I is None:
        _struct_4I17f6I = struct.Struct("<4I17f6I")
    return _struct_4I17f6I

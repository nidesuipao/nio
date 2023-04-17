#!/usr/bin/python3
from distutils.version import StrictVersion
from google import protobuf
if StrictVersion(protobuf.__version__) < StrictVersion('3.9.6'):
    raise Exception("You must have protobuf > 3.9.6")

import os, math
import struct
from datetime import datetime
from google.protobuf.json_format import MessageToJson
from google.protobuf.message import DecodeError
from env import Environment, ddprint
from color import info, warn, error

import sys
python_root=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.join(python_root, "messages"))


class Bag:
    def __init__(self, path, path_write = None):
        self.file=open(path,'rb')
        if path_write != None:
            self.file_write = open(path_write, 'wb')
        self.filename=path
        self.filesize=os.path.getsize(path)
        self.filepos=0
        self.eof=False
        self.topic=os.path.basename(path).replace(".pb.dat","").replace("-","/")
        self.current_frame=None
        self.current_timestamp=-1
        self.current_frame_size=-1
        self.env = Environment()

        if not self.env.find_messages():
            # raise Exception("No proto messages found.")
            print(warn() + __file__ + ": No proto messages found.")

        self.messagetype=self.env.messagetype(self.topic)
        if self.messagetype is None:
            # raise Exception("No message found for topic: " + self.topic)
            print(warn() + __file__ + ": No message found for topic: " + self.topic)

    def reset(self):
        self.file.seek(0, os.SEEK_SET)

    def pos(self):
        return self.file.tell()

    def spilt(self, start_t, end_t):
        recv_ts_ptp = None
        send_ts_ptp = None
        recv_ts = None
        send_ts = None
        fsize= None
        cnt = 0
        try:
            if self.pos() < self.filesize:
                recv_ts_ptp = self.current_timestamp=struct.unpack("l",self.file.read(8))[0]
                send_ts_ptp = self.current_timestamp=struct.unpack("l",self.file.read(8))[0]
                ret = self.current_timestamp=struct.unpack("l",self.file.read(8))[0]
                if 1600000000000000000 < int(ret) < 2000000000000000000:
                    recv_ts = ret
                    send_ts = self.current_timestamp=struct.unpack("l",self.file.read(8))[0]
                    fsize = self.current_frame_size=struct.unpack("l",self.file.read(8))[0]
                    cnt = 40
                else:
                    recv_ts = recv_ts_ptp
                    send_ts = send_ts_ptp
                    self.current_timestamp = send_ts_ptp
                    fsize = self.current_frame_size = ret
                    cnt = 24

                feed_time = float(timestamp2str(recv_ts / 1e9).split(' ')[1].replace(':', ''))
                # print(recv_ts)
                # print(feed_time)
                if feed_time >= start_t and feed_time <= end_t:
                    self.file.seek(-cnt, 1)
                    self.file_write.write(self.file.read(cnt+fsize))
                else:
                    self.file.read(fsize)
                if self.pos() == self.filesize:
                    self.eof = True
        except DecodeError:
            pass
        except Exception as e:
            print(e)
        

    def read_raw(self):
        recv_ts_ptp = None
        send_ts_ptp = None
        recv_ts = None
        send_ts = None
        fsize= None
        raw = None
        try:
            if self.pos() < self.filesize:
                recv_ts_ptp = self.current_timestamp=struct.unpack("l",self.file.read(8))[0]
                send_ts_ptp = self.current_timestamp=struct.unpack("l",self.file.read(8))[0]
                ret = self.current_timestamp=struct.unpack("l",self.file.read(8))[0]
                if 1600000000000000000 < int(ret) < 2000000000000000000:
                    recv_ts = ret
                    send_ts = self.current_timestamp=struct.unpack("l",self.file.read(8))[0]
                    fsize = self.current_frame_size=struct.unpack("l",self.file.read(8))[0]
                else:
                    recv_ts = recv_ts_ptp
                    send_ts = send_ts_ptp
                    self.current_timestamp = send_ts_ptp
                    fsize = self.current_frame_size = ret
                raw = self.file.read(self.current_frame_size)
                if self.pos() == self.filesize:
                    self.eof=True

            else:
                self.eof=True
        except DecodeError:
            pass
        except Exception as e:
            print(e)

        return raw, fsize, recv_ts, send_ts, recv_ts_ptp, send_ts_ptp

    def read(self):
        recv_ts_ptp = None
        send_ts_ptp = None
        recv_ts = None
        send_ts = None
        fsize= None
        frame = None
        try:
            if self.pos() < self.filesize:
                recv_ts_ptp = self.current_timestamp=struct.unpack("l",self.file.read(8))[0]
                send_ts_ptp = self.current_timestamp=struct.unpack("l",self.file.read(8))[0]
                ret = self.current_timestamp=struct.unpack("l",self.file.read(8))[0]
                if 1600000000000000000 < int(ret) < 2000000000000000000:
                    recv_ts = ret
                    send_ts = self.current_timestamp=struct.unpack("l",self.file.read(8))[0]
                    fsize = self.current_frame_size=struct.unpack("l",self.file.read(8))[0]
                else:
                    recv_ts = recv_ts_ptp
                    send_ts = send_ts_ptp
                    self.current_timestamp = send_ts_ptp
                    fsize = self.current_frame_size = ret
                frame = self.messagetype.FromString(self.file.read(self.current_frame_size))
                self.current_frame = frame
                if self.pos() == self.filesize:
                    self.eof=True

            else:
                self.eof=True
        except DecodeError:
            pass
        except Exception as e:
            print(e)

        return frame, fsize, recv_ts, send_ts, recv_ts_ptp, send_ts_ptp

    def read_as_json(self, use_integers_for_enums=True,
                     preserving_proto_field_name=True,
                     including_default_value_fields=True):
        proto,*_=self.read()
        if proto is None:
            return ""
        else:
            return MessageToJson(proto,
                                 use_integers_for_enums=use_integers_for_enums,
                                 preserving_proto_field_name=preserving_proto_field_name,
                                 including_default_value_fields=including_default_value_fields)

    def read_as_plot_json(self):
        j=self.read_as_json()
        if j:
            buf="{\""+self.topic+"\":"+j+",\"timestamp\":"+str(self.current_timestamp/1e9)+"}"
            return buf
        else:
            return ""

    def close(self):
        self.file.close()

    def w_close(self):
        self.file_write.close()

    @staticmethod
    def Print(filename):
        bag = Bag(filename)
        pre_pub_t=-1
        pre_sub_t=-1
        count=0
        while not bag.eof:
            msg, size, sub_t, pub_t, sub_t_ptp, pub_t_ptp = bag.read()
            print(msg)
            print("%-6s" % count,
                    datetime.fromtimestamp(pub_t/1e9).isoformat(),
                    "pub:",pub_t,
                    "(",'%6.1f' % ((pub_t-pre_pub_t)/1e6 if pre_pub_t>0 else 0),"ms)",
                    "sub:",sub_t,
                    "(","%6.1f" % ((sub_t-pre_sub_t)/1e6 if pre_sub_t>0 else 0),"ms)",
                    "trip:", (sub_t-pub_t)/1e6,
                    "size=",size,
                    "pos:", bag.pos(), "/", bag.filesize, int(100*bag.pos()/bag.filesize),"%",
                    bag.topic,
                    bag.messagetype.__name__
                )
            pre_pub_t=pub_t
            pre_sub_t=sub_t
            count+=1

        bag.close()

def timestamp2str(timestamp):
    b1 = math.modf(timestamp)[1]
    b0 = math.modf(timestamp)[0]
    time_str = datetime.strftime(datetime.fromtimestamp(b1), '%Y-%m-%d %H:%M:%S') \
                + '.' + str(b0).split('.')[1][0:4]
    return time_str
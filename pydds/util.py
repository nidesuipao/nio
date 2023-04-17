from distutils.version import StrictVersion
from google import protobuf
if StrictVersion(protobuf.__version__) < StrictVersion('3.9.6'):
    raise Exception("You must have protobuf > 3.9.6")

import sys,math,os, json
import numpy as np
from datetime import datetime
from google.protobuf.json_format import MessageToJson
from google.protobuf.message import DecodeError
import color
from color import info, info_all, warn, error
from bag import Bag
import cv2
import tqdm
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

sys.path.append('./')

class RecorcParser:
    def __init__(self, dict_topic, start_t, end_t) -> None:
        self.dict_topic = dict_topic
        self.start_t = float(start_t)
        self.end_t = float(end_t)
        self.arr_topic_name = dict_topic.values()
        self.arr_json_topic_name = {}
        self.dict_pb_msg = {}
        self.dict_msg_counter = {}
        self.dict_aligned_index_of_fct = {} # 从fct视角对齐所有消息
        self.dict_aligned_index_of_rm = {} 
        self.dict_aligned_index_of_dt = {} # 按照固定周期的方式对其所有消息,数据结构：topic_name: [publish_ts, index]

        self.dict_json_msg = {}
        for name in self.arr_topic_name:
            self.dict_pb_msg[name] = []
            self.dict_aligned_index_of_fct[name] = []
            self.dict_aligned_index_of_dt[name] = []

        for name in self.arr_json_topic_name:
            self.dict_json_msg[name] = []


    def Split(self, record_path):
        for f in os.listdir(record_path):
            data_file = os.path.join(record_path, f)
            print(info() + 'record data file: ' + data_file)
            if '.pb.dat' not in data_file:
                print(error() + 'record file: ' + data_file + 'is invalid.')
                continue
            topic = os.path.basename(data_file).replace(".pb.dat","").replace("-","/")
            if topic not in self.arr_topic_name:
                continue
            print(info_all('begin split msg of topic: ' + topic))
            bag = Bag(data_file, record_path + '/../split/' + f)
            pre_pub_t=-1
            pre_sub_t=-1
            count=0
            while not bag.eof:
                bag.spilt(self.start_t, self.end_t)
            bag.w_close()
            bag.close()
            print(info_all('finish split msg of topic: ' + topic))

    def FindToJson(self, record_path, dict_frame_counter):
        dict_json_msg = {}
        for key in dict_frame_counter.keys():
            dict_json_msg[key] = []
        for f in os.listdir(record_path):
            data_file = os.path.join(record_path, f)
            print(info() + 'record data file: ' + data_file)
            if '.pb.dat' not in data_file:
                print(error() + 'record file: ' + data_file + 'is invalid.')
                continue
            topic = os.path.basename(data_file).replace(".pb.dat","").replace("-","/")
            if topic not in dict_frame_counter.keys():
                print('skip convert msg of topic: ' + topic)
                continue
            print(info_all('begin convert msg of topic to json file: ' + topic))
            bag = Bag(data_file)
            while not bag.eof:
                msg = bag.read_as_json()
                json_msg = json.loads(msg)
                if int(json_msg['counter']) >= int(dict_frame_counter[topic][0]) and \
                    int(json_msg['counter']) <= int(dict_frame_counter[topic][-1]):
                    # print("find the " + json_msg['counter'] + " frame msg of " + topic)
                    dict_json_msg[topic].append([int(json_msg['counter']), msg])
            bag.close()
            print(info_all('finish convert msg of topic to json: ' + topic))
        return dict_json_msg

    def Parser(self, record_path, parse_mode):
        for f in os.listdir(record_path):
            data_file = os.path.join(record_path, f)
            print(info() + 'record data file: ' + data_file)
            if '.pb.dat' not in data_file:
                print(error() + 'record file: ' + data_file + 'is invalid.')
                continue
            topic = os.path.basename(data_file).replace(".pb.dat","").replace("-","/")
            if topic not in self.arr_topic_name:
                print(info_all('skip parse msg of topic: ' + topic))
                continue
            print(info_all('begin parse msg of topic: ' + topic))
            bag = Bag(data_file)
            pre_pub_t=-1
            pre_sub_t=-1
            count=0
            while not bag.eof:
                if parse_mode == "pb_msg":
                    msg, size, sub_t, pub_t, sub_t_ptp, pub_t_ptp = bag.read()
                elif parse_mode == "str_msg":
                    msg, size, sub_t, pub_t, sub_t_ptp, pub_t_ptp = bag.read_raw()
                elif parse_mode == "json_msg":
                    msg = bag.read_as_json()

                if sub_t == None or pub_t == None or msg == None:
                    continue
                feed_time = float(timestamp2str(sub_t / 1e9).split(' ')[1].replace(':', ''))
                if feed_time < self.start_t or feed_time > self.end_t:
                    continue
                self.dict_pb_msg[topic].append([sub_t, msg])
                #print(sub_t)
                # if topic == 'common/vehicle_in/vehicle_10ms':
                #     self.dict_json_msg[topic].append([sub_t, '<div>' + MessageToJson(msg, use_integers_for_enums=True, \
                #         preserving_proto_field_name=True, including_default_value_fields=True).replace(' ', '&nbsp;').replace('\n', '<br/>') + '</div>'])
                pre_pub_t=pub_t
                pre_sub_t=sub_t
                count+=1
            bag.close()
            print(info_all('finish parse msg of topic: ' + topic))
        return self.dict_pb_msg

    def SearchAndAlignedMsgIndexByFixedDt(self, dt):
        start_t = None
        all_topics = self.dict_pb_msg.keys()
        for topic in all_topics:
            print(topic)
            if start_t == None:
                start_t = self.dict_pb_msg[topic][0][0]
            elif start_t < self.dict_pb_msg[topic][0][0]:
                start_t = self.dict_pb_msg[topic][0][0]
        search_finish = False
        forward_t = start_t + dt * 1e9 # unit : ns, dt unit : second
        dict_search_index = {}
        for topic in all_topics:
            dict_search_index[topic] = 0
        while not search_finish:
            search_finish = False
            for topic in all_topics:
                while self.dict_pb_msg[topic][dict_search_index[topic]][0] < forward_t:
                    dict_search_index[topic] = dict_search_index[topic] + 1
                    if dict_search_index[topic] >= len(self.dict_pb_msg[topic]) - 1:
                        print(dict_search_index)
                        print(topic, "exceed max length: ", dict_search_index[topic], len(self.dict_pb_msg[topic]) - 1)
                        search_finish = True
                        break
                str_t = timestamp2str(self.dict_pb_msg[topic][dict_search_index[topic] - 1][0] / 1e9)
                counter = self.dict_pb_msg[topic][dict_search_index[topic] - 1][1].counter
                # print(timestamp2str(forward_t/1e9), topic, dict_search_index[topic] - 1, str_t)
                self.dict_aligned_index_of_dt[topic].append([dict_search_index[topic] - 1, str_t, counter])
            #update dict_aligned_index_of_dt
            forward_t = forward_t + dt * 1e9
        return self.dict_aligned_index_of_dt

    def SearchAndAlignedMsgIndexByRM(self):
        dict_index_cnt = {}
        for name in self.arr_topic_name:
            dict_index_cnt[name] = None
        if self.dict_topic['road_model'] in self.dict_pb_msg.keys():
            rm_topic_name = self.dict_topic['road_model']
            for i in range(len(self.dict_pb_msg[rm_topic_name])):
                self.dict_aligned_index_of_rm[rm_topic_name].append(i)
                dict_index_cnt[rm_topic_name] = i
                fct_sub_t = self.dict_pb_msg[rm_topic_name][i][0]
                for topic in self.arr_topic_name:
                    if topic == rm_topic_name:
                        continue
                    search_index = 0
                    if dict_index_cnt[topic] != None:
                        search_index = dict_index_cnt[topic] + 1
                    this_sub_t = self.dict_pb_msg[topic][search_index][0]
                    while this_sub_t < fct_sub_t and search_index < len(self.dict_pb_msg[topic]):
                        this_sub_t = self.dict_pb_msg[topic][search_index][0]
                        search_index = search_index + 1

                    self.dict_aligned_index_of_rm[topic].append(search_index - 1)
                    dict_index_cnt[rm_topic_name] = search_index - 1
        return self.dict_aligned_index_of_rm

    def SearchAndAlignedMsgIndexByFct(self):
        dict_index_cnt = {}
        for name in self.arr_topic_name:
            dict_index_cnt[name] = None
        if self.dict_topic['fct_out'] in self.dict_pb_msg.keys():
            fct_topic_name = self.dict_topic['fct_out']
            for i in range(len(self.dict_pb_msg[fct_topic_name])):
                self.dict_aligned_index_of_fct[fct_topic_name].append(i)
                dict_index_cnt[fct_topic_name] = i
                fct_sub_t = self.dict_pb_msg[fct_topic_name][i][0]
                for topic in self.arr_topic_name:
                    if topic == fct_topic_name:
                        continue
                    search_index = 0
                    if dict_index_cnt[topic] != None:
                        search_index = dict_index_cnt[topic]
                    this_sub_t = self.dict_pb_msg[topic][search_index][0]
                    while this_sub_t < fct_sub_t and search_index < len(self.dict_pb_msg[topic]):
                        this_sub_t = self.dict_pb_msg[topic][search_index][0]
                        search_index = search_index + 1

                    self.dict_aligned_index_of_fct[topic].append(search_index - 1)
                    dict_index_cnt[fct_topic_name] = search_index - 1
        return self.dict_aligned_index_of_fct
  
class PbMsgParser:
    def __init__(self, dict_topic) -> None:
        self.ad_geometry = ADGeometry()
        self.dict_topic = dict_topic

    def RoadModelData(self, msg_road_model):
        res = {'t':[], 'cnt':[], 'frame':[{'lines':[], 'car_polygon':{'xs':[],'ys':[]}}]}
        for i in range(len(msg_road_model)):
            cell = msg_road_model[i]
            res['t'].append(timestamp2str(cell[1].publish_ts / 1e9))
            res['cnt'].append(cell[1].counter)
            one_frame = {'lines':[], 'car_polygon':{'xs':[],'ys':[]}}
            for line in cell[1].line_infos:
                dict_line = {'role': None, 'id': None, 'c0': None, \
                    'c1': None, 'c2': None, 'c3': None, 'start': None, \
                    'end': None, 'poly_points': {'xs':[], 'ys':[]},\
                    'points': {'xs':[], 'ys':[], 'zs':[]}}
                dict_line['role'] = line.role
                dict_line['id'] = line.id
                dict_line['c0'] = line.c0
                dict_line['c1'] = line.c1
                dict_line['c2'] = line.c2
                dict_line['c3'] = line.c3
                dict_line['start'] = line.start
                dict_line['end'] = line.end
                for x in np.arange(line.start, line.end, 0.2):
                    dict_line['poly_points']['xs'].append(x)
                    y = line.c0 + line.c1*x + line.c2*x*x + line.c3*x*x*x
                    dict_line['poly_points']['ys'].append(y)
                for p in line.points:
                    dict_line['points']['xs'].append(p.x)
                    dict_line['points']['ys'].append(p.y)
                    dict_line['points']['zs'].append(p.z)
                one_frame['lines'].append(dict_line)

            ### trans to relative coord
            # rel_local_msg_index = dict_aligned_index_of_rm[self.dict_topic['relative_localization']][i]
            # rel_local_msg = msg_relative_localization[rel_local_msg_index][1]
            # car_box = self.ad_geometry.tf_car2world_2d(rel_local_msg.position.x, rel_local_msg.position.y, rel_local_msg.euler_angle.yaw)
            car_box = self.ad_geometry.tf_car2world_2d(0.0, 0.0, 0.0)

            # dict_car_box = {'xs':[], 'ys':[]}
            # dict_car_box['xs'] = adc_box[0]
            # dict_car_box['ys'] = adc_box[1]
            one_frame['car_polygon']['xs'] = car_box[0]
            one_frame['car_polygon']['ys'] = car_box[1]
            res['frame'].append(one_frame)
        return res

    def RelativeLocalizationData(self, msg_relative_localization):
        res = {'t':[], 'cnt':[], 'rel_xs':[], 'rel_ys':[]}
        for cell in msg_relative_localization:
            res['t'].append(timestamp2str(cell[1].publish_ts / 1e9))
            res['cnt'].append(int(cell[1].counter))
            res['rel_xs'].append(float(cell[1].position.x))
            res['rel_ys'].append(float(cell[1].position.y))
        return res


    def EhyTseData(self, msg_ehy_tse):
        res = {'t':[], 'cnt':[], 'frame': []}
        for cell in msg_ehy_tse:
            res['t'].append(timestamp2str(cell[1].publish_ts / 1e9))
            res['cnt'].append(int(cell[1].counter))
            ehy_tse = {'cipv_lost': None, 'objs':[], 'ego_polygon':{'xs':[],'ys':[]}}
            ehy_tse['cipv_lost'] = cell[1].tsi_flg_cipv_lost
            for obj in cell[1].tse_obj:
                tgt_obj = {'id':None, 'obj_index':None, 'car_polygon':{'xs':[],'ys':[]}, 'age':None}
                tgt_obj['id'] = int(obj.age)
                tgt_obj['obj_index'] = int(obj.obj_index)
                # self.ad_geometry.set_width_length(float(obj.width), float(obj.length))
                car_box = self.ad_geometry.tf_car2world_2d(float(obj.lon_pos_vcs), float(obj.lat_pos_vcs), float(obj.phi_angle))
                tgt_obj['car_polygon']['xs'] = car_box[0]
                tgt_obj['car_polygon']['ys'] = car_box[1]
                ehy_tse['objs'].append(tgt_obj)
            # print(len(cell[1].tse_obj), ehy_tse)
            car_box = self.ad_geometry.tf_car2world_2d(0.0, 0.0, 0.0)
            ehy_tse['ego_polygon']['xs'] = car_box[0]
            ehy_tse['ego_polygon']['ys'] = car_box[1]
            res['frame'].append(ehy_tse)
        return res

    def FctData(self, msg_fct):
        res = {'t':[], 'r_t':[],'cnt':[], 'AbsltPinionAgReq':[], 'LatCtrlActv':[], 'TargetAccel':[], 'VlcReqFct':[]}
        first_timestamp = None
        for cell in msg_fct:
            if first_timestamp == None:
                first_timestamp = cell[0]
                res['r_t'].append(0)
            else:
                res['r_t'].append(cell[0] / 1e9 - first_timestamp / 1e9)

            res['t'].append(timestamp2str(cell[1].publish_ts / 1e9))
            res['cnt'].append(int(cell[1].counter))
            res['AbsltPinionAgReq'].append(float(cell[1].LatCtrl.AbsltPinionAgReq))
            res['LatCtrlActv'].append(float(cell[1].LatCtrl.LatCtrlActv))
            res['TargetAccel'].append(float(cell[1].LonCtrl.TargetAccel))
            res['VlcReqFct'].append(float(cell[1].LonCtrl.VlcReqFct))
        return res

    def RmeLine2Json(self, rme_line):
        line = {'pt_conf': None, 'c0': None, 'c1': None, 'c2': None, 'c3': None, \
                'lrange_start': None, 'lrange_end': None, 'lm_width': None, \
                    'poly_points': {'xs':[], 'ys':[]}}
        line['pt_conf'] = rme_line.pt_conf
        line['c0'] = float(rme_line.c0)
        line['c1'] = float(rme_line.c1)
        line['c2'] = float(rme_line.c2)
        line['c3'] = float(rme_line.c3)
        line['lrange_start'] = float(rme_line.lrange_start)
        line['lrange_end'] = float(rme_line.lrange_end)
        line['lm_width'] = float(rme_line.lm_width)
        for x in np.arange(line['lrange_start'], line['lrange_end'], 1.0):
            line['poly_points']['xs'].append(x)
            y = line['c0'] + line['c1']*x + line['c2']*x*x + line['c3']*x*x*x
            line['poly_points']['ys'].append(y)
        return line

    def EhyRmeData(self, msg_ehy_rme):
        line = {'pt_conf': None, 'c0': None, \
                    'c1': None, 'c2': None, 'c3': None, 'lrange_start': None, \
                    'lrange_end': None, 'poly_points': {'xs':[], 'ys':[]}}
        Lane = {'host_lane':{'left_line': None, 'right_line': None, 'lane_start':None, 'lane_end':None}}
        res = {'t':[], 'cnt':[], 'frame':[]}
        for cell in msg_ehy_rme:
            res['t'].append(timestamp2str(cell[1].publish_ts / 1e9))
            res['cnt'].append(cell[1].counter)
            frame_lane = Lane
            frame_lane['host_lane']['left_line'] = self.RmeLine2Json(cell[1].host_lane.left_line)
            frame_lane['host_lane']['right_line'] = self.RmeLine2Json(cell[1].host_lane.right_line)
            frame_lane['host_lane']['lane_start'] = cell[1].host_lane.lane_start
            frame_lane['host_lane']['lane_end'] = cell[1].host_lane.lane_end
            res['frame'].append(frame_lane)
        return res
    
    def Veh10msData(self, msg_veh_10ms):
        res = {'t':[], 'cnt':[], 'frame':[]}
        for cell in msg_veh_10ms:
            res['t'].append(timestamp2str(cell[1].publish_ts / 1e9))
            res['cnt'].append(cell[1].counter)

    def Veh50msData(self, msg_veh_50ms):
        res = {'t':[], 'cnt':[], 'frame':[]}
        for cell in msg_veh_50ms:
            res['t'].append(timestamp2str(cell[1].publish_ts / 1e9))
            res['cnt'].append(cell[1].counter)

    def ParseOnePolyLine(self, poly_line):
        poly_line = {}
        poly_line['pt_conf'] = poly_line.pt_conf
        return poly_line

###########################################################################
def timestamp2str(timestamp):
    b1 = math.modf(timestamp)[1]
    b0 = math.modf(timestamp)[0]
    time_str = datetime.strftime(datetime.fromtimestamp(b1), '%Y-%m-%d %H:%M:%S') \
                + '.' + str(b0).split('.')[1][0:4]
    return time_str

class ADGeometry:
    def __init__(self):
        front_edge_to_center = 3.5
        back_edge_to_center = 1
        right_edge_to_center = 1.2
        left_edge_to_center = 1.2
        self.car_box = [[front_edge_to_center, \
            front_edge_to_center, \
            -back_edge_to_center, \
            -back_edge_to_center, \
            front_edge_to_center],\
            [right_edge_to_center,\
            -left_edge_to_center,\
            -left_edge_to_center,\
            right_edge_to_center,\
            right_edge_to_center]]

    def set_width_length(self, width, length):
        self.width = width
        self.length = length
        self.car_box= [[length/2, \
            length/2, \
            -length/2, \
            -length/2, \
            length/2],\
            [width/2,\
            -width/2,\
            -width/2,\
            width/2,\
            width/2]]
    
    def tf_car2world_2d(self, x0_w, y0_w, theta_w):
        world_box = [[],[]]
        for i in range(len(self.car_box[0])):
            cos = math.cos(theta_w)
            sin = math.sin(theta_w)
            x_w = cos * self.car_box[0][i] - sin * self.car_box[1][i] + x0_w
            y_w = sin * self.car_box[0][i] + cos * self.car_box[1][i] + y0_w
            world_box[0].append(x_w)
            world_box[1].append(y_w)
        return world_box
    
    def point_car2world_2d(self, x0_w, y0_w, theta_w, car_x, car_y):
        cos = math.cos(theta_w)
        sin = math.sin(theta_w)
        x_w = cos * car_x - sin * car_y + x0_w
        y_w = sin * car_x + cos * car_y + y0_w
        return x_w, y_w

def timestamp2str(timestamp):
    b1 = math.modf(timestamp)[1]
    b0 = math.modf(timestamp)[0]
    time_str = datetime.strftime(datetime.fromtimestamp(b1), '%Y-%m-%d %H:%M:%S') \
                + '.' + str(b0).split('.')[1][0:4]
    return time_str

class video_cut():
    def __init__(self, video_dir, out_record_dir, signal_change_times, interval, date) -> None:
        self.video_dir = video_dir
        self.out_record_dir = out_record_dir
        self.signal_change_times = signal_change_times
        self.interval = interval
        self.date = date
        self.total_frame = 0
    

    def handle_video(self):
        for video_name in os.listdir(self.video_dir):
            if 'h264' not in video_name:
                continue
            video_path = os.path.join(self.video_dir, video_name)
            txt_name = video_name[:-4] + 'txt'
            txt_path = os.path.join(self.video_dir, txt_name)
            if not os.path.exists(txt_path):
                print(os.path.join(self.video_dir, txt_path) + " not exist")

            #start_frame, end_frame = self.get_frame(txt_path, self.out_record_dir, txt_name)
            #self.cut(video_path, video_name, self.out_record_dir, start_frame, end_frame)
            self.bin_cut(video_path, video_name, self.out_record_dir)

    def bin_cut(self, video_path, video_name, out_record_dir):
            findkey = '\\x00\\x00\\x00\\x01\\x06\\x05\\x'
            binFile=open(video_path,'rb')
            video_write = []
            #print(self.signal_change_times) #1680514606968462016
            for f_index in range(len(self.signal_change_times)):
                out_video_dir = os.path.join(out_record_dir, \
                                        self.date + '-' + str(self.signal_change_times[f_index]), \
                                        'camera')
                if not os.path.exists(out_video_dir):
                    os.mkdir(out_video_dir)
                video_write.append(open(os.path.join(out_video_dir, video_name), "wb"))
            
            video_is_write = [False] * len(self.signal_change_times)
            binFile.seek(0, 2)
            eof = binFile.tell()
            binFile.seek(0, 0)
            line = binFile.readline()
            while True:
                to_search = str(line.strip())
                # print(to_search)
                # find head '\x00\x00\x00\x01\x06\x05\x'
                index1 = to_search.find(findkey)
                #print(index1)
                if index1 != -1:
                    index2 = index1 + 28
                    length1 = len(to_search)
                    for i in range(1, 99):
                        if index2 + i < length1 and to_search[index2 + i] == ' ':
                            index_ii = index2 + i
                            break
                    if index2 + i > length1:
                        line = binFile.readline()
                        continue
                    # print(ii)
                    timestamp = to_search[index_ii+1:index_ii+17]
                    
                    timestamp_ns = int(timestamp) * 1e3
                    for f_index in range(len(self.signal_change_times)):
                        st = self.signal_change_times[f_index] - self.interval/2
                        et = self.signal_change_times[f_index] + self.interval/2
                        if(timestamp_ns > st and timestamp_ns < et):
                            video_is_write[f_index] = True
                        else:
                            video_is_write[f_index] = False
                
                for f_index in range(len(self.signal_change_times)):
                    if video_is_write[f_index]:
                        video_write[f_index].write(line)
                line = binFile.readline()
                if binFile.tell() >= eof:
                	break
    
    def get_frame(self, txt_path, out_record_dir, txt_name):
        f = open(txt_path, 'r')
        f2 = []
        for f_index in range(len(self.signal_change_times)):
            out_txt_dir = os.path.join(out_record_dir, \
                                       self.date + '-' + str(self.signal_change_times[f_index]), \
                                       'camera')
            if not os.path.exists(out_txt_dir):
                os.mkdir(out_txt_dir)
            f2.append(open(os.path.join(out_txt_dir, txt_name), 'w'))

        start_frame = [-1] * len(self.signal_change_times)
        end_frame = [-1] * len(self.signal_change_times)

        for l in f:
            self.total_frame += 1
            line = l.split()
            end_time = int(line[1])
            frame = int(line[3])
            for f_index in range(len(self.signal_change_times)):
                start_ts = self.signal_change_times[f_index] - self.interval/2
                end_ts = self.signal_change_times[f_index] + self.interval/2
                if end_time >= start_ts and end_time <= end_ts:
                    f2[f_index].writelines(l)
                    if start_frame[f_index] == -1:
                        start_frame[f_index] = frame
                    end_frame[f_index] = frame
        f.close()
        return start_frame, end_frame

    def cut(self, input_video, video_name, out_record_dir, start_frame, end_frame):
        video_caputre = cv2.VideoCapture(input_video)
        # get video parameters
        fps = video_caputre.get(cv2.CAP_PROP_FPS)
        width = video_caputre.get(cv2.CAP_PROP_FRAME_WIDTH)
        height = video_caputre.get(cv2.CAP_PROP_FRAME_HEIGHT)

        # print("fps:", fps)
        # print("width:", width)
        # print("height:", height)

        # 定义截取尺寸,后面定义的每帧的h和w要于此一致，否则视频无法播放
        split_width = int(width)
        split_height = int(height)
        size = (split_width, split_height)

        # fourcc = cv2.VideoWriter_fourcc(*'avc1')
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        # fourcc = 0x7634706d
        
        # 创建视频写入对象
        videp_write = []
        for f_index in range(len(self.signal_change_times)):
            out_video_dir = os.path.join(out_record_dir, \
                                       self.date + '-' + str(self.signal_change_times[f_index]), \
                                       'camera')
            videp_write.append(cv2.VideoWriter(os.path.join(out_video_dir, video_name), fourcc, fps, size))

        # print('Start!!!')
        # 读取视频帧
        success, frame_src = video_caputre.read()  # (960, 2560, 3)  # (height, width, channel)
        i = 0
        pbar = tqdm.tqdm(total = max(end_frame))
        pbar.set_description(video_name + " solveing")
        while success and not cv2.waitKey(1) == 27:  # 读完退出或者按下 esc 退出

            # [width, height] 要与上面定义的size参数一致，注意参数的位置
            # frame_target = frame_src[0:split_height, 0:split_width]  # (split_height, split_width)
            # frame_target = frame_src[0:split_height, split_width:int(width)]  # (split_height, split_width)
            # cv2.imwrite("./pig/" + str(i) + ".jpg", frame_src)
            i += 1
            pbar.update(1)
            # 写入视频文件
            # print(i)
            for f_index in range(len(self.signal_change_times)):
                if i >= start_frame[f_index] and i <= end_frame[f_index]:
                    videp_write[f_index].write(frame_src)
            if i > max(end_frame):
                break
            # 不断读取
            success, frame_src = video_caputre.read()
        # print("Finished!!!")
        video_caputre.release()


def signal2value(info, signal):
    for i in range(1, len(signal)):
        info = getattr(info, signal[i])
    return info


def convert_center_to_leftdown(x_cord, y_cord, angle, width, height):
    xp = x_cord-(math.sqrt(width**2+height**2)/2)*math.cos(math.atan2(height, width)+angle/180*math.pi)
    yp = y_cord-(math.sqrt(width**2+height**2)/2)*math.sin(math.atan2(height, width)+angle/180*math.pi)
    return xp, yp

def analysis(info, t, ana_path, signal, sensor, location, interval):
    # analysis txt generate
    f = open(ana_path + "/analysis.txt", "w")
    info_ = info[t][1]
    cur_timestamp = info[t][0]
    our_vel = "np/debug/dgb_aeb_strtg.carInfo.vLgt".split('.')
    our_accel = "np/debug/dgb_aeb_strtg.carInfo.aLgt".split('.')
    our_angle = "np/debug/dgb_aeb_strtg.carInfo.strAngle".split('.')
    out_angle_speed = "np/debug/dgb_aeb_strtg.carInfo.strSpeed".split('.')

    obj_id_ = "np/debug/dgb_aeb_strtg.crenInfo.objInfo.id".split('.')
    obj_vel = "np/debug/dgb_aeb_strtg.crenInfo.objInfo.longVel".split('.')
    obj_accel = "np/debug/dgb_aeb_strtg.crenInfo.objInfo.longAccel".split('.')
    obj_longdist = "np/debug/dgb_aeb_strtg.crenInfo.objInfo.longDist".split('.')
    obj_latdist = "np/debug/dgb_aeb_strtg.crenInfo.objInfo.latDist".split('.')
    obj_head = "np/debug/dgb_aeb_strtg.crenInfo.objInfo.heading".split('.')
    id = signal2value(info_, obj_id_)
    detect_sensor = "np/apps/ehy_obf_outputs.obf_objects".split('.')
    obj_ttc = "np/debug/dgb_aeb_strtg.crenInfo.othaInfo.ttc".split('.')
    

    f.write("自车速度：" + str(signal2value(info_, our_vel)) + "\n")
    f.write("自车加速度：" + str(signal2value(info_, our_accel)) + "\n")
    f.write("自车转角：" + str(signal2value(info_, our_angle)) + "\n")
    f.write("自车转角速度：" + str(signal2value(info_, out_angle_speed)) + "\n")

    f.write("目标车速度：" + str(signal2value(info_, obj_vel)) + "\n")
    f.write("目标车加速度：" + str(signal2value(info_, obj_accel)) + "\n")
    f.write("目标车位置：" + str(signal2value(info_, obj_longdist)) + " "+str(signal2value(info_, obj_latdist)) + "\n")
    f.write("目标车朝向：" + str(signal2value(info_, obj_head)) + "\n")
    
    
    for d_index in range(len(sensor)):
        if sensor[d_index][0] < cur_timestamp:
            continue
        detect = signal2value(sensor[d_index][1], detect_sensor)
        for d in detect:
            if getattr(getattr(d, "fuseobj"), "id") == id:
                f.write("目标车监测传感器：" + str(getattr(getattr(d, "fuseobj"), "fusion_source")) + "\n")
        if sensor[d_index][0] >= cur_timestamp:
            break
    
    f.write("目标车ttc：" + str(signal2value(info_, obj_ttc)) + "\n")
    last_timetamp = -1
    for i_index in range(t, len(info)):
        if signal2value(info[i_index][1], signal) == True:
            last_timetamp = info[i_index][0]
        else:
            break
    f.write("持续时间：" + str(int(last_timetamp)/1e9 - int(cur_timestamp)/1e9) + "\n")
    f.close()
    #analysis picture generate 
    obj_info = []
    for d_index in range(len(sensor)):
        if sensor[d_index][0] < cur_timestamp:
            continue
        obj_info_total = signal2value(sensor[d_index][1], "np/apps/ehy_obf_outputs.obf_objects".split('.'))
        for obj in obj_info_total:
            obj_id = getattr(getattr(obj, "fuseobj"), "id")
            pos_x = getattr(getattr(getattr(obj, "fuseobj"), "pos_vcs"),"x")
            pos_y = - getattr(getattr(getattr(obj, "fuseobj"), "pos_vcs"),"y")
            obj_type = getattr(getattr(getattr(obj, "fuseobj"), "type"),"obj_main_class")
            obj_head = 6.283 - getattr(getattr(obj, "fuseobj"), "heading")
            width = getattr(getattr(getattr(obj, "fuseobj"), "size"),"length")
            height = getattr(getattr(getattr(obj, "fuseobj"), "size"),"width")
            obj_info.append([obj_id, pos_x, pos_y, obj_type, obj_head, width, height])
        break
        
    obj_info = np.array(obj_info)
    _width = max(obj_info[:,1]) - min(obj_info[:,1])
    _height = max(obj_info[:,2]) - min(obj_info[:,2])
    # ax.set_xlim((_min, _max))
    # ax.set_ylim((_min, _max))
    fig = plt.figure(figsize=(40, 40*_height/_width))
    ax = fig.add_subplot()

    for i in range(obj_info.shape[0]):
        if obj_info[i][0] == id:
            c = 'green'
        else:
            c = 'red'
        if abs(float(obj_info[i][4])) >= 0.0001:
            head = float(obj_info[i][4])
            ax.arrow(obj_info[i,1], obj_info[i,2], 2*math.cos(head), 2*math.sin(head), 
                     width = 0.01, head_width = 0.2, color = 'black')
        if int(obj_info[i][3]) == 1:
            ax.text(obj_info[i,1], obj_info[i,2], int(obj_info[i][0]))
            x,y = convert_center_to_leftdown(obj_info[i,1], obj_info[i,2], obj_info[i][4]*57.3, obj_info[i][5], obj_info[i][6])
            ax.add_patch(plt.Rectangle((x, y), width = obj_info[i][5], height = obj_info[i][6], facecolor = 'none', 
                                       edgecolor = c , angle = obj_info[i][4]*57.3))
        elif int(obj_info[i][3]) == 2:
            ax.text(obj_info[i,1], obj_info[i,2], int(obj_info[i][0]))
            x,y = convert_center_to_leftdown(obj_info[i,1], obj_info[i,2], obj_info[i][4]*57.3, obj_info[i][5], obj_info[i][6])
            ax.add_patch(plt.Rectangle((x, y), width = obj_info[i][5], height = obj_info[i][6], facecolor = 'none', 
                                       edgecolor = c, angle = obj_info[i][4]*57.3))
        elif int(obj_info[i][3]) == 3:
            ax.text(obj_info[i,1], obj_info[i,2], int(obj_info[i][0]))
            x,y = convert_center_to_leftdown(obj_info[i,1], obj_info[i,2], obj_info[i][4]*57.3, obj_info[i][5], obj_info[i][6])
            ax.add_patch(plt.Rectangle((x, y), width = obj_info[i][5], height = obj_info[i][6], facecolor = 'none', 
                                       edgecolor = c, angle = obj_info[i][4]*57.3))
        else:
            ax.scatter(obj_info[i,1], obj_info[i,2], marker = 'o', s=50, c = '', edgecolors = c)
    
    
    x,y = convert_center_to_leftdown(1.3, 0, 0, 5.2, 2)
    ax.add_patch(plt.Rectangle((x, y), width = 5.2, height = 2, facecolor = 'none', edgecolor = 'b', angle = 0))
    ax.arrow(1.3, 0, 2*math.cos(0), 2*math.sin(0), width = 0.01, head_width = 0.2, color = 'black')
    

    print("ssssssssssssssssssss")
    yaw_init = -100
    x_init = -1
    y_init = -1
    target_index = 0
    target_info = []
    i_index = 0
    for d_index in range(len(sensor)):
        if sensor[d_index][0] < cur_timestamp - interval/2:
            continue
        if sensor[d_index][0] > cur_timestamp + interval/2:
            break
        while sensor[d_index][0] > info[i_index][0]:
            id = signal2value(info[i_index][1], obj_id_)
            i_index += 1
        obj_info_total = signal2value(sensor[d_index][1], "np/apps/ehy_obf_outputs.obf_objects".split('.'))

        for obj in obj_info_total:
            obj_id = getattr(getattr(obj, "fuseobj"), "id")
            if obj_id == id and int(id) != 0:
                pos_x = getattr(getattr(getattr(obj, "fuseobj"), "pos_vcs"),"x")
                pos_y = getattr(getattr(getattr(obj, "fuseobj"), "pos_vcs"),"y")
                obj_type = getattr(getattr(getattr(obj, "fuseobj"), "type"),"obj_main_class")
                obj_head = getattr(getattr(obj, "fuseobj"), "heading")
                target_info.append([obj_id, pos_x, pos_y, obj_type, obj_head, sensor[d_index][0]])

    for l_index in range(len(location)):
        if location[l_index][0] < cur_timestamp:
            continue
        yaw_init = signal2value(location[l_index][1], "common/localization/relative_localization.euler_angle.yaw".split('.'))
        x_init = signal2value(location[l_index][1], "common/localization/relative_localization.position.x".split('.'))
        y_init = signal2value(location[l_index][1], "common/localization/relative_localization.position.y".split('.'))
        break

    target_info = np.array(target_info)
    # print(target_info.shape)
    # print(len(location))
    for l_index in range(len(location)):
        if location[l_index][0] < cur_timestamp - interval/2:
            continue
        if location[l_index][0] > cur_timestamp + interval/2:
            break
        yaw = signal2value(location[l_index][1], "common/localization/relative_localization.euler_angle.yaw".split('.'))
        local_x = signal2value(location[l_index][1], "common/localization/relative_localization.position.x".split('.'))
        local_y = signal2value(location[l_index][1], "common/localization/relative_localization.position.y".split('.'))
        #print(local_x, local_y)
        dx = local_x - x_init
        dy = local_y - y_init
        ax.scatter(dx * math.cos(-yaw_init) - dy * math.sin(-yaw_init) + 0.6, 
                   dx * math.sin(-yaw_init) + dy * math.cos(-yaw_init), 
                   marker = 'o', s=5, c = '', edgecolors = 'b')
        
        while target_index < target_info.shape[0] and \
            target_info[target_index][5] >= location[l_index][0] \
            and target_info[target_index][5] < location[l_index+1][0]:

            target_pos_x = target_info[target_index][1]
            target_pos_y = -target_info[target_index][2]

            target_x = local_x + target_pos_x * math.cos(yaw) - target_pos_y * math.sin(yaw)
            target_y = local_y + target_pos_x * math.sin(yaw) + target_pos_y * math.cos(yaw)

            dx = target_x - x_init
            dy = target_y - y_init
            ax.scatter(dx * math.cos(-yaw_init) - dy * math.sin(-yaw_init), 
                    dx * math.sin(-yaw_init) + dy * math.cos(-yaw_init), 
                    marker = 'o', s=5, c = '', edgecolors = 'r')
            target_index += 1


    fig.savefig(ana_path + "/analysis.png")

 


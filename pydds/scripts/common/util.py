from distutils.version import StrictVersion
from google import protobuf
if StrictVersion(protobuf.__version__) < StrictVersion('3.9.6'):
    raise Exception("You must have protobuf > 3.9.6")

import sys,math,os, json
import numpy as np
from datetime import datetime
from google.protobuf.json_format import MessageToJson
from google.protobuf.message import DecodeError
from common import color
from color import info, info_all, warn, error
from common.bag import Bag

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
import math
import numpy as np
from datetime import datetime

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

    def FctDebugData(self, msg_fct_debug):
        res = {'t':[], 'r_t':[],'cnt':[]}
        first_timestamp = None
        for cell in msg_fct_debug:
            if first_timestamp == None:
                first_timestamp = cell[0]
                res['r_t'].append(0)
            else:
                res['r_t'].append(cell[0] / 1e9 - first_timestamp / 1e9)

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
        line['c0'] = float(-rme_line.c0) # sae -> iso
        line['c1'] = float(-rme_line.c1)
        line['c2'] = float(-rme_line.c2)
        line['c3'] = float(-rme_line.c3)
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
            frame = {'host_lane':{'left_line': None, 'right_line': None, 'lane_start':None, 'lane_end':None}}
            frame['host_lane']['left_line'] = self.RmeLine2Json(cell[1].host_lane.left_line)
            frame['host_lane']['right_line'] = self.RmeLine2Json(cell[1].host_lane.right_line)
            frame['host_lane']['lane_start'] = cell[1].host_lane.lane_start
            frame['host_lane']['lane_end'] = cell[1].host_lane.lane_end
            res['frame'].append(frame)
        return res
    
    def PlanningData(self, msg_fct_debug):
        res = {'t':[], 'cnt':[], 'frame':[]}
        trajectory_template = {'r_t':[], 'v':[], 'a':[], 'j':[], 's':[], 'x':[], 'y':[], 'theta':[], 'kappa':[], 'st_graph':[]}
        for msg in msg_fct_debug:
            cell = [msg[0], msg[1].fct_planning]
            res['t'].append(timestamp2str(cell[1].publish_ts / 1e9))
            res['cnt'].append(cell[1].counter)
            one_traj = {'stitching_size':None, 'is_replan':None, 'replan_reason':[],
                        'r_t':[], 'v':[], 'a':[], 'j':[], 's':[], 
                        'x':[], 'y':[], 'theta':[], 'kappa':[], 'st_graph':[],
                        'refline':[]
                        }
            for seg in cell[1].planning_debug.reference_line:
                refline_seg = {'c0': seg.y_coeff[0], 'c1': seg.y_coeff[1], 'c2': seg.y_coeff[2],
                               'c3': seg.y_coeff[3], 'lrange_start': seg.p_start,
                               'lrange_end': seg.p_end, 'poly_points': {'xs':[], 'ys':[]}}
                for x in np.arange(refline_seg['lrange_start'], refline_seg['lrange_end'], 1.0):
                    refline_seg['poly_points']['xs'].append(x)
                    y = refline_seg['c0'] + refline_seg['c1']*x + refline_seg['c2']*x*x + refline_seg['c3']*x*x*x
                    refline_seg['poly_points']['ys'].append(y)
                one_traj['refline'].append(refline_seg)
            for point in cell[1].trajectory_point:
                one_traj['r_t'].append(float(point.relative_time))
                one_traj['v'].append(float(point.v))
                one_traj['a'].append(float(point.a))
                one_traj['j'].append(float(point.da))
                one_traj['s'].append(float(point.path_point.s))
                if math.isnan(float(point.path_point.x)) == True:
                    print('x', cell[1].counter, point.path_point.x, math.isnan(float(point.path_point.x)))
                if math.isnan(float(point.path_point.y)) == True:
                    print('y', cell[1].counter, point.path_point.y, math.isnan(float(point.path_point.y)))
                if math.isnan(float(point.path_point.theta)) == True:
                    print('theta', cell[1].counter, point.path_point.theta, math.isnan(float(point.path_point.theta)))
                if math.isnan(float(point.path_point.kappa)) == True:
                    print('kappa', cell[1].counter, point.path_point.kappa, math.isnan(float(point.path_point.kappa)))
                one_traj['x'].append(float(point.path_point.x))
                one_traj['y'].append(float(point.path_point.y))
                one_traj['theta'].append(float(point.path_point.theta))
                # one_traj['kappa'].append(float(point.path_point.kappa))

            one_traj['stitching_size'] = int(cell[1].planning_debug.stitching_size)
            one_traj['is_replan'] = cell[1].is_replan
            one_traj['replan_reason'] = cell[1].planning_debug.replan_reason
            print(one_traj['replan_reason'])

            st_graph = {'id': None, 'boundary': {'id': None, 'ss':[], 'ts':[]}}
            # st_graph['id'] = str(cell[1].planning_debug.st_graph.id)
            for boundary in cell[1].planning_debug.st_graph.boundary:
                st_graph['boundary']['id'] = str(boundary.id)
                for spd_point in boundary.point:
                    st_graph['boundary']['ss'].append(spd_point.s)
                    st_graph['boundary']['ts'].append(spd_point.t)
            one_traj['st_graph'].append(st_graph)
            res['frame'].append(one_traj)
        return res
    
    def ControlData(self, msg_fct_debug):
        res = {'t':[], 'r_t':[], 'cnt':[], 'acc_cmd':[], 'acc_p':[],
               'acc_i':[], 'acc_d':[], 'acc_ff':[], 'acc_pitch':[],
                'station_pid_out':[], 'index_ref':[], 'time_error':[],
                'station_ref':[], 'station_cur': [], 'station_err':[],
                'station_err_flt':[]
                }
        first_timestamp = None
        for msg in msg_fct_debug:
            cell = [msg[0], msg[1].fct_control]
            res['t'].append(timestamp2str(cell[1].publish_ts / 1e9))
            if first_timestamp == None:
                first_timestamp = cell[0]
                res['r_t'].append(0)
            else:
                res['r_t'].append(float(cell[0] / 1e9 - first_timestamp / 1e9))

            res['cnt'].append(cell[1].counter)
            res['acc_cmd'].append(cell[1].lon_debug.acc_cmd)
            res['acc_p'].append(cell[1].lon_debug.acc_p)
            res['acc_i'].append(cell[1].lon_debug.acc_i)
            res['acc_d'].append(cell[1].lon_debug.acc_d)
            res['acc_ff'].append(cell[1].lon_debug.acc_ff)
            res['acc_pitch'].append(cell[1].lon_debug.acc_pitch)
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
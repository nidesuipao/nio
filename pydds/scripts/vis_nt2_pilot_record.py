import os, sys, argparse
parser = argparse.ArgumentParser(description = 'Nt2 PnC Visual Script')
parser.add_argument("-d", "--record_dir", help="record directory")
parser.add_argument("-s", "--start_t", help="start time, e: 120010")
parser.add_argument("-e", "--end_t", help="end time, e: 120050")

args = parser.parse_args()
cur_path = os.getcwd()
sys.path.append('./common')
sys.path.append('./conf')
sys.path.append('./')
sys.path.append(args.record_dir + '../bin')
sys.path.append(args.record_dir + '../bin/python')
sys.path.append(args.record_dir + '../bin/python/dds')
sys.path.append(args.record_dir + '../bin/python/messages')
os.environ['RECORD_ROOT_PATH'] = cur_path + '/' + args.record_dir

from google.protobuf import message
from google.protobuf import text_format, json_format

sys.path.append("../target/py_files")
from planning_msgs import planning_pb2
from control_msgs import control_data_pb2

sys.path.append('./common')
sys.path.append('./conf')
sys.path.append('./')
# from conf.visio_conf import dict_topic, dict_main_fig_set, \
#     layer_road_model_poly_line_set, layer_road_model_point_line_set, \
#     dict_sub_fig_set, layer_localization_car_set, dict_fct_out_fig_set, \
#     layer_fct_out_cursor_set, layer_planning_sl_obs_set, layer_planning_path_set, \
#     dict_planning_dynamic_fig_set, layer_planning_speed_set, layer_planning_acc_set, \
#     layer_planning_kappa_set, layer_planning_kappa_set, dict_planning_st_fig_set, \
#     layer_planning_stitch_path_set, layer_planning_stitch_kappa_set, layer_planning_stitch_speed_set, \
#     layer_planning_stitch_acc_set
from conf.visio_conf import *
from common.util import RecorcParser
from common.msg_parser import PbMsgParser, timestamp2str
from common import draw
from common.color import info, info_all, warn, error
from common.draw_base import CurveLayer, CircleLayer, \
    TextLabelLayer, MultiPolygonLayer, MultiLinesLayer, \
    PointsLayer, PointsLayerWithColors

import bokeh.plotting as bkp
from bokeh.models import Slider, Div, CustomJS, LabelSet, Select
from bokeh.plotting import ColumnDataSource, output_file
from bokeh.layouts import column, row
################################################################################################

record_parser = RecorcParser(dict_topic, 0, 1e18)
dict_pb_msg = record_parser.Parser(args.record_dir, parse_mode='pb_msg')
dict_aligned_index_of_dt = record_parser.SearchAndAlignedMsgIndexByFixedDt(0.02)

msg_parser = PbMsgParser(dict_topic)
relative_loc_data = msg_parser.RelativeLocalizationData(dict_pb_msg[dict_topic['relative_loc']])
ehy_tse_data = msg_parser.EhyTseData(dict_pb_msg[dict_topic['ehy_tse']])
ehy_rme_data = msg_parser.EhyRmeData(dict_pb_msg[dict_topic['ehy_rme']])

fct_debug_data = msg_parser.FctDebugData(dict_pb_msg[dict_topic['fct_debug_out']])
planning_data = msg_parser.PlanningData(dict_pb_msg[dict_topic['fct_debug_out']])
control_data = msg_parser.ControlData(dict_pb_msg[dict_topic['fct_debug_out']])

slider_end = len(dict_aligned_index_of_dt[dict_topic['ehy_tse']]) - 1
replay_slider = Slider(start=0, end=slider_end, value=1, step=1, title="aligned_index")
div = Div(width=400, height=800, height_policy="fixed")
control_data_select = Select(title="select control data key", value="acc_cmd", options=list(control_data.keys()))

main_fig = draw.GenTopViewFigsGroup(dict_main_fig_set)
dict_planning_st_fig = draw.GenPlanningStFigsGroup(dict_planning_st_fig_set, planning_data)
dict_planning_fig = draw.GenPlanningFigsGroupAtRelativeTime(dict_planning_dynamic_fig_set, planning_data)
dict_control_data_fig = draw.GenFctOutSignalFigsGroup(dict_fct_out_fig_set, control_data)

ehy_tse_layer = MultiPolygonLayer(main_fig, layer_localization_car_set)
ehy_rme_hl_line_layer = CurveLayer(main_fig, layer_road_model_poly_line_set)
ehy_rme_hr_line_layer = CurveLayer(main_fig, layer_road_model_poly_line_set)

refline_layer = CurveLayer(main_fig, layer_planning_path_set)
planning_path_layer = CurveLayer(main_fig, layer_planning_path_set)
planning_speed_layer = CurveLayer(dict_planning_fig['Planning: speed'], layer_planning_speed_set)
planning_acc_layer = CurveLayer(dict_planning_fig['Planning: acceleration'], layer_planning_acc_set)
planning_kappa_layer = CurveLayer(dict_planning_fig['Planning: kappa'], layer_planning_kappa_set)
planning_dkappa_layer = CurveLayer(dict_planning_fig['Planning: kappa rate'], layer_planning_kappa_set)

planning_stitch_path_layer = CurveLayer(main_fig, layer_planning_stitch_path_set)
planning_stitch_speed_layer = CurveLayer(dict_planning_fig['Planning: speed'], layer_planning_stitch_speed_set)
planning_stitch_acc_layer = CurveLayer(dict_planning_fig['Planning: acceleration'], layer_planning_stitch_acc_set)
planning_stitch_kappa_layer = CurveLayer(dict_planning_fig['Planning: kappa'], layer_planning_stitch_kappa_set)
planning_stitch_dkappa_layer = CurveLayer(dict_planning_fig['Planning: kappa rate'], layer_planning_stitch_kappa_set)

planning_station_layer = CurveLayer(dict_planning_st_fig['Planning ST'], layer_planning_speed_set)
planning_obs_st_boundary_layer = PointsLayer(dict_planning_st_fig['Planning ST'], layer_planning_sl_obs_set)
# planning_obs_st_boundary_layer.data_source.data['pts_xs'] = planning_data['frame'][0]['st_graph'][0]['boundary']['ts']
# planning_obs_st_boundary_layer.data_source.data['pts_ys'] = planning_data['frame'][0]['st_graph'][0]['boundary']['ss'] 
# planning_st_obs_name_layer = TextLabelLayer(dict_planning_st_fig['Planning ST'], layer_planing_label_set)
# planning_st_obs_type_layer = TextLabelLayer(dict_planning_st_fig['Planning ST'], layer_planing_label_set)

overview_fig = draw.GenTopViewFigsGroup(dict_sub_fig_set)
# dict_fct_out_fig = draw.GenFctOutSignalFigsGroup(dict_fct_out_fig_set, fct_out_data)
relative_loc_traj_layer = CurveLayer(overview_fig, layer_road_model_poly_line_set)
relative_loc_realtime_position_layer = CircleLayer(overview_fig, layer_road_model_poly_line_set)
relative_loc_traj_layer.data_source.data['pts_xs'] = relative_loc_data['rel_xs']
relative_loc_traj_layer.data_source.data['pts_ys'] = relative_loc_data['rel_ys']

variable_control_key_data_curve_layer = CurveLayer(dict_control_data_fig['control data: variable key data'], layer_planning_speed_set)
variable_control_key_data_points_layer = PointsLayer(dict_control_data_fig['control data: variable key data'], layer_planning_sl_obs_set)

arr_fct_out_cursor_layer = []
arr_fct_out_cursor_data_source = []
for fig in dict_control_data_fig.values():
    cursor = CurveLayer(fig, layer_fct_out_cursor_set)
    arr_fct_out_cursor_layer.append(cursor)
    arr_fct_out_cursor_data_source.append(cursor.data_source)

callback = CustomJS(args=dict(
    channel=dict_topic,
    aligned_index=dict_aligned_index_of_dt,
    rl_data = relative_loc_data,
    tse_data = ehy_tse_data,
    rme_data = ehy_rme_data,
    plan_data = planning_data,
    ctrl_data = control_data,

    rt_pos_DS = relative_loc_realtime_position_layer.data_source,
    tse_DS = ehy_tse_layer.data_source,
    rme_hl_DS = ehy_rme_hl_line_layer.data_source,
    rme_hr_DS = ehy_rme_hr_line_layer.data_source,

    refline_DS = refline_layer.data_source,

    plan_obs_stb_DS = planning_obs_st_boundary_layer.data_source,

    plan_path_DS = planning_path_layer.data_source,
    plan_s_DS = planning_station_layer.data_source,
    plan_v_DS = planning_speed_layer.data_source,
    plan_a_DS = planning_acc_layer.data_source,
    plan_k_DS = planning_kappa_layer.data_source,

    plan_stit_path_DS = planning_stitch_path_layer.data_source,
    plan_stit_v_DS = planning_stitch_speed_layer.data_source,
    plan_stit_a_DS = planning_stitch_acc_layer.data_source,
    # adc_DS = ad_car_layer.data_source
    arr_fct_cursor_DS = arr_fct_out_cursor_data_source
    ),
    code = """
    const step = cb_obj.value;
    const rme_index = aligned_index[channel['ehy_rme']][step][0];
    console.log(rme_index)
    const tse_index = aligned_index[channel['ehy_tse']][step][0];
    console.log(tse_index)
    const loc_index = aligned_index[channel['relative_loc']][step][0];
    // console.log(loc_index)
    const plan_index = aligned_index[channel['fct_debug_out']][step][0];
    // console.log(plan_index)
    const ctrl_index = aligned_index[channel['fct_debug_out']][step][0];

    rt_pos_DS.data['pts_xs'] = [rl_data['rel_xs'][loc_index]];
    rt_pos_DS.data['pts_ys'] = [rl_data['rel_ys'][loc_index]];
    rt_pos_DS.data['pts_rs'] = [0.5];
    rt_pos_DS.change.emit();

    var tse_obj_xs = [];
    var tse_obj_ys = [];
    for (var i = 0; i < tse_data['frame'][tse_index]['objs'].length; i++) {
        if (tse_data['frame'][tse_index]['objs'][i]['id'] > 0) {
            tse_obj_xs.push([[tse_data['frame'][tse_index]['objs'][i]['car_polygon']['xs']]]);
            tse_obj_ys.push([[tse_data['frame'][tse_index]['objs'][i]['car_polygon']['ys']]]);
        }
    }
    tse_DS.data['pts_xs'] = tse_obj_xs;
    tse_DS.data['pts_ys'] = tse_obj_ys;
    tse_DS.change.emit();

    rme_hl_DS.data['pts_xs'] = rme_data['frame'][rme_index]['host_lane']['left_line']['poly_points']['xs'];
    rme_hl_DS.data['pts_ys'] = rme_data['frame'][rme_index]['host_lane']['left_line']['poly_points']['ys'];
    console.log(rme_data['frame'][0]['host_lane']['left_line']['c0']);
    rme_hl_DS.change.emit();

    rme_hr_DS.data['pts_xs'] = rme_data['frame'][rme_index]['host_lane']['right_line']['poly_points']['xs'];
    rme_hr_DS.data['pts_ys'] = rme_data['frame'][rme_index]['host_lane']['right_line']['poly_points']['ys'];
    console.log(rme_data['frame'][0]['host_lane']['right_line']['c0']);
    rme_hr_DS.change.emit();

    if (plan_data['frame'][plan_index]['refline'].length > 0) {
        refline_DS.data['pts_xs'] = plan_data['frame'][plan_index]['refline'][0]['poly_points']['xs'];
        refline_DS.data['pts_ys'] = plan_data['frame'][plan_index]['refline'][0]['poly_points']['ys'];
        refline_DS.change.emit();
    }
    
    var obs_stb_ss = [];
    var obs_stb_ts = [];
    for (var i = 0; i < plan_data['frame'][plan_index]['st_graph'].length; i++) {
        obs_stb_ss.push([[ plan_data['frame'][plan_index]['st_graph'][i]['boundary']['ss'] ]]);
        obs_stb_ts.push([[ plan_data['frame'][plan_index]['st_graph'][i]['boundary']['ts'] ]]);
    }

    plan_obs_stb_DS.data['pts_xs'] = plan_data['frame'][plan_index]['st_graph'][0]['boundary']['ts'];
    plan_obs_stb_DS.data['pts_ys'] = plan_data['frame'][plan_index]['st_graph'][0]['boundary']['ss'];
    plan_obs_stb_DS.change.emit();

    plan_path_DS.data['pts_xs'] = plan_data['frame'][plan_index]['x'];
    plan_path_DS.data['pts_ys'] = plan_data['frame'][plan_index]['y'];
    plan_path_DS.change.emit();

    plan_s_DS.data['pts_xs'] = plan_data['frame'][plan_index]['r_t'];
    plan_s_DS.data['pts_ys'] = plan_data['frame'][plan_index]['s'];
    plan_s_DS.change.emit();

    plan_v_DS.data['pts_xs'] = plan_data['frame'][plan_index]['r_t'];
    plan_v_DS.data['pts_ys'] = plan_data['frame'][plan_index]['v'];
    plan_v_DS.change.emit();

    plan_a_DS.data['pts_xs'] = plan_data['frame'][plan_index]['r_t'];
    plan_a_DS.data['pts_ys'] = plan_data['frame'][plan_index]['a'];
    plan_a_DS.change.emit();

    plan_k_DS.data['pts_xs'] = plan_data['frame'][plan_index]['r_t'];
    plan_k_DS.data['pts_ys'] = plan_data['frame'][plan_index]['kappa'];
    plan_k_DS.change.emit();

    var stit_r_t = [];
    var stit_v = [];
    var stit_a = [];
    var stit_x = [];
    var stit_y = [];
    const stit_size = plan_data['frame'][plan_index]['stitching_size'];
    for (var i = 0; i < stit_size; i++) {
        stit_r_t.push(plan_data['frame'][plan_index]['r_t'][i]);
        stit_v.push(plan_data['frame'][plan_index]['v'][i]);
        stit_a.push(plan_data['frame'][plan_index]['a'][i]);
        stit_x.push(plan_data['frame'][plan_index]['x'][i]);
        stit_y.push(plan_data['frame'][plan_index]['y'][i]);
    }
    plan_stit_path_DS.data['pts_xs'] = stit_x;
    plan_stit_path_DS.data['pts_ys'] = stit_y;
    plan_stit_path_DS.change.emit();

    plan_stit_v_DS.data['pts_xs'] = stit_r_t;
    plan_stit_v_DS.data['pts_ys'] = stit_v;
    plan_stit_v_DS.change.emit();
    
    plan_stit_a_DS.data['pts_xs'] = stit_r_t;
    plan_stit_a_DS.data['pts_ys'] = stit_a;
    plan_stit_a_DS.change.emit();

    
    for (var i = 0; i < arr_fct_cursor_DS.length; i++) {
        arr_fct_cursor_DS[i].data['pts_xs'] = [ctrl_data['r_t'][ctrl_index], ctrl_data['r_t'][ctrl_index]];
        arr_fct_cursor_DS[i].data['pts_ys'] = [-1000, 1000];
        arr_fct_cursor_DS[i].change.emit();
    }
    """)

control_data_select_callback = CustomJS(args=dict(
        ctrl_data = control_data,
        var_ctrl_key_data_curve_DS = variable_control_key_data_curve_layer.data_source,
        var_ctrl_key_data_points_DS = variable_control_key_data_points_layer.data_source
        ),
        code = """
            const key = cb_obj.value;
            var_ctrl_key_data_curve_DS.data['pts_xs'] = ctrl_data['r_t'];
            var_ctrl_key_data_curve_DS.data['pts_ys'] = ctrl_data[key];
            var_ctrl_key_data_curve_DS.change.emit();

            var_ctrl_key_data_points_DS.data['pts_xs'] = ctrl_data['r_t'];
            var_ctrl_key_data_points_DS.data['pts_ys'] = ctrl_data[key];
            var_ctrl_key_data_points_DS.change.emit();
        """)

planning_outputs_str = ""
planning_outputs_str = planning_outputs_str.replace('\n', "<br>")
planning_outputs_str = planning_outputs_str.replace(' ', "&nbsp")

def display_event(div):
    "Build a suitable CustomJS to display the current event in the div model."
    return CustomJS(args=dict(div=div,
                              channel=dict_topic,
                              aligned_index=dict_aligned_index_of_dt,
                              tse_data=ehy_tse_data,
                              rme_data=ehy_rme_data,
                              loc_data=relative_loc_data,
                              plan_json = planning_outputs_str),
        code = """
            // const attrs = %s;
            // const args = [];
            // for (let i = 0; i<attrs.length; i++) {
            //     args.push(attrs[i] + '=' + Number(cb_obj[attrs[i]]).toFixed(2));
            // }
            const step = cb_obj.value;
            const rme_index = aligned_index[channel['ehy_rme']][step][0];

            const tse_index = aligned_index[channel['ehy_tse']][step][0];

            const loc_index = aligned_index[channel['relative_loc']][step][0];

            // const veh10_index = aligned_index[channel['veh_10ms']][step][0];

            // const veh50_index = aligned_index[channel['veh_50ms']][step][0];
            
            const rme_publish_ts = rme_data['t'][rme_index];
            const rme_counter = rme_data['cnt'][rme_index];

            const tse_publish_ts = tse_data['t'][tse_index];
            const tse_counter = tse_data['cnt'][tse_index];

            const loc_publish_ts = loc_data['t'][loc_index];
            const loc_counter = loc_data['cnt'][loc_index];

            // const veh10_publish_ts = loc_data['t'][veh10_index];
            // const veh10_counter = loc_data['cnt'][veh10_index];

            // const veh50_publish_ts = loc_data['t'][veh50_index];
            // const veh50_counter = loc_data['cnt'][veh50_index];

            const str1 = "ehy_tse publish time:" + tse_publish_ts + " counter:" + tse_counter + "<br>" + \
                         " ehy_rme publish time:" + rme_publish_ts + " counter:" + rme_counter + "<br>" + \
                         " relative_loc publish time:" + loc_publish_ts + " counter:" + loc_counter + "<br>" \
                         //+ " veh_10ms publish time:" + veh10_publish_ts + " counter:" + veh10_counter + "<br>" \
                         //+ " veh_50ms publish time:" + veh50_publish_ts + " counter:" + veh50_counter;

            // const str2 = aligned_index[channel['ehy_tse']][step][1] + "\\n" + aligned_index[channel['ehy_rme']][step][1] + "\\n" + aligned_index[channel['relative_loc']][step][1];
            div.text = str1;
        """)

control_data_select.js_on_change('value', control_data_select_callback)
replay_slider.js_on_change('value', callback, display_event(div))

main_fig.legend.click_policy="hide"
html_name = args.record_dir + 'pnc.html'
output_file(html_name)
bkp.show(row(
    column(row(dict_planning_st_fig['Planning ST']),
           row(dict_planning_fig['Planning: speed'], dict_planning_fig['Planning: acceleration']), 
           row(dict_planning_fig['Planning: kappa'])),

    column(control_data_select, dict_control_data_fig['control data: variable key data'], main_fig, replay_slider),
    column(row(dict_control_data_fig['control data: lon acc cmd'])),
    column(div)
    
    )
)
from __future__ import print_function
import sys, os, argparse, threading, json
parser = argparse.ArgumentParser(description = 'Debug Fct Script')
parser.add_argument("-d", "--record_dir", default = '/home/nio/Videos/20230331T190552.SOC1/record', help="record directory")
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
# os.environ['DDS_DEBUG'] = 'on'
# from dds.bag import Bag
from conf.visio_conf import dict_topic, dict_main_fig_set, \
    layer_road_model_poly_line_set, layer_road_model_point_line_set, \
    dict_sub_fig_set, layer_localization_car_set, dict_fct_out_fig_set, layer_fct_out_cursor_set, layer_planning_sl_obs_set
from common.util import RecorcParser, PbMsgParser
from common import draw
from common.draw_base import CurveLayer, CircleLayer, \
    TextLabelLayer, MultiPolygonLayer, MultiLinesLayer

import bokeh.plotting as bkp
from bokeh.models import Slider, Div, CustomJS, LabelSet
from bokeh.plotting import ColumnDataSource, output_file
from bokeh.layouts import column, row

if args.start_t == None or args.end_t == None:
    args.start_t = -1
    args.end_t = 1e20

record_parser = RecorcParser(dict_topic, args.start_t, args.end_t)
msg_parser = PbMsgParser(dict_topic)

dict_pb_msg = record_parser.Parser(args.record_dir, 'pb_msg')
dict_aligned_index_of_dt = record_parser.SearchAndAlignedMsgIndexByFixedDt(0.02)
# f = open("../data/50HZ_index.txt", "w")
# f.write(json.dumps(dict_aligned_index_of_dt, indent=1))
# f.close()

relative_loc_data = msg_parser.RelativeLocalizationData(dict_pb_msg[dict_topic['relative_loc']])
fct_out_data = msg_parser.FctData(dict_pb_msg[dict_topic['fct_out']])
ehy_tse_data = msg_parser.EhyTseData(dict_pb_msg[dict_topic['ehy_tse']])
ehy_rme_data = msg_parser.EhyRmeData(dict_pb_msg[dict_topic['ehy_rme']])
veh_10ms_data = msg_parser.Veh10msData(dict_pb_msg[dict_topic['veh_10ms']])
veh_50ms_data = msg_parser.Veh10msData(dict_pb_msg[dict_topic['veh_50ms']])
# veh_10ms_json_data = dict_json_msg[dict_topic['veh_10ms']]

max_index = len(dict_aligned_index_of_dt[dict_topic['ehy_tse']]) - 1
replay_slider = Slider(start=0, end=max_index, value=0, step=1, title="index")
div = Div(width=600, height=800, height_policy="fixed")

main_fig = draw.GenTopViewFigsGroup(dict_main_fig_set)
ehy_tse_layer = MultiPolygonLayer(main_fig, layer_localization_car_set)
ehy_rme_hl_line_layer = CurveLayer(main_fig, layer_road_model_poly_line_set)
ehy_rme_hr_line_layer = CurveLayer(main_fig, layer_road_model_poly_line_set)

overview_fig = draw.GenTopViewFigsGroup(dict_sub_fig_set)
# dict_fct_out_fig = draw.GenFctOutSignalFigsGroup(dict_fct_out_fig_set, fct_out_data)

relative_loc_traj_layer = CurveLayer(overview_fig, layer_road_model_poly_line_set)
relative_loc_realtime_position_layer = CircleLayer(overview_fig, layer_road_model_poly_line_set)
relative_loc_traj_layer.data_source.data['pts_xs'] = relative_loc_data['rel_xs']
relative_loc_traj_layer.data_source.data['pts_ys'] = relative_loc_data['rel_ys']

# arr_fct_out_cursor_layer = []
# arr_fct_out_cursor_data_source = []
# for fig in dict_fct_out_fig.values():
#     cursor = CurveLayer(fig, layer_fct_out_cursor_set)
#     arr_fct_out_cursor_layer.append(cursor)
#     arr_fct_out_cursor_data_source.append(cursor.data_source)

callback = CustomJS(args=dict(
    channel=dict_topic,
    aligned_index=dict_aligned_index_of_dt,
    tse_data = ehy_tse_data,
    rme_data = ehy_rme_data,
    rl_data = relative_loc_data,
    fct_data = fct_out_data,

    tse_DS = ehy_tse_layer.data_source,
    rme_hl_DS = ehy_rme_hl_line_layer.data_source,
    rme_hr_DS = ehy_rme_hr_line_layer.data_source,
    rt_pos_DS = relative_loc_realtime_position_layer.data_source
    # adc_DS = ad_car_layer.data_source
    # arr_fct_cursor_DS = arr_fct_out_cursor_data_source
    ),
    code = """
    const step = cb_obj.value;
    const rme_index = aligned_index[channel['ehy_rme']][step][0];

    const tse_index = aligned_index[channel['ehy_tse']][step][0];

    const loc_index = aligned_index[channel['relative_loc']][step][0];

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
    rme_hl_DS.change.emit();

    rme_hr_DS.data['pts_xs'] = rme_data['frame'][rme_index]['host_lane']['right_line']['poly_points']['xs'];
    rme_hr_DS.data['pts_ys'] = rme_data['frame'][rme_index]['host_lane']['right_line']['poly_points']['ys'];
    rme_hr_DS.change.emit();

    rt_pos_DS.data['pts_xs'] = [rl_data['rel_xs'][loc_index]];
    rt_pos_DS.data['pts_ys'] = [rl_data['rel_ys'][loc_index]];
    rt_pos_DS.data['pts_rs'] = [0.5];
    rt_pos_DS.change.emit();
    """)
def display_event(div):
    "Build a suitable CustomJS to display the current event in the div model."
    return CustomJS(args=dict(div=div,
                              channel=dict_topic,
                              aligned_index=dict_aligned_index_of_dt,
                              tse_data=ehy_tse_data,
                              rme_data=ehy_rme_data,
                              loc_data=relative_loc_data,
                              veh10_data=veh_10ms_data,
                              veh50_data=veh_50ms_data),
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

            const veh10_index = aligned_index[channel['veh_10ms']][step][0];

            const veh50_index = aligned_index[channel['veh_50ms']][step][0];
            
            const rme_publish_ts = rme_data['t'][rme_index];
            const rme_counter = rme_data['cnt'][rme_index];

            const tse_publish_ts = tse_data['t'][tse_index];
            const tse_counter = tse_data['cnt'][tse_index];

            const loc_publish_ts = loc_data['t'][loc_index];
            const loc_counter = loc_data['cnt'][loc_index];

            const veh10_publish_ts = loc_data['t'][veh10_index];
            const veh10_counter = loc_data['cnt'][veh10_index];

            const veh50_publish_ts = loc_data['t'][veh50_index];
            const veh50_counter = loc_data['cnt'][veh50_index];

            const str1 = "ehy_tse publish time:" + tse_publish_ts + " counter:" + tse_counter + "<br>" + \
                         " ehy_rme publish time:" + rme_publish_ts + " counter:" + rme_counter + "<br>" + \
                         " relative_loc publish time:" + loc_publish_ts + "counter:" + loc_counter + "<br>" + \
                         " veh_10ms publish time:" + veh10_publish_ts + "counter:" + veh10_counter + "<br>" + \
                         " veh_50ms publish time:" + veh50_publish_ts + "counter:" + veh50_counter;

            // const str2 = aligned_index[channel['ehy_tse']][step][1] + "\\n" + aligned_index[channel['ehy_rme']][step][1] + "\\n" + aligned_index[channel['relative_loc']][step][1];
            div.text = str1;
        """)

replay_slider.js_on_change('value', callback, display_event(div))

main_fig.legend.click_policy="hide"
html_name = args.record_dir.split('/')[-2] + '.html'
output_file(html_name)
bkp.show(row(column(div), column(main_fig, replay_slider), column(overview_fig)))
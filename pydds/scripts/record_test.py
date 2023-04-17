from __future__ import print_function
import sys, os, argparse

parser = argparse.ArgumentParser(description = 'PnC Visual Script')
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
os.environ['RECORD_ROOT_PATH'] = args.record_dir
# os.environ['DDS_DEBUG'] = 'on'
# from dds.bag import Bag
from conf.visio_conf import dict_topic, dict_main_fig_set, \
    layer_road_model_poly_line_set, layer_road_model_point_line_set, \
    dict_sub_fig_set, layer_localization_car_set, dict_fct_out_fig_set, layer_fct_out_cursor_set
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
x = record_parser.Parser(args.record_dir, "pb_msg")
y = "np/debug/dgb_aeb_strtg.rqabInfo.fcwReq"
y = y.split('.')
xx = getattr(x['np/debug/dgb_aeb_strtg'][0][1], 'rqabInfo', None)
xxx = getattr(xx, 'fcwReq', None)
print(xxx)

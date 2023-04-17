from __future__ import print_function
import sys, os, argparse, json, threading
parser = argparse.ArgumentParser(description = 'Debug Fct Script')
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
# os.environ['DDS_DEBUG'] = 'on'
# from dds.bag import Bag
from conf.visio_conf import dict_topic
from common.util import RecorcParser, PbMsgParser

if args.start_t == None or args.end_t == None:
    args.start_t = -1
    args.end_t = 1e20

record_parser = RecorcParser(dict_topic, args.start_t, args.end_t)
msg_parser = PbMsgParser(dict_topic)

f = open("../data/50HZ_index.txt", "r")
_50hz_index_str = f.read()
dict_aligned_index_of_dt = json.loads(_50hz_index_str)
dict_frame_count={}
for key in dict_aligned_index_of_dt.keys():
    dict_frame_count[key] = []

for key in dict_frame_count.keys():
    for i in range(len(dict_aligned_index_of_dt[key])):
        if i >= 11790 and i <= 12671:
            dict_frame_count[key].append(dict_aligned_index_of_dt[key][i][2]) # 2 mean counter

f = open("../data/scene_test/follow_scene/aligned_index_50hz.txt", "w")
f.write(json.dumps(dict_frame_count, indent=1))
f.close()
dict_json_msg = record_parser.FindToJson(args.record_dir, dict_frame_count)

for topic in dict_json_msg.keys():
    dir_name = "../data/scene_test/follow_scene/" + topic.split('/')[-1]
    if not os.path.exists(dir_name):
        os.mkdir(dir_name)
    for msg in dict_json_msg[topic]:
        counter = msg[0]
        file_name = dir_name + "/" + topic.split('/')[-1] + "_counter_" + str(counter) + ".txt"
        print(file_name)
        f = open(file_name, "w")
        f.write(msg[1])
        f.close()

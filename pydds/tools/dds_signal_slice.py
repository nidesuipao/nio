import os
dds_dir=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
python_root=os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import sys
inputs=sys.argv[1::]
#inputs = ["/home/nio/Videos/20230331T190552.SOC1", "np/debug/dgb_aeb_strtg.rqabInfo.fcwReq", 10000000000]
# print(inputs)
try:
    dir_path=inputs[0]
    signal=inputs[1]
    interval=int(inputs[2]) * 1000000000
    is_see_video = inputs[3] == "True"
except Exception as e:
    print(e)
    raise("Usage: python3 dds_signal_slice.py record_dir target_time(ns) interval(ns)")
    
sys.path.append(dds_dir)
sys.path.append(python_root)
sys.path.append(os.path.join(dir_path, "bin/python/messages"))
os.environ['DIR_PATH'] = os.path.join(dir_path)
os.environ['DDS_MESSAGES'] = os.path.join(dir_path, "bin/python/messages")

from util import RecorcParser
from util import video_cut
from util import analysis
# from visio_conf import dict_topic
from pydds.bag import Bag

signal = signal.split('.')
dict_topic = {"1":signal[0], 
	      "2":"np/apps/ehy_obf_outputs",
		  "3":"common/localization/relative_localization"}
record_parser = RecorcParser(dict_topic, -1, 1e20)
record_path = os.path.join(dir_path, '_record')
info = record_parser.Parser(record_path, "pb_msg")
sensor = info["np/apps/ehy_obf_outputs"]
location = info["common/localization/relative_localization"]
info = info[signal[0]]
last_signal = False
signal_change_times = []
video_dir = os.path.join(dir_path, '_camera')
date = dir_path.split('/')[-1].split('.')[0]

if not os.path.exists(os.path.join(record_path, "slice_interval_record")):
	os.mkdir(os.path.join(record_path, "slice_interval_record"))

for t in range(len(info)):
	timestamp = info[t][0]
	info_ = info[t][1]
	for i in range(1, len(signal)):
		info_ = getattr(info_, signal[i], None)
	if t == 0:
		last_signal = info_
	if last_signal != info_:
		last_signal = info_
		if info_== True:
			ana_path = os.path.join(record_path, "slice_interval_record", date+"-"+str(timestamp))
			if not os.path.exists(ana_path):
				os.mkdir(ana_path)
			analysis(info, t, ana_path, signal, sensor, location, interval)
			signal_change_times.append(timestamp)

#print(_max, _min)


if len(signal_change_times) == 0:
	exit(0)

import math
from datetime import datetime
def timestamp2str(timestamp):
    
    b1 = math.modf(timestamp)[1]
    b0 = math.modf(timestamp)[0]
    time_str = datetime.strftime(datetime.fromtimestamp(b1), '%Y-%m-%d %H:%M:%S') \
                + '.' + str(b0).split('.')[1][0:4]
    return time_str

#print(timestamp2str(int(signal_change_times[0])/1e9))
cur_file_index = 0

#t_list = []
for path in os.listdir(record_path):
	if '.dat' not in path:
			continue
	try:
		bag=Bag(os.path.join(record_path, path))
	except:
		continue

	file_list = []
	for cur_timestamp_index in range(len(signal_change_times)):
		cur_timestamp_path = os.path.join(record_path, "slice_interval_record/", \
			date + '-' + str(signal_change_times[cur_timestamp_index]))
		if not os.path.exists(cur_timestamp_path):
			os.mkdir(cur_timestamp_path)
		cur_timestamp_record = cur_timestamp_path + "/record"
		if not os.path.exists(cur_timestamp_record):
			os.mkdir(cur_timestamp_record)
		file_list.append(open(cur_timestamp_record+"/"+os.path.basename(path),'wb'))
	is_write = False
	while not bag.eof:
		msg, fsize, recv_ts, send_ts, recv_ts_ptp, send_ts_ptp = bag.read()
		# if msg:
			#print(bag.current_timestamp)  #1674035234512244544 1674033774051664864
#[1674034489113713696, 1674034590573193632, 1674034786573072448, 1674034990573995904]

			#t_list.append(bag.current_timestamp)
		for f_index in range(len(signal_change_times)):
			start_t = signal_change_times[f_index] - interval/2
			end_t = signal_change_times[f_index] + interval/2
			if bag.current_timestamp>=start_t and bag.current_timestamp<=end_t:
				file_list[f_index].write(recv_ts_ptp.to_bytes(8,"little"))
				file_list[f_index].write(send_ts_ptp.to_bytes(8,"little"))
				file_list[f_index].write(recv_ts.to_bytes(8,"little"))
				file_list[f_index].write(send_ts.to_bytes(8,"little"))
				file_list[f_index].write(fsize.to_bytes(8,"little"))
				file_list[f_index].write(msg.SerializeToString())
		# else:
		# 	print(msg, fsize, recv_ts, send_ts, recv_ts_ptp, send_ts_ptp)
	for f in file_list:
		f.close()
		
if is_see_video:
	out_record_path = os.path.join(record_path, "slice_interval_record/")	
	video_c = video_cut(video_dir, out_record_path, signal_change_times, interval, date)
	video_c.handle_video()

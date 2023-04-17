import os
dds_dir=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
python_root=os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import sys
sys.path.append(dds_dir)
sys.path.append(python_root)
sys.path.append(os.path.join(python_root, "messages"))
from pydds.bag import Bag
inputs=sys.argv[1::]
try:
    dir_path=inputs[0]
    target_time=int(inputs[1])
    interval=int(inputs[2])
except Exception as e:
    print(e)
    raise("Usage: python3 dds_cut.py record_dir target_time(ns) interval(ns)")



start_t = target_time - interval/2
end_t = target_time + interval/2

if not os.path.exists(os.path.join(dir_path, "slice_interval_record")):
	os.mkdir(os.path.join(dir_path, "slice_interval_record"))
print(dir_path)
for path in os.listdir(dir_path):
	if '.dat' not in path:
		continue
	print(path)
	try:
		bag=Bag(os.path.join(dir_path, path))
	except:
		continue
	# f=open(dir_path+"/slice_record/"+str(start_t)+"_"+str(end_t)+"-"+os.path.basename(path),'wb+')
	f=open(dir_path+"/slice_interval_record/"+os.path.basename(path),'wb+')

	while True:
		msg, fsize, recv_ts, send_ts, recv_ts_ptp, send_ts_ptp = bag.read()
		if msg:
			if bag.current_timestamp>=start_t and bag.current_timestamp<=end_t:
				f.write(recv_ts_ptp.to_bytes(8,"little"))
				f.write(send_ts_ptp.to_bytes(8,"little"))
				f.write(recv_ts.to_bytes(8,"little"))
				f.write(send_ts.to_bytes(8,"little"))
				f.write(fsize.to_bytes(8,"little"))
				f.write(msg.SerializeToString())
				#print(bag.current_timestamp)
		else:
			break

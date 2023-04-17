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
    path=inputs[0]
    start_t=int(inputs[1])
    end_t=int(inputs[2])
except Exception as e:
    print(e)
    raise("Usage: python3 dds_cut.py XX.pb.dat start_timestamp(ns) end_timestamp(ns)")
bag=Bag(path)
f=open(os.path.basename(path)+"-"+str(start_t)+"_"+str(end_t),'wb')
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
    else:
        break

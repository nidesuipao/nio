import os
python_root=os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import sys 
sys.path.append(python_root)
from pydds.bag import Bag 

def bag_list(path):
    try:
        bag=Bag(path,True)
    except Exception as e:
        print(e)
        return
    pre_pub_t=-1
    pre_sub_t=-1
    pre_counter=-1
    count=0
    while True:
        msg, size, sub_t, pub_t, sub_t_ptp, pub_t_ptp=bag.read()
        if msg:
            if msg.publish_ts<pre_pub_t:
                print("%-6s" % count,
                    "pre_counter:%5s" % pre_counter,
                    "counter:%5s" % msg.counter,
                    "diff:%4s" % (pre_pub_t-msg.publish_ts),
                    "pre_pub:",pre_pub_t,
                    "pub:",msg.publish_ts,
                    "pre_trip:%10s" % (pre_sub_t-pre_pub_t),
                    "trip:%10s" % (sub_t-msg.publish_ts))
            pre_pub_t=msg.publish_ts
            pre_sub_t=sub_t
            pre_counter=msg.counter
            count+=1
        else:
            break
try:
    bag_list(sys.argv[1])
except Exception as e:
    print(e)
    print("Usage: python3 dds_list.py XX.pb.dat")

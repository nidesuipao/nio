import os
python_root=os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import sys 
sys.path.append(python_root)
from pydds.bag import Bag 

def bag_list(path):
    try:
        bag=Bag(path)
    except Exception as e:
        print(e)
        return
    pre_pub_t=-1
    pre_sub_t=-1
    tms_plus_count=0
    ttms_plus_count=0
    tttms_plus_count=0
    count=0
    trip=0
    while True:
        msg, size, sub_t, pub_t, sub_t_ptp, pub_t_ptp = bag.read()
        if msg:
            trip=sub_t-pub_t
            print("%-6s" % count,
                    "counter:%5s" % msg.counter,
                    "size:%4s" % size,
                    "pub:",pub_t,
                    "(%5.1f" % ((pub_t-pre_pub_t)/1e6 if pre_pub_t>0 else 0),"ms)",
                    "sub:",sub_t,
                    "(%5.1f" % ((sub_t-pre_sub_t)/1e6 if pre_sub_t>0 else 0),"ms)",
                    "trip:%10s" % trip,
                    bag.topic,bag.messagetype.__name__)
            pre_pub_t=pub_t
            pre_sub_t=sub_t
            count+=1

            if trip>=1000000:
                tms_plus_count+=1

            if trip>=10000000:
                ttms_plus_count+=1

            if trip>=100000000:
                tttms_plus_count+=1

            print("1ms: %-6s" % tms_plus_count, "10ms: %-6s" % ttms_plus_count, "100ms: %-6s" % tttms_plus_count)

        else:
            break
try:
    bag_list(sys.argv[1])
except Exception as e:
    print(e)
    print("Usage: python3 dds_list.py XX.pb.dat")

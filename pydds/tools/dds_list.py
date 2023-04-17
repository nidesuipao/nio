import os
python_root=os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import sys 
sys.path.append(python_root)
sys.path.append(os.path.join(python_root, "messages"))
from pydds.bag import Bag 

def bag_list(path):
    try:
        bag=Bag(path)
    except Exception as e:
        print(e)
        return
    pre_pub_t=-1
    pre_sub_t=-1
    count=0
    while True:
        msg,size,sub_t,pub_t=bag.read()
        if msg:
            print("%-6s" % count,
                    "counter:%5s" % msg.counter,
                    "size:%4s" % size,
                    "pub:",pub_t,
                    "(%5.1f" % ((pub_t-pre_pub_t)/1e6 if pre_pub_t>0 else 0),"ms)",
                    "sub:",sub_t,
                    "(%5.1f" % ((sub_t-pre_sub_t)/1e6 if pre_sub_t>0 else 0),"ms)",
                    "trip:%10s" % (sub_t-pub_t),
                    bag.topic,bag.messagetype.__name__)
            pre_pub_t=pub_t
            pre_sub_t=sub_t
            count+=1
        else:
            break
try:
    bag_list(sys.argv[1])
except Exception as e:
    print(e)
    print("Usage: python3 dds_list.py XX.pb.dat")


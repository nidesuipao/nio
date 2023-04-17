import os
python_root=os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import sys
sys.path.append(python_root)
sys.path.append(os.path.join(python_root, "messages"))
from pydds.bag import Bag
try:
    bag=Bag(sys.argv[1])
except Exception as e:
    print(e)
    print("Usage: python3 dds_count.py XX.pb.dat")
    exit(1)
prv_counter=-1
while True:
    msg,*_=bag.read()
    if msg:
        if prv_counter>0 and msg.counter-prv_counter!=1:
            print("frame lost: previous counter",prv_counter,"next counter",msg.counter)
        prv_counter=msg.counter
    else:
        break

bag.close()

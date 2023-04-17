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
    print("Usage: python3 dds_print.py XX.pb.dat [>a.txt], `a.txt` is optional")
    exit(1)
while True:
    msg,*_=bag.read()
    if msg:
        print(msg)
    else:
        break

bag.close()

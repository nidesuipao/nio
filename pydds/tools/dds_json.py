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
    print("Usage: python3 dds_json.py XX.pb.dat [>a.json], `a.json` is optional")
    exit(0)
print("[")
msg=bag.read_as_json()
print(msg)
while True:
    msg=bag.read_as_json()
    if msg:
        print(",")
        print(msg)
    else:
        break
print("]")
bag.close()

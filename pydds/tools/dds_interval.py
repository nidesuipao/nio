import os
python_root=os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import sys
sys.path.append(python_root)
sys.path.append(os.path.join(python_root, "messages"))
from pydds.bag import Bag
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')
bag=Bag(sys.argv[1])
pub_intervals=[]
pub_sub_intervals=[]
pt=-1
while True:
    msg, size, sub_t, pub_t, sub_t_ptp, pub_t_ptp = bag.read()
    if msg:
        if bag.current_timestamp>0:
            pub_sub_intervals.append((sub_t-pub_t)/1e6)
        if pt>0:
            pub_t_interval=(pub_t-pt)/1e6
            pub_intervals.append(pub_t_interval)
        pt=pub_t
    else:
        break
plt.scatter(x=range(len(pub_intervals)),y=pub_intervals,label="publish interval",s=2)
plt.scatter(x=range(len(pub_sub_intervals)),y=pub_sub_intervals,label="publish record interval",s=2)
plt.xlabel("frame index")
plt.ylabel("interval time/ms")
plt.legend()
plt.grid()
plt.show()

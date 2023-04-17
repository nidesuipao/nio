import os
python_root=os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
print(python_root)
import sys
sys.path.append(python_root)
sys.path.append(os.path.join(python_root, "messages"))
from pydds.bag import Bag
from datetime import datetime
from glob import glob

def bag_info(path):
    try:
        bag=Bag(path)
    except Exception as e:
        print(e)
        return
    messages=0
    start_time=-1
    end_time=-1
    size=0
    while True:
        msg,*_=bag.read()
        if msg:
            if messages == 0:
                start_time=bag.current_timestamp
            messages+=1
            size+=16+bag.current_frame_size
        else:
            end_time=bag.current_timestamp
            break
    duration=(end_time-start_time)/1e9
    frequency=messages/duration if duration else 0
    start_time_date=datetime.fromtimestamp(start_time/1e9)
    end_time_date=datetime.fromtimestamp(end_time/1e9)
    info={
            "path":path,
            "topic":bag.topic,
            "type":bag.messagetype,
            "messages":messages,
            "frequency (Hz)":frequency,
            "duration (seconds)":duration,
            "start time (nanoseconds)":str(start_time)+" "+str(start_time_date),
            "end time (nanoseconds)":str(end_time)+" "+str(end_time_date),
            "size (KB)":size/1024,
            }
    print("\033[44m                                summary                               \033[0m")
    for key,value in info.items():
        print("%-24s" % key,value)

inputs=sys.argv[1::]
paths=[]
for i in inputs:
    if os.path.isfile(i):
        paths.append(i)
    else:
        raise("Please input file paths, not directories or others, you can use * to filter files like `*/vehicle*.pb.dat")
if not paths:
    paths=glob("*.pb.dat")
for path in paths:
    bag_info(path)

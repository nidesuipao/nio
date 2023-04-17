import os
python_root=os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import sys
sys.path.append(python_root)
sys.path.append(os.path.join(python_root, "messages"))
from pydds.bag import Bag
import websocket
args=sys.argv[1::]
paths=[]
server="127.0.0.1:9871"
for i,arg in enumerate(args):
    if arg=="-s":
        server=args[i+1]
    elif os.path.isfile(arg):
        paths.append(arg)
if not paths:
    print("Please input path of a record file")
    exit(0)

ws=websocket.WebSocket()
try:
    ws.connect("ws://"+server)
except:
    print("Server not established at",server)
    ws.close()
    exit(0)
for path in paths:
    bag=Bag(path)
    print("Sending",path)
    while True:
        buf=bag.read_as_plot_json()
        if buf:
            ws.send(buf)
        else:
            break
    bag.close()
    print("\033[1A\033[K\033[32m\r√",path,"\033[0m"); # back to up row, clean and print
ws.close()

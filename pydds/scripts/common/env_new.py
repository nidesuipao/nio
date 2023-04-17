import inspect
import sys
import glob
import os
import json

# DDS DEBUG PRINT
PYDDS_PATH = os.path.dirname(__file__)

def ddprint(args):
    if os.environ.get("DDS_DEBUG"):
        print(args)


class Environment:
    def __init__(self):
        with open(f"{PYDDS_PATH}/topics.json", 'r') as json_file:
            self.topic_messagetype_map = json.load(json_file)
            self.messagetype_map={}

    def import_proto_type(self,path):
        ss = path.split("/messages/")
        if ss[0] not in sys.path:
            ddprint("### append path: " + ss[0])
            sys.path.append(ss[0])
        module_string="messages."+ss[1].replace("/",".").replace(".py","")
        __import__(module_string)
        module=sys.modules[module_string]
        messagetype_pairs=inspect.getmembers(module,inspect.isclass)

        ddprint("=== found {} message types.".format(len(messagetype_pairs)) )
        for pair in messagetype_pairs:
            messagetype_name=module_string+"."+pair[0]
            self.messagetype_map[messagetype_name]=pair[1]
            ddprint("--- {} : {}".format(messagetype_name, pair[1]))

    def messagetype(self,topic):
        try:
            ddprint("### topic=" + topic)
            msg=self.topic_messagetype_map[topic]
            ddprint("### msg=" + msg)
            msg_type=self.messagetype_map[msg]
            ddprint("### type=")
            ddprint(msg_type)
            return msg_type 
        except:
            raise Exception("No message found for " + topic)

    def find_messages(self):
        original_dir=os.getcwd()
        for i in range(4):
            cur_dir=os.getcwd()
            if cur_dir == "/":
                dirs=glob.glob("/python/messages/**/*pb2.py", recursive=True)
            else:
                dirs=glob.glob(f"{PYDDS_PATH}/../messages/**/*pb2.py", recursive=True)
            ddprint("### search message in " + cur_dir)
            if dirs:
                ddprint("### found " + cur_dir)
                break
            else:
                os.chdir("..")

        os.chdir(original_dir)
        if dirs:
            for d in dirs:
                self.import_proto_type(d)
            return True
        else:
            ddprint("### No python proto type files were found")
            return False


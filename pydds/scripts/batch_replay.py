import sys, os, argparse
sys.path.append('../target')
import nt2_pilot_debug

parser = argparse.ArgumentParser(description = 'PnC Visual Script')
parser.add_argument("-d", "--record_dir", help="record directory")
args = parser.parse_args()

sys.path.append('./common')
sys.path.append(args.record_dir + '../bin')
sys.path.append(args.record_dir + '../bin/python')
sys.path.append(args.record_dir + '../bin/python/dds')
sys.path.append(args.record_dir + '../bin/python/messages')

cur_path = os.getcwd()
os.environ['RECORD_ROOT_PATH'] = cur_path + '/' + args.record_dir

from common.bag import Bag
bag = Bag(args.record_dir + '/common-vehicle_in-vehicle_10ms.pb.dat')
while not bag.eof:
    msg_c, size_c, sub_t_c, pub_t_c, sub_t_ptp_c, pub_t_ptp_c = bag.read_raw()
    nt2_pilot_debug.ExeutePilotTask(msg_c)
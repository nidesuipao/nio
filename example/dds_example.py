import sys,os
root=os.path.abspath(__file__+'/../..')
print("root="+root)
sys.path.insert(0, root)

from dds.bag import Bag

if len(sys.argv)<2:
    record_path = '../../../record/'
else:
    record_path=sys.argv[1]


#%%
for f in os.listdir(record_path):
    data_file=os.path.join(record_path, f)    
    print("======================================================")
    print("### Read 1st frame from " + data_file)
    print("======================================================")
    
    bag=Bag(data_file)
    msg=bag.read()
    print(msg)
    bag.close()

    print(" ")
    print(" ")
    print(" ")

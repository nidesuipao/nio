import os


SOC_path = "/home/nio/Videos"
signal = "np/debug/dgb_aeb_strtg.rqabInfo.fcwReq"
slice_time = "10"
is_video = str(True)

bash_cmd = "bash ./pydds/split.sh"


for root,dirs,files in os.walk(SOC_path):
	for d in dirs:
		if "SOC" in d:
			SOC_path = os.path.join(root, d)
			os.system(bash_cmd + " " + SOC_path
	     + " " +signal \
	     + " " +slice_time \
	     + " " +is_video
			)
	

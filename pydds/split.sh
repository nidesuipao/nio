#!/bin/sh　
echo "第一个参数为：$1";
echo "第二个参数为：$2";
echo "第三个参数为：$3";
echo "第三个参数为：$4";

if [ ! -d "$1/_record" ];then
    mv -T $1/record $1/_record 
    mkdir $1/record
else
    echo "_record文件夹已经存在"
fi

if [ ! -d "$1/_camera" ];then
    mv -T $1/camera $1/_camera
    mkdir $1/camera
else
    echo "_camera文件夹已经存在"
fi

# $1="/home/nio/Videos/20230331T190552.SOC1"  #record目录地址
# $2="np/debug/dgb_aeb_strtg.rqabInfo.fcwReq" #监测信号
# $3="10000000000"  #监测信号变化记录时间（ns）
rename -v 's/h264.txt/txt/' $1/_camera/*txt

python3 ./pydds/tools/dds_signal_slice.py "$1" "$2" "$3" "$4"
#python3 ./tools/dds_signal_slice.py "$1" "$2" "$3" "$4"


for dir in $(ls $1/_record/slice_interval_record)
do
    echo $dir
    rm -rf $1/record/*
    cp $1/_record/slice_interval_record/$dir/record/*dat $1/record/
    rm -rf $1/camera/*
    cp $1/_record/slice_interval_record/$dir/camera/* $1/camera/
    adviz convert2rosbag $1 $1/_record/slice_interval_record/$dir/$dir.bag
done
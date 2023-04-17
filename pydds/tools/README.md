# NIODDS Data Tool
用于分析MAZU NIODDS中间件数据

# 准备工作：
1. 升级protobuf，确保其版本大于3.10
```
python3 -m pip install --upgrade protobuf
python3 -m pip list | grep protobuf
```

2. 下载并解压数据包
```
tar xzf YYYYMMDDTHHMMSS.SOCx.tar.gz
```

3. 在数据包内运行
```
cd YYYYMMDDTHHMMSS.SOCx
python3 ./bin/python/pydds/tools/dds_print.py

cd YYYYMMDDTHHMMSS.SOCx/bin/python/pydds/tools/
python3 dds_print.py

```

# 工具列表（持续开发中）

## dds_info.py
**打印数据文件的概览信息**
```python
python3 dds_info.py XX.pb.dat
```
输出内容类似如下所示：
```
                                summary                               
path                     python/example/apps-arb_out.pb.dat
topic                    apps/arb_out
type                     <class 'messages.apps.arb_out_pb2.ARBOut'>
messages                 17859
frequency (Hz)           48.27615914565652
duration (seconds)       369.934152096
start time (nanoseconds) 1625540787053688960 2021-07-06 11:06:27.053689
end time (nanoseconds)   1625541156987841056 2021-07-06 11:12:36.987841
size (KB)                1170.40234375
```
## dds_print.py
**将数据文件打印到终端或者文件**
```python
python3 dds_print.py XX.pb.dat [>a.txt]
```
`>a.txt`表示打印到文件，如果打印到终端可以省略
## dds_json.py
**将数据文件转换成json格式，可以打印到终端或者文件**
```python
python3 dds_json.py XX.pb.dat [>a.json]
```
`>a.json`表示打印到文件，如果打印到终端可以省略
## dds_interval.py
**以图表形式显示数据文件所存消息两帧之间的时间间隔**
使用前需要安装matplotlib，python3 -m pip install matplotlib
还要安装python3-tk，sudo apt install python3-tk
```python
python3 dds_interval.py XX.pb.dat
```
## dds_plot.py
**使用NioJuggler可视化数据**
请下载plotjuggler的蔚来优化版本Niojuggler，使用更简便：http://mazu.nioint.com/dist/plotjuggler/x86/NioJuggler-3.2.1-x86_64.AppImage
运行python脚本前安装websoket-client，python3 -m pip install websocket-client，并打开NioJuggler
```python
python3 dds_plot.py -f XX.pb.dat [-s plotjuggler_ip:port]
```
-s是可选项，默认plotjugger工作在本机，监听9871端口，如果plotjugger工作在其他机器，需要制定其ip和端口号
## dds_cut.py
**根据时间戳截取数据**
```python
python3 dds_cut.py XX.pb.dat start_timestamp(ns) end_timestamp(ns)
```
截取的文件存储在当前路径下，文件名包含起止时间戳
## dds_list.py
**显示数据收发时间戳和时间间隔**
```python
python3 dds_list.py XX.pb.dat
```
## dds_count.py
**检查是否漏帧**
```python
python3 dds_count.py XX.pb.dat
```

import cv2
import argparse
 
parser = argparse.ArgumentParser()
parser.add_argument('input_dir', type=str, help='please input directory')
parser.add_argument('start_ts', type=int, help='start ts')
parser.add_argument('end_ts', type=int, help='end_ts')
args = parser.parse_args()


def split_video(input_video, output_video, start_frame, end_frame):
    video_caputre = cv2.VideoCapture(input_video)

    # get video parameters
    fps = video_caputre.get(cv2.CAP_PROP_FPS)
    width = video_caputre.get(cv2.CAP_PROP_FRAME_WIDTH)
    height = video_caputre.get(cv2.CAP_PROP_FRAME_HEIGHT)

    print("fps:", fps)
    print("width:", width)
    print("height:", height)

    # 定义截取尺寸,后面定义的每帧的h和w要于此一致，否则视频无法播放
    split_width = int(width)
    split_height = int(height)
    size = (split_width, split_height)


    # fourcc = cv2.VideoWriter_fourcc(*'avc1')
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    # fourcc = 0x7634706d
    
    # 创建视频写入对象
    videp_write = cv2.VideoWriter(output_video, fourcc, fps, size)

    # print('Start!!!')
    # 读取视频帧
    success, frame_src = video_caputre.read()  # (960, 2560, 3)  # (height, width, channel)
    i = 0
    
    while success and not cv2.waitKey(1) == 27:  # 读完退出或者按下 esc 退出

        # [width, height] 要与上面定义的size参数一致，注意参数的位置
        # frame_target = frame_src[0:split_height, 0:split_width]  # (split_height, split_width)
        frame_target = frame_src[0:split_height, split_width:int(width)]  # (split_height, split_width)
        # cv2.imwrite("./pig/" + str(i) + ".jpg", frame_src)
        i += 1
        # 写入视频文件
        print(i)
        if i >= start_frame and i < end_frame:
            videp_write.write(frame_src)
        # 不断读取
        success, frame_src = video_caputre.read()

    # print("Finished!!!")
    video_caputre.release()

if __name__ == '__main__':
    input_file = '1.h264'
    output_file = 'Park_Front.h264'
    f = open('Park_Front.txt', 'r')
    start = 1680260903827238666 
    end = 1680260927575992685
    start_frame = -1
    end_frame = -1
    for l in f:
        line = l.split()
        start_time = int(line[0])
        end_time = int(line[1])
        print(line)
        frame = int(line[3])
        if start_time > start and end_time < end:
            if start_frame == -1:
                start_frame = frame
            end_frame = frame
    print(start_frame, end_frame)
    split_video(input_video=input_file, output_video=output_file, start_frame = start_frame, end_frame = end_frame)

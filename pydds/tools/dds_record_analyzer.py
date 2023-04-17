"""
DDS Record Analyzer is a tool to analyze dds_record data file

--file the path of the record data file
--folder the path of the record data folder
--data the path of the data file
--log the path of the log file

How to use:
# Analyze the dds_record data file
python dds_record_analyzer.py --file np-apps-ehy_obf_outputs.pb.dat

# Analyze the dds_record data file in specific folder
python dds_record_analyzer.py --folder record

# Analyze the dds_record data file to specific file
python dds_record_analyzer.py --file np-apps-ehy_obf_outputs.pb.dat --log np-apps-ehy_obf_outputs.log

"""
import argparse
import json
import logging
import os
import re
import sys
python_root = os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))
sys.path.append(python_root)
sys.path.append(os.path.join(python_root, 'messages'))
from pydds.bag import Bag


def covert_proto_data_file(path, output):
    """
    Convert proto data file with specific path to output file

    Parameters:
        path - the full path of proto file

    """
    try:
        bag = Bag(path)
    except Exception as e:
        logging.error(e)
        return

    if os.path.exists(output):
        os.remove(output)
    while True:
        json_data = bag.read_as_json()
        if json_data:
            json_dict = json.loads(json_data)
            with open(output, 'a+', encoding='utf-8') as f:
                f.write(json.dumps(json_dict))
                f.write('\n')
        else:
            break
    bag.close()


def log_analysis_result(log_dict):
    """
    Log analysis result with log dictionary

    Parameters:
        log_dict - the dictionary of the log

    """
    if log_dict['length'] > 0:
        logging.info(
            f"[DDS_RECORD]start at: {log_dict['first']['publish_ts']}, end at: {log_dict['last']['publish_ts']}")

    logging.info(
        f"[DDS_RECORD]Total number of messages: {log_dict['length']}")

    if len(log_dict['data_drop_list']) > 0:
        logging.error(
            f"[DDS_RECORD]Drop data result: {log_dict['data_drop_list']}")

    if len(log_dict['data_order_list']) > 0:
        logging.error(
            f"[DDS_RECORD]Wrong order result: {log_dict['data_order_list']}")

    if len(log_dict['data_repeat_list']) > 0:
        logging.error(
            f"[DDS_RECORD]Wrong repeat result: {log_dict['data_repeat_list']}")

    if len(log_dict['data_drop_list']) > 0 or len(log_dict['data_order_list']) > 0 or len(log_dict['data_repeat_list']) > 0:
        logging.error(f"[DDS_RECORD]Analysis result: FAIL")
    else:
        logging.info(f"[DDS_RECORD]Analysis result: PASS")


def analyze_dat_file(path):
    """
    Analyze dat file 

    Parameters:
        path - the path of the dat file
    Returns:
        log result

    """
    log_dict = {
        'length': 0,
        'first': {},
        'last': {},
        'data_drop_list': [],
        'data_order_list': [],
        'data_repeat_list': []
    }
    previous = {}
    with open(path) as f:
        count = 0
        while True:
            line = f.readline()
            # break if no data
            if not line:
                break
            data = json.loads(line)
            # set last data
            log_dict['last'] = data
            # set first data
            if count == 0:
                log_dict['first'] = data
                previous = data
            if count > 0:
                if float(data['counter']) != float(previous['counter']) + 1.0:
                    log_dict['data_drop_list'].append(data['counter'])
                if float(data['counter']) < float(previous['counter']):
                    print(data, '\n', previous)
                    log_dict['data_order_list'].append(data['counter'])
                if float(data['counter']) == float(previous['counter']):
                    log_dict['data_repeat_list'].append(data['counter'])
            previous = data
            count += 1
    log_dict['length'] = count
    return log_dict


def get_file_size(path):
    """
    Get the size of the file in specific path

    Parameters:
        path - the full path of the file

    Returns:
        the size of the file

    """
    return os.path.getsize(path)


def analyze_file(path, dat_file):
    """
    Analyze proto data file with specific path of dat file

    Parameters:
        path - the path of the proto data file
        dat_file - the path of the dat file

    """
    if get_file_size(path):
        covert_proto_data_file(path, dat_file)
        if os.path.exists(dat_file):
            log_dict = analyze_dat_file(dat_file)
            log_analysis_result(log_dict)
        else:
            logging.info(f"[DDS_RECORD]Analyze {path}: File is empty!")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--file', action='store', default='',
                        required=False, help='the path of the dds_record proto file')
    parser.add_argument('--folder', action='store', default='',
                        required=False, help='the path of the dds_record proto folder')
    parser.add_argument('--dat', action='store', default='./dds_record_analyzer.dat',
                        required=False, help='the path of the json file')
    parser.add_argument('--log', action='store', default='./dds_record_analyzer.log',
                        required=False, help='the path of the log file')
    args = parser.parse_args()

    format = '%(asctime)s - %(levelname)s: %(message)s'
    logging.basicConfig(level=logging.INFO,
                        filename=args.log,
                        filemode='w',
                        format=format)

    dat_file = args.dat

    if args.file:
        logging.info(f"[DDS_RECORD]Analyze {args.file}")
        analyze_file(args.file, args.dat)

    if args.folder:
        for _, _, files in os.walk(args.folder):
            for file in files:
                logging.info(f"[DDS_RECORD]Analyze {file}")
                file_path = os.path.join(args.folder, file)
                analyze_file(file_path, args.dat)

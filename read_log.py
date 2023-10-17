import os
import sys

from datetime import datetime

# 主功能: 初始化main函数入口
def initial_main():
    calico_log_path = '/var/log/calico'
    calico_log_path_res = os.listdir(calico_log_path)
    log_result = convert_log_abs_path(calico_log_path,calico_log_path_res)
    strategy_master(log_result)
    
# 功能1: 定位要找到日志的所在路径范围
def convert_log_abs_path(calico_log_path,calico_log_path_res):
    file_res_mapping = {}
    feature_extensions_name = ['.log']
    counter_x = 0
    abs_file_name_list = []
    while counter_x < len(calico_log_path_res):
        convert_calico_log_path_res = os.path.join(calico_log_path,calico_log_path_res[counter_x])
        base_file_name = os.path.basename(convert_calico_log_path_res)
        prefix_file,file_extensions = os.path.splitext(base_file_name)
        determine_excucte_list = [y for y in [f'{file_extensions}'] if y in feature_extensions_name]
        if determine_excucte_list == []:
            if os.path.isfile(convert_calico_log_path_res) == True:
                pass
            else:
                convert_second_abs_path_res = os.listdir(convert_calico_log_path_res)
                for b in convert_second_abs_path_res:
                    convert_second_abs_path = os.path.join(convert_calico_log_path_res,b)
                    base_second_file_name = os.path.basename(convert_second_abs_path)
                    prefix_second_file, second_file_extensions = os.path.splitext(base_second_file_name)
                    if prefix_second_file == 'calico':
                        print('定位到所要的日志文件:',convert_second_abs_path)
                        abs_file_name_list.append(convert_second_abs_path)

                    elif [a for a in [f"{second_file_extensions}"] if a in feature_extensions_name] != []:
                        print('有相应的但是名称对不齐的日志文件:',convert_second_abs_path)
                        abs_file_name_list.append(convert_second_abs_path)

                    else:
                        pass
                    
                    file_res_mapping['abs_path'] = abs_file_name_list
            pass 
        else:
            if prefix_file == 'calico':
                file_res_mapping['abs_path'] = convert_calico_log_path_res 
            else:
                pass
        counter_x += 1
    return file_res_mapping

# 功能2: 把读取到的日志结果映射到指定字典里面传递出去
def strategy_master(log_result):
    print('策略大师开始拆解日志',log_result)
    if log_result == []:
        sys.exit()
    else:
        pass

    counter_logs_line = 0
    counter_numbers = 1
    convert_key_list = list(log_result.keys())
    messages_mapping = {}
    log_number = 0
    for keys in convert_key_list:
        values = log_result.get(keys)
        for files in values:
            with open(files,mode='r') as logfile:
                convert_log_res_list = logfile.readlines() 
                print('正在读取日志为:',files,'\n','日志长度为:',len(convert_log_res_list))
                while counter_logs_line < len(convert_log_res_list):
                    single_log_lines = convert_log_res_list[counter_logs_line]
                    convert_single_log_lines_list = single_log_lines.split(" ")
                    time_stamp = single_log_lines.split(" ")[0:2]
                    slice_convert_single_log_lines_list = convert_single_log_lines_list[2:]
                    catcher_tag_flag = slice_convert_single_log_lines_list[0:-1]
                    messages_mapping['LogAbsPath'] = [f"{files}"] 
                    messages_mapping['Trigger'] = [log_number]
                    messages_mapping['LineNumber'] = [f"{counter_numbers}"]
                    messages_mapping['TimeStamp'] = time_stamp
                    messages_mapping['LogContent'] = slice_convert_single_log_lines_list      
                    counter_logs_line += 1
                    counter_numbers += 1
                    print('正在传递映射好的字典给下一个环节,日志分析大师-->',type(messages_mapping))
                    analysis_logger(messages_mapping)
                log_number += 1
    
'''
[ERROR] 发生错误了
[WARNING] 有告警
[INFO] 正常的信息记录
需求: 
1.有时间戳包括几分几秒
2.只做错误和告警的切分
3.什么文件的 什么告警内容
'''
# 功能3: 使用元组推导式进行精准匹配
def analysis_logger(messages_mapping):
    print('日志分析大师接收到字典数据的钥匙列表长度为-->',len(messages_mapping.keys()))
    if type(messages_mapping) == dict:
        print('映射到的字典为:',messages_mapping)
    else:
        print('为错误或者没有映射出来',type(messages_mapping),messages_mapping)
        
    messages_key_list = list(messages_mapping.keys())
    counter_z = 0 
    tag_flag = '*'
    convert_log_tag_flag = messages_mapping['LogContent']
    
    catcher_tag_flag_feature = ("ERROR","WARNING")
    execute_read_log_result = [z for z in convert_log_tag_flag if z in catcher_tag_flag_feature]
    if execute_read_log_result == []:
        pass
    else:
        print('找到对应的错误以及告警行数在第',messages_mapping['LineNumber'],'行对应的时间节点为:',messages_mapping['TimeStamp'])
    print(f'{tag_flag * 108}')
    
                    
if __name__ == '__main__':
    initial_main()
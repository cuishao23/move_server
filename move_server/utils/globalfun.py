import configparser
import fcntl
import datetime


def get_conf(section, key, path):
    conf = configparser.ConfigParser()
    try:
        with open(path, 'r', encoding='utf-8') as f:
            fcntl.flock(f.fileno(), fcntl.LOCK_SH)
            conf.read_file(f)
            fcntl.flock(f.fileno(), fcntl.LOCK_UN)
        str_val = conf.get(section, key)
    except Exception:
        str_val = None
    return str_val


# 转换时间格式
def get_time(old_time):
    '''
    时间戳转换为指定格式的日期: "1575513188" -> "2019-12-05 10:33:08"
    '''
    if old_time == None:
        pass
    else:
        dateArray = datetime.datetime.fromtimestamp(old_time)
        new_time = dateArray.strftime("%Y-%m-%d %H:%M:%S")
        return new_time
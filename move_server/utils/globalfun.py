import configparser
import fcntl


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

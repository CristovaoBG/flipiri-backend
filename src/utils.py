from datetime import datetime

def str_to_datetime(s):
    return datetime.strptime(s, '%Y-%m-%dT%H:%M')




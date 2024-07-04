from datetime import datetime
import re

def date_to_str_simple(d: datetime) -> str:
    return str(d.day).zfill(2) + '/' + str(d.month).zfill(2)

def time_to_str_simple(d: datetime) -> str:
    return str(d.hour) + 'h' + (str(d.minute).zfill(2) if d.minute != 0 else '')

def str_to_datetime(s):
    return datetime.strptime(s, '%Y-%m-%dT%H:%M')

def datetimes_have_intersection(start1, end1, start2, end2):
    return max(start1, start2) < min(end1, end2)

def str_contains_html(text):
    return bool(re.search('<[a-z][\s\S]*>', text, re.I))
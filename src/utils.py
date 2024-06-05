from datetime import datetime

def str_to_datetime(s):
    return datetime.strptime(s, '%Y-%m-%dT%H:%M')

def datetime_collides(start_one: datetime, end_one: datetime, start_two: datetime, end_two: datetime):
    return start_one <= end_two and start_two <= end_one

def datetimes_have_intersection(start1, end1, start2, end2):
    return max(start1, start2) < min(end1, end2)

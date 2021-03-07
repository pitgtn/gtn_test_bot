import time

def needs_refresh(end_dates:[]):
    if len(end_dates) == 0:
        return True

    min_time = time.time()
    for date in end_dates:
        if time.mktime(date.timetuple()) < min_time:
            return True

    return False
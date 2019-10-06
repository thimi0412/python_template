from datetime import datetime


def get_str_now():
    date = datetime.now()
    return date.strftime('%Y%m%d%H%M%S')

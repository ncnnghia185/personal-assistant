from datetime import datetime, date


def get_time():
    now = datetime.now()
    current_time = now.strftime("%H hours %M minutes %S seconds")
    return current_time


def get_hour():
    now = datetime.now()
    return now.strftime("%H")


def get_date():
    return str(date.today())

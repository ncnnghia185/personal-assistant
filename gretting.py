from time_module import get_hour, get_date
from output_module import output
from database import update_last_seen, get_last_seen
from datetime import date


def greet():
    previous_date = get_last_seen()

    today_date = get_date()
    update_last_seen(today_date)

    if previous_date == today_date:
        output("Welcome back bro")
    else:
        hour = int(get_hour())
        if 4 <= hour < 12:
            output("Good Morning!")
        elif 12 <= hour < 18:
            output("Good Afternoon")
        else:
            output("Good Evening")

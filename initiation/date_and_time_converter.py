# Computer date and time format consists only of numbers, for example: 21.05.2018 16:30.
# Humans prefer to see something like this: 21 May 2018 year, 16 hours 30 minutes.
# Your task is simple - convert the input date and time from computer format into a "human" format.
# Input: Date and time as a string
# Output: The same date and time, but in a more readable format as a string
# Example:
# assert date_time("01.01.2000 00:00") == "1 January 2000 year 0 hours 0 minutes"
# assert date_time("09.05.1945 06:07") == "9 May 1945 year 6 hours 7 minutes"
import datetime as dt


def date_time(time: str) -> str:
    FORMAT_to_dt = '%d.%m.%Y %H:%M'
    to_dt = dt.datetime.strptime(time, FORMAT_to_dt)
    minutes = lambda x: 'minute' if x == 1 else 'minutes'
    hours = lambda x: 'hour' if x == 1 else 'hours'
    FORMAT_from_dt = f'%#d %B %Y year %#H {hours(to_dt.hour)} %#M {minutes(to_dt.minute)}'
    from_dt = to_dt.strftime(FORMAT_from_dt)
    return from_dt


if __name__ == "__main__":
    print("Example:")
    assert (
        date_time("01.01.2000 00:00") == "1 January 2000 year 0 hours 0 minutes"
    ), "Millenium"
    assert (
        date_time("09.05.1945 06:30") == "9 May 1945 year 6 hours 30 minutes"
    ), "Victory"
    assert (
        date_time("20.11.1990 03:55") == "20 November 1990 year 3 hours 55 minutes"
    ), "Somebody was born"
    print("Coding complete? Click 'Check' to earn cool rewards!")


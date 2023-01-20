from datetime import datetime

from dateutil.tz import tzlocal


def get_now():
    return datetime.now(tzlocal())  # pyaphid: ignore


datetime.now()

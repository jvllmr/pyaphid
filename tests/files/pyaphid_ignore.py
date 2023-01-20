from contextlib import closing
from datetime import datetime

from dateutil.tz import tzlocal

datetime.now()  # pyaphid: ignore


def get_now():
    return datetime.now(tzlocal())  # pyaphid: ignore


file = open("abc")
with closing(file):  # pyaphid: ignore
    pass

async with closing(file):  # pyaphid: ignore
    pass

if datetime.now():  # pyaphid: ignore
    pass


for value in datetime.now():  # pyaphid: ignore
    pass


async for value in datetime.now():  # pyaphid: ignore
    pass


list_ = [datetime.now() for _ in range(100)]  # pyaphid: ignore

datetime.now()

import time
import random
from datetime import datetime

def random_sleep(min_time: float) -> None: # Tasker's func - https://github.com/z-tasker/qloader/blob/master/qloader/browserdriver.py
    """
        Fuzz wait times between [min_time, min_time*2]
    """
    time.sleep(min_time + min_time * random.random())

def stringToDate(dateStr: str, dateFormat) -> datetime:
    return datetime.strptime(dateStr, dateFormat)


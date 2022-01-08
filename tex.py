from datetime import datetime, timedelta

from time import sleep
import time


n = datetime.now()

time.sleep()

e = datetime.now()

total = e-n

hours = total.seconds // 3600
mintues = (total.seconds // 60) % 60

print(hours, mintues)

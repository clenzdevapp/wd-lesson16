import time
from datetime import datetime

localtime = time.asctime(time.localtime())
localtime2 = time.localtime(time.time())
print localtime
print localtime2
import time
from datetime import datetime

timestamp=time.time()
print(timestamp)


timer01=datetime.now()
print(timer01)

timer=datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
print(timer)
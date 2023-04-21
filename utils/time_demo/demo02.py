import  time

time_stamp=time.time()
print(time_stamp)

struct_time=time.localtime()
print(struct_time)
print(struct_time.tm_year)
print(time.strftime('%Y-%m-%d:%H-%M-%S',struct_time))

print('--------------')
format_time=time.strftime('%Y-%m-%d:%H-%M-%S %p')
print(format_time)


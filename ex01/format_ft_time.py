import time
import datetime

# https://stackoverflow.com/questions/4548684/how-to-get-the-seconds-since-epoch-from-the-time-date-output-of-gmtime

# https://www.programiz.com/python-programming/datetime/strftime


print("Seconds since January 1, 1970: ", end = "")
sec = time.time()
print(sec, end = "")
print(" or", end = "")
print("  ...   ", end = "")
print(" in scientific notation")
x = datetime.datetime.now()
print(x.strftime("%b %d %Y")) 

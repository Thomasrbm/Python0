import time
import datetime
import decimal

# https://stackoverflow.com/questions/4548684/how-to-get-the-seconds-since-epoch-from-the-time-date-output-of-gmtime

# https://www.programiz.com/python-programming/datetime/strftime

# https://docs.python.org/3/library/string.html#format-specification-mini-language



print("Seconds since January 1, 1970: ", end = "")
sec = time.time()
print(f"{sec:,.4f}", end = "")
print(" or ", end = "")
print((f"{sec:.2e}"), end = "")
print(" in scientific notation")
x = datetime.datetime.now()
print(x.strftime("%b %d %Y")) 

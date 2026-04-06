import time

# https://stackoverflow.com/questions/4548684/how-to-get-the-seconds-since-epoch-from-the-time-date-output-of-gmtime

print("Seconds since January 1, 1970: ", end = "")
print(time.time(), end = "")
print(" or", end = "")
print("  ...   ", end = "")
print(" in scientific notation", end = "")
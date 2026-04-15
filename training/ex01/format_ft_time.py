import datetime

now = datetime.datetime.now()
epoch = now.timestamp()
print(f"Seconds since January 1, 1970: {epoch:,.4f} or {epoch:.3} \
in scientific notation\n{now.strftime("%b %d %Y")}")

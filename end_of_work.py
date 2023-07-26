import datetime

dt = datetime.datetime.now()
dt = dt.replace(hour=19, minute=0)

split = "minutes"
old_val = 0
while True:
    nw = datetime.datetime.now()
    diff = dt - nw
    d = {"days": diff.days}
    d["hours"], rem = divmod(diff.seconds, 3600)
    d["minutes"], d["seconds"] = divmod(rem, 60)
    if (d[split] != old_val):
        print(dt.strftime("%H:%M") + " -", "{hours}h {minutes}m".format(**d))
        old_val = d[split]

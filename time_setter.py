import subprocess
import shlex
import datetime

nw = datetime.datetime.now()
nw = nw.replace(hour=nw.hour+4)
time_string = nw.isoformat()

subprocess.call(shlex.split("sudo date -s '%s'" % time_string))
subprocess.call(shlex.split("sudo hwclock -w"))


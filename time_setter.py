import subprocess
import shlex
import datetime

# need to be used only once, time will remain even after reboot

nw = datetime.datetime.now()
nw = nw.replace(hour=nw.hour-2)
time_string = nw.isoformat()

subprocess.call(shlex.split("sudo date -s '%s'" % time_string))
subprocess.call(shlex.split("sudo hwclock -w"))


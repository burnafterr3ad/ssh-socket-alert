#!/usr/bin/env python
import os
import re
import time
CMD_MATCH = 'init'
ALERTED_PIDS = []
def get_pids():
    dirs = os.listdir('/proc')
    r = re.compile('^\d+$')
    pids = list(filter(r.match, dirs))
    return pids
def get_cmds(pids):
    for pid in pids:
        if pid not in ALERTED_PIDS:
            f = "/proc/" + pid + "/cmdline"
            cmd = get_cmdline(f)
            if CMD_MATCH in cmd:
                print("Found "+ CMD_MATCH + " in " +f)
                ALERTED_PIDS.append(pid)
def get_cmdline(f):
    with open (f, "r") as myfile:
        data = myfile.readline()
    return data
if __name__ == "__main__":
    while True:
        pids = get_pids()
        get_cmds(pids)
        time.sleep(60)

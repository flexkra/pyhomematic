#!/usr/bin/python3
import time
import sys
import logging
from pyhomematic import HMConnection

logging.basicConfig(level=logging.INFO)



def systemcallback(src, *args):
    print(src)
    for arg in args:
        print(arg)

try:
    # Create a server that listens on 127.0.0.1:7080 and identifies itself as myserver.
    # Connect to Homegear at 127.0.0.1:2001
    # Automatically start everything. Without autostart, pyhomematic.start() can be called.
    # We add a systemcallback so we can see what else happens besides the regular events.
    pyhomematic = HMConnection(interface_id="myserver",
                               autostart=True,
                               systemcallback=systemcallback,
                               remotes={"rf":{
                                   "ip":"192.168.7.130",
                                   "port": 2001}})
except Exception:
    sys.exit(1)

sleepcounter = 0

def eventcallback(address, interface_id, key, value):
    print("CALLBACK: %s, %s, %s, %s" % (address, interface_id, key, value))

while not pyhomematic.devices and sleepcounter < 20:
    print("Waiting for devices")
    sleepcounter += 1
    time.sleep(1)
print(pyhomematic.devices)



pyhomematic.stop()

sys.exit(0)

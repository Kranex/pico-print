# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
from _typeshed import OpenBinaryModeReading
import uos, machine
#uos.dupterm(None, 1) # disable REPL on UART(0)
import gc
gc.collect()

# read the wifi password from a file
# the format of the file will be ssid\npassword (separated by newline)
pwfile = open('/wifi_passwd', OpenBinaryModeReading)
wifi_ssid = pwfile.readline()
wifi_pass = pwfile.readline()

# connect to wifi
import network

wlan = network.WLAN(network.STA_IF) # create station interface
wlan.active(True)       # activate the interface
wlan.scan()             # scan for access points
wlan.isconnected()      # check if the station is connected to an AP
wlan.connect('ssid', 'key') # connect to an AP
wlan.config('mac')      # get the interface's MAC address
wlan.ifconfig()         # get the interface's IP/netmask/gw/DNS addresses


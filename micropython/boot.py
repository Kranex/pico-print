# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
import uos, machine
#uos.dupterm(None, 1) # disable REPL on UART(0)
import gc
gc.collect()

# read the wifi password from a file
# the format of the file will be ssid\npassword (separated by newline)
import json
confstr = open('config.json', 'r')
config = json.load(confstr)

# connect to wifi
import network

wlan = network.WLAN(network.STA_IF) # create station interface
wlan.active(True)
if not wlan.isconnected():
    print(wlan.scan())
    print('connecting to network...')
    wlan.connect(config["wifi"]["ssid"], config["wifi"]["pass"])
    while not wlan.isconnected():
        pass

ifconfig = wlan.ifconfig()

# print('network config:', ifconfig)
print('current ip: ', ifconfig[0])

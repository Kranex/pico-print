# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
import uos, machine
#uos.dupterm(None, 1) # disable REPL on UART(0)
import gc
gc.collect()

# read the wifi password from a file
# the format of the file will be ssid\npassword (separated by newline)
pwfile = open('/wifi_passwd', 'r')
wifi_ssid = pwfile.readline()
wifi_pass = pwfile.readline()

# connect to wifi
import network

wlan = network.WLAN(network.STA_IF) # create station interface
wlan.active(True)
if not wlan.isconnected():
    print(wlan.scan())
    print('connecting to network...')
    wlan.connect(wifi_ssid, wifi_pass)
    while not wlan.isconnected():
        pass
print('network config:', wlan.ifconfig())


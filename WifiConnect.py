import WifiProfile
import network

def connect():


    if(WifiProfile.password == 'none'):
       ap = network.WLAN(network.AP_IF)
       ap.active(True)
       ap.config(essid='ELSA-AP')
       ip = ap.ifconfig()
       print(ip)
       return ip[0]
    else:
       station = network.WLAN(network.STA_IF)

       if station.isconnected() == True:
           print("Already connected")
           ip=station.ifconfig()
           return ip[0]

       station.active(True)
       station.connect(WifiProfile.ssid, WifiProfile.password)

       while station.isconnected() == False:
          pass

       print("Connection successful")
       ip = station.ifconfig()
       print(ip)
       return ip[0]


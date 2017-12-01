import WifiProfile

def connectSTA():
    import network

    station = network.WLAN(network.STA_IF)

    if station.isconnected() == True:
        print("Already connected")
        return

    station.active(True)
    station.connect(WifiProfile.ssid, WifiProfile.password)

    while station.isconnected() == False:
        pass

    print("Connection successful")
    print(station.ifconfig())


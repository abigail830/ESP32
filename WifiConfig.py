import WifiProfile

def getWifiProfile():
   profileDictionary={"ssid":WifiProfile.ssid, "password":WifiProfile.password}
   return profileDictionary


def getWifiProfile(userID, pwd):
   f=open('WifiProfile.py','w')
   f.write('ssid=\"userID\"\n')
   f.write('password=\"pwd\"\n')
   f.close()


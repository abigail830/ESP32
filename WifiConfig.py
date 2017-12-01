import re

fileName="WifiConnect.py"
re_id=re.compile('(?:ssid=)(.*)')
re_pwd=re.compile('(?:password=)(.*)')

def getID():
   f=open(fileName)
   content=f.read()
   result=re.search(re_id,content)
   f.close()
   return result.group(1)

def getPwd():
   f=open(fileName)
   content=f.read()
   result=re.search(re_pwd,content)
   f.close()
   return result.group(1)

def setID(input_id):
   new_id="ssid="+input_id
   f=open(fileName,'r+')
   content=f.read()
   new_content=re.sub(re_id,new_id,content)
   f.truncate(0)
   f.write(new_content)
   f.close()
   print("SSID is updated to "+ input_id)

def setPwd(input_pwd):
   new_pwd = "password="+input_pwd
   f=open(fileName)
   content=f.read()
   new_content = re.sub(re_pwd,new_pwd,content)
   f.truncate(0)
   f.write(new_content)
   f.close() 
   print("PASSWORD is udpated to "+input_pwd)




import picoweb
import ujson
import WifiConfig
import machine
 
app = picoweb.WebApp(__name__)


@app.route("/")
def index(req,resp):
   yield from picoweb.start_response(resp,content_type = "text/html")
   htmlFile = open('home.html','r')
   for line in htmlFile:
      yield from resp.awrite(line)


@app.route("/wifi")
def getwificonfig(req, resp):
   yield from picoweb.jsonify(resp, WifiConfig.getWifiProfile())


@app.route("/setwifi")
def setwificonfig(req,resp):
   queryString = req.qs
   parameters = qs_parse(queryString)
   print(parameters)
   WifiConfig.setWifiProfile(parameters["ssid"], parameters["password"])
   yield from picoweb.start_response(resp)
   yield from resp.awrite("Wifi profile updated successfully.")


@app.route("/reset")
def reset(req,resp):
    yield from picoweb.start_response(resp)
    yield from resp.awrite("ESP32 will be hard reset now...")
    machine.reset()


@app.route("/getPinValue")
def getPinValue(req,resp):
   queryString = req.qs
   parameters = qs_parse(queryString)
   pin_num = parameters["pin"]
   pin = machine.Pin(int(pin_num))
   print('getPinValue for ' + pin_num + ' and result is '+str(pin.value()))
   yield from picoweb.start_response(resp)
   yield from resp.awrite(str(pin.value()))


@app.route("/getPinADCValue")
def getPinADCValue(req,resp):
   queryString = req.qs
   parameters = qs_parse(queryString)
   pin_num = parameters["pin"]
   pin = machine.ADC(int(pin_num))
   print('getPinADCValue for ' + pin_num + ' and result is '+str(pin.read()))
   yield from picoweb.start_response(resp)
   yield from resp.awrite(str(pin.read()))


@app.route("/setPinValue")
def setPinValue(req,resp):
   queryString = req.qs
   parameters = qs_parse(queryString)
   pin_num = parameters["pin"]
   targetValue = parameters["value"]
   print('Going to setPinValue for ' + pin_num + ' with target value ' + targetValue)
   pin = machine.Pin(int(pin_num), machine.Pin.OUT)
   pin.value(int(targetValue))
   yield from picoweb.start_response(resp)
   yield from resp.awrite("Done!")


@app.route("/setPWMValue")
def setPWMValue(req,resp):
   queryString = req.qs
   parameters = qs_parse(queryString)
   pin_num = parameters["pin"]
   targetFreq = parameters["freq"]
   targetDuty = parameters["duty"]
   print('Going to setPinValue for ' + pin_num + ' with target Freq/Duty value: ' + targetFreq+"/"+targetDuty)

   pin = machine.Pin(int(pin_num))
   pwmPin = machine.PWM(pin)
   pwmPin.freq(int(targetFreq))
   pwmPin.duty(int(targetDuty))

   yield from picoweb.start_response(resp)
   yield from resp.awrite("Done!")


def qs_parse(qs):
  parameters = {}
  ampersandSplit = qs.split("&")

  for element in ampersandSplit:
    equalSplit = element.split("=")
    parameters[equalSplit[0]] = equalSplit[1]

  return parameters




 

import picoweb
import ujson
import WifiConfig
import machine
 
app = picoweb.WebApp(__name__)


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


@app.route("/")
def index(req,resp):
   yield from picoweb.start_response(resp,content_type = "text/html")
   htmlFile = open('home.html','r')
   for line in htmlFile:
      yield from resp.awrite(line)


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

@app.route("/setPinValue")
def getPinValue(req,resp):
   queryString = req.qs
   parameters = qs_parse(queryString)
   pin_num = parameters["pin"]
   print('setPinValue for ' + pin_num)
   yield from picoweb.start_response(resp)
   yield from resp.awrite("Going to set Pin Value")

@app.route("/setPWMValue")
def getPinValue(req,resp):
   queryString = req.qs
   parameters = qs_parse(queryString)
   pin_num = parameters["pin"]
   print('setPWMValue for ' + pin_num)
   yield from picoweb.start_response(resp)
   yield from resp.awrite("Going to set PWM Value")

def qs_parse(qs):
  parameters = {}
  ampersandSplit = qs.split("&")

  for element in ampersandSplit:
    equalSplit = element.split("=")
    parameters[equalSplit[0]] = equalSplit[1]

  return parameters




 

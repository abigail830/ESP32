import picoweb
import ujson
import WifiConfig
 
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


def qs_parse(qs):

  parameters = {}
  ampersandSplit = qs.split("&")

  for element in ampersandSplit:
    equalSplit = element.split("=")
    parameters[equalSplit[0]] = equalSplit[1]

  return parameters




 

import picoweb
import ujson
import WifiConfig
 
app = picoweb.WebApp(__name__)
 
@app.route("/WifiConfig")
def getwificonfig(req, resp):
   wifiProfileJson = ujson.dumps(WifiConfig.getWifiProfile())
   yield from picoweb.start_response(resp, content_type = "application/json")
   yield from resp.awrite(wifiProfileJson)

@app.route("/")
def index(req,resp):
   yield from picoweb.start_response(resp,content_type = "text/plain")
   yield from resp.awrite("Hello World!")



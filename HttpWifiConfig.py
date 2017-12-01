import picoweb
import ujson
import WifiConfig
 
app = picoweb.WebApp(__name__)
 
@app.route("/")
def index(req, resp):
   wifiProfileJson = ujson.dumps(WifiConfig.getWifiProfile())
   yield from picoweb.start_response(resp, content_type = "application/json")
   yield from resp.awrite(wifiProfileJson)


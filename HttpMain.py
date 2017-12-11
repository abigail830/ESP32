import picoweb
import ujson
import WifiConfig
 
app = picoweb.WebApp(__name__)
 
@app.route("/wifi")
def getwificonfig(req, resp):
   yield from picoweb.jsonify(resp, WifiConfig.getWifiProfile())

@app.route("/setwifi")
def setwificonfig(req,resp):
   print(req.qs)
   yield from picoweb.start_response(resp)
   yield from resp.awrite("Http Post received.")

@app.route("/")
def index(req,resp):
   yield from picoweb.start_response(resp,content_type = "text/html")
   htmlFile = open('home.html','r')
   for line in htmlFile:
      yield from resp.awrite(line)




 

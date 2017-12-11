import picoweb
import ujson
import WifiConfig
 
app = picoweb.WebApp(__name__)
 
@app.route("/wifi")
def getwificonfig(req, resp):
   if(req.method == 'GET'):
      wifiProfileJson = ujson.dumps(WifiConfig.getWifiProfile())
      yield from picoweb.start_response(resp, content_type = "application/json")
      yield from resp.awrite(wifiProfileJson)
   else:
      postData = req.read_form_data()
      print(postData)
      yield from picoweb.start_response(resp, content_type="text/html")
      yield from resp.awrite("Http Post received.")

@app.route("/")
def index(req,resp):
   yield from picoweb.start_response(resp,content_type = "text/html")
   htmlFile = open('home.html','r')
   for line in htmlFile:
      yield from resp.awrite(line)




 

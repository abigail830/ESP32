import picoweb
import ujson
import WifiConfig
 
app = picoweb.WebApp(__name__)
 
@app.route("/wifi")
def getwificonfig(req, resp):
   if(req.method == 'GET'):
      picoweb.jsonify(resp, WifiConfig.getWifiProfile())
   else:
      print(req.form)
      yield from picoweb.start_response(resp, content_type="text/html")
      yield from resp.awrite("Http Post received.")

@app.route("/")
def index(req,resp):
   yield from picoweb.start_response(resp,content_type = "text/html")
   htmlFile = open('home.html','r')
   for line in htmlFile:
      yield from resp.awrite(line)




 

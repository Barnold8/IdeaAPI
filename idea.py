import sys
from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from random import randint

PORT = "8000"
HOST = "localhost"



class ServServer(BaseHTTPRequestHandler):

    def write_start(self,string="Idea"):
        css = ["html{ margin:0px; padding:0px;font-family: Arial, Helvetica, sans-serif;}","body{background-color:#ccc;}","h1 {text-align: center;margin-top:25%;font-size:450%;}","div{ margin-top:24%; text-align:center;font-size:210%;}"]

        self.wfile.write(bytes("<html><head><title>{}</title><style>".format(string),"utf-8"))

        for styles in css:
            self.wfile.write(bytes(styles,"utf-8"))

        self.wfile.write(bytes("</style></head>","utf-8"))

    def do_GET(self): # Get request handler

        split_path = self.path.split("/")
        # print("split_path: {}".format(split_path))

        if split_path[1].lower() == "json":
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            
            if split_path[len(split_path)-1] == "dadjokes":
                with open("Assets/DadJokes.txt","r",encoding="utf8") as file:
                    f = file.readlines()
                    joke = f[randint(0,len(f))].split("<>")
                    self.wfile.write(json.dumps({'Build-up': joke[0].strip(), 'Payoff': joke[1].strip()}).encode("utf-8"))
            else:   # The actual API
                with open("Assets/Ideas.txt","r",encoding="utf8") as file:
                    f = file.readlines()
                    idea = f[randint(0,len(f))]
                    self.wfile.write(json.dumps({'Idea': idea.strip()}).encode("utf-8"))
              
        else:
            self.send_response(200)
            self.send_header("Content-type","text/html")
            self.end_headers()
            
            if split_path[1].lower() == "dadjokes":
                self.write_start("Dad jokes!")
                self.wfile.write(bytes("<marquee>Dad jokes</marquee>","utf-8"))
                with open("Assets/DadJokes.txt","r",encoding="utf8") as file:
                    f = file.readlines()
                    joke = f[randint(0,len(f))].split("<>")
                    self.wfile.write(bytes("<div>{} {}</div>".format(joke[0],joke[1]),"utf-8"))
                    self.wfile.write(bytes("</html>","utf-8"))
            else:
                with open("Assets/Ideas.txt","r",encoding="utf8") as file:
                    self.write_start()
                    f = file.readlines()
                    idea = f[randint(0,len(f))]
                    self.wfile.write(bytes("<div>{}</div>".format(idea),"utf-8"))
                    self.wfile.write(bytes("</html>","utf-8"))
                   
                   
                

                
if __name__ == "__main__":

    arguments = [args for args in sys.argv]
    arguments = arguments[1:len(arguments)]

    PORT = arguments[0] if len(arguments) > 0 else PORT
    HOST = arguments[1] if len(arguments) > 1 else HOST

    print("Server intialising at {}:{}".format(HOST,PORT))
    
    webServer = HTTPServer((HOST, int((PORT))), ServServer)

    try:
        print("Server launched at https://{}:{}".format(HOST,PORT))
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

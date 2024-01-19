from microdot_asyncio import Microdot, Response, send_file
from microdot_utemplate import render_template
from microdot import Request
from machine import Pin, I2C
from time import sleep
import dht 

I2C_ID = 0
SCL_PIN = 1
SDA_PIN = 0



app = Microdot()
Response.default_content_type = "text/html"

name1 = []
inputs = []
aux_name = []
aux_input = []
nod = 0
noin = 0
status = []
status_in = []

# index.html root route
@app.route("/")
async def index(request):
    global name1
    global nod
    global status
    output = request.form
    #print(output)
    if output == None:
        for inp in range(len(inputs)):
            status_in[inp] = Pin(int(inputs[inp]), Pin.IN, Pin.PULL_DOWN).value()
            print(status_in[inp])
        return render_template("ledon.html", name1 = name1, status = status, inputs = inputs, status_in = status_in)
        
    if output["name"] == "ADD":
        return render_template("index.html")
    if output["name"] == "RMV":
        return render_template("remove.html", name1 = name1, inputs = inputs)
    
    

    
    return render_template("ledon.html", name1 = name1, status = status, inputs = inputs, status_in = status_in)

# Read sensor readings and return as JSON
@app.route("/leds", methods = ['POST', 'GET'])
async def led(request):
    

    global name1
    global inputs
    global nod
    global noin
    global status
    
    ok = 0
    okin = 0
    output = request.form
    if output["name"] == "ADD":
        return render_template("index.html")
    if output["name"] == "RMV":
        return render_template("remove.html", name1 = name1, inputs = inputs)
    if output["name"]!= "":
        aux_name.append(output["name"])
        
        for bec in aux_name:
            if bec not in name1:
                name1.append(bec)
                nod = nod + 1
                status.append(0)
                ok = 1
                
    if output["name_in"]!= "":
        aux_input.append(output["name_in"])
        
        for inp in aux_input:
            if inp not in inputs:
                inputs.append(inp)
                noin = noin + 1
                status_in.append(0)
                okin = 1
    
    if ok == 1:
        if name1[nod-1] != "LED":
            Pin(int(name1[nod-1]), Pin.OUT).value(0)
            status[nod-1] = 0
        else:
            Pin(name1[nod-1], Pin.OUT).value(0)
            status[nod-1] = 0
    

      
        
        
    for inp in range(len(inputs)):
        status_in[inp] = Pin(int(inputs[inp]), Pin.IN, Pin.PULL_DOWN).value()
        print(status_in[inp])
      
    
    return render_template("ledon.html", name1 = name1, status = status, inputs = inputs, status_in = status_in )

@app.route("/remove", methods = ['POST', 'GET'])
async def led(request):
    global name1
    global inputs
    global status
    global status_in
    global nod
    global noin
    global aux_input
    global aux_name
    aux_string = request.form
    buton = aux_string["name"]
    print(aux_string["name"])
    if len(name1) == 0 and len(inputs) ==0:
            return render_template("index.html")
    if buton == "RMV":
        return render_template("remove.html", name1 = name1, inputs = inputs)
    #print(buton)
    if len(name1) != 0 and buton[0:3] == "OUT":
        name1.pop(int(buton[3:]))
        status.pop(int(buton[3:]))
        aux_name.pop(int(buton[3:]))
        nod = nod - 1
        
    if len(inputs) != 0 and buton[0:2] == "IN":
        inputs.pop(int(buton[2:]))
        status_in.pop(int(buton[2:]))
        aux_input.pop(int(buton[2:]))
        noin = noin - 1    
    #print("VAL BUTON: "+buton)
    return render_template("ledon.html", name1 = name1, status = status, inputs = inputs, status_in = status_in)

# Read sensor readings and return as JSON
@app.route("/led=on", methods = ['POST', 'GET'])
async def led(request):
    global name1
    global status
    global nod
    aux_string = request.form
    buton = aux_string["name"]
    
    if buton == "ADD":
        return render_template("index.html")
    if buton == "RMV":
        return render_template("remove.html", name1 = name1, inputs = inputs)
    index = int(buton)
    if name1[index] != "LED":
        Pin(int(name1[index]), Pin.OUT).value(1)
        status[index] = 1
    else:
        Pin(name1[index], Pin.OUT).value(1)
        status[index] = 1
    
    return render_template("ledon.html",name1 = name1, status = status, inputs = inputs, status_in = status_in)

# Read sensor readings and return as JSON
@app.route("/led=off", methods = ['POST', 'GET'])
async def led(request):
    global nod
    global name1
    aux_string = request.form
    buton = aux_string["name"]
    
    if buton == "ADD":
        return render_template("index.html")
    if buton == "RMV":
        return render_template("remove.html", name1 = name1, inputs = inputs)
    index = int(buton)
    if name1[index] != "LED":
        Pin(int(name1[index]), Pin.OUT).value(0)
        status[index] = 0
    else:
        Pin(name1[index], Pin.OUT).value(0)
        status[index] = 0
    
    return render_template("ledon.html",name1 = name1, status = status, inputs = inputs, status_in = status_in)

# Shutdown the application
@app.route("/shutdown")
async def shutdown(request):
    request.app.shutdown()
    return "The server is shutting down..."

# Static CSS/JSS
@app.route("/static/<path:path>")
def static(request, path):
    if ".." in path:
        # directory traversal is not allowed
        return "Not found", 404
    return send_file("static/" + path)


if __name__ == "__main__":
    try:
        app.run()
    except KeyboardInterrupt:
        pass

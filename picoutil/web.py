from adafruit_httpserver.mime_type import MIMEType
from adafruit_httpserver.request import HTTPRequest
from adafruit_httpserver.response import HTTPResponse
from adafruit_httpserver.server import HTTPServer

from picoutil.wifi import connect
import wifi 
import board

from picolights.controller import Controller
from picolights.effects import color_chase, rainbow_cycle, blend

pool = connect()
server = HTTPServer(pool)


controller = Controller(pixel_pin=board.GP21, num_pixels=300, brightness=0.3, auto_write=False)

current_color = 0
requested_color = 213


@server.route("/")
def base(request: HTTPRequest):
    """
    Serve the default index.html file.
    """
    global requested_color
    color = request.query_params.get("color")
    if color:
        # color = color.replace("%2C", ",")
        # color = [int(x) for x in color.split(",", 3)]
        requested_color = int(color)
    with HTTPResponse(request, content_type=MIMEType.TYPE_HTML) as response:
        response.send_file("index.html")



print(f"Listening on http://{wifi.radio.ipv4_address}:80")
# server.serve_forever(str(wifi.radio.ipv4_address))
server.start(str(wifi.radio.ipv4_address))


while True:
    try:
        # Do something useful in this section,
        # for example read a sensor and capture an average,
        # or a running total of the last 10 samples

        # Process any waiting requests
        if current_color != requested_color:
            blend(controller, requested_color)
            current_color = requested_color

        server.poll()
    except OSError as error:
        print(error)
        continue
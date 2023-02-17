# SPDX-FileCopyrightText: 2018 Kattni Rembor for Adafruit Industries
#
# SPDX-License-Identifier: MIT

"""CircuitPython Essentials NeoPixel example"""
import time
import board
from rainbowio import colorwheel
from picolights.controller import Controller
from picolights.effects import color_chase, rainbow_cycle
from picolights.colors import RED, GREEN, BLUE

import socketpool
import wifi
import secrets


from adafruit_httpserver.mime_type import MIMEType
from adafruit_httpserver.request import HTTPRequest
from adafruit_httpserver.response import HTTPResponse
from adafruit_httpserver.server import HTTPServer
from adafruit_httpserver.methods import HTTPMethod


ssid, password = secrets.WIFI_SSID, secrets.WIFI_PASSWORD  # pylint: disable=no-member


print("Connecting to", ssid)
wifi.radio.connect(ssid, password)
print("Connected to", ssid)

print("My IP address is", wifi.radio.ipv4_address)

pool = socketpool.SocketPool(wifi.radio)
server = HTTPServer(pool)

controller = Controller(pixel_pin=board.GP21, num_pixels=300, brightness=0.3, auto_write=False)


@server.route("/")
def base(request: HTTPRequest):
    """
    Serve the default index.html file.
    """
    color = request.query_params.get("color")
    if color:
        color = color.replace("%2C", ",")
        color = [int(x) for x in color.split(",", 3)]
        color_chase(controller, color)
    with HTTPResponse(request, content_type=MIMEType.TYPE_HTML) as response:
        response.send_file("index.html")



print(f"Listening on http://{wifi.radio.ipv4_address}:80")
server.serve_forever(str(wifi.radio.ipv4_address))


# pixels = controller.pixels


# while True:
#     pixels.fill(RED)
#     pixels.show()
#     # Increase or decrease to change the speed of the solid color change.
#     time.sleep(1)
#     pixels.fill(GREEN)
#     pixels.show()
#     time.sleep(1)
#     pixels.fill(BLUE)
#     pixels.show()
#     time.sleep(1)

#     color_chase(controller, RED)  # Increase the number to slow down the color chase
#     # color_chase(YELLOW, 0)
#     color_chase(controller, GREEN)
#     # color_chase(CYAN, 0)
#     color_chase(controller, BLUE)
#     # color_chase(PURPLE, 0)

#     for _ in range(5):
#         rainbow_cycle(controller)  # Increase the number to slow down the rainbow

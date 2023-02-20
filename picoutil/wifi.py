# SPDX-FileCopyrightText: 2022 Liz Clark for Adafruit Industries
#
# SPDX-License-Identifier: MIT

import os
import time
import ssl
import wifi
import socketpool
import microcontroller
import adafruit_requests
import secrets

#  adafruit quotes URL
quotes_url = "https://www.adafruit.com/api/quotes.php"


__pool = None

def connect():
    global __pool
    if __pool is None:          
        ssid, password = secrets.WIFI_SSID, secrets.WIFI_PASSWORD  # pylint: disable=no-member
        wifi.radio.connect(ssid, password)
        print("My IP address is", wifi.radio.ipv4_address)
        __pool = socketpool.SocketPool(wifi.radio)
    return __pool


def get_quote():
        pool = connect()
        requests = adafruit_requests.Session(pool, ssl.create_default_context())

        #  pings adafruit quotes
        print("Fetching text from %s" % quotes_url)
        #  gets the quote from adafruit quotes
        response = requests.get(quotes_url)
        print("-" * 40)
        #  prints the response to the REPL
        print("Text Response: ", response.text)
        print("-" * 40)
        response.close()

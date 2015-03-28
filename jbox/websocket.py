#!/usr/bin/python

import json
import cherrypy
from ws4py.websocket import WebSocket
from jbox.core import volume

class JBoxWebSocket(WebSocket):
    def opened(self):
        cherrypy.log("WebSocket now ready")

    def closed(self, code=1000, reason="Burp, done!"):
        cherrypy.log("WebSocket terminated with reason '%s'" % reason)

    def received_message(self, msg):
        cherrypy.log("WebSocket Received message: %s" % msg)


#!/usr/bin/python

import json
import cherrypy
from ws4py.websocket import WebSocket

class JBoxWebSocket(WebSocket):
    volume = None

    def opened(self):
        cherrypy.log("WebSocket now ready")

    def closed(self, code=1000, reason="Burp, done!"):
        cherrypy.log("WebSocket terminated with reason '%s'" % reason)

    def received_message(self, msg):
        if self.volume:
            data = json.loads(str(msg))
            self.volume.set_level(data['level'])
        cherrypy.log("WebSocket Received message: %s" % msg)


#!/usr/bin/env python
# Copyright (C) 2001 Colin Svingen
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the
# Free Software Foundation, Inc., 59 Temple Place - Suite 330,
# Boston, MA 02111-1307, USA.
import os
import cherrypy
from ws4py.server.cherrypyserver import WebSocketPlugin, WebSocketTool

from jbox import websocket, volume_thread
from jbox.core import config, volume
from jbox.player import player
from jbox.services import songs, controls, nowplaying, directories, \
        applications

JBOX_CONF = config.Config('jbox.conf')

volume = volume.Volume(JBOX_CONF) 
play = player.Player(JBOX_CONF)
vol_thread = volume_thread.VolumeThread(volume)

class Root(object):
    @cherrypy.expose
    def ws(self):
        socket = cherrypy.request.ws_handler
        socket.volume = volume
        vol_thread.websocket = socket

CONF = {
        '/': {
            'tools.staticdir.root': os.path.abspath(os.getcwd()),
            'tools.staticdir.on': True,
            'tools.staticdir.dir': 'site',
            'tools.staticdir.index': 'index.html'

        },
        '/ws': {
            'tools.websocket.on': True,
            'tools.websocket.handler_cls': websocket.JBoxWebSocket
        }
        
}
SETUP = {'/': {'request.dispatch': cherrypy.dispatch.MethodDispatcher()}}
    
#    cherrypy.config.update({'server.socket_port': 9000})
WebSocketPlugin(cherrypy.engine).subscribe()
cherrypy.tools.websocket = WebSocketTool()

cherrypy.tree.mount(songs.Songs(), '/api/songs', SETUP)
cherrypy.tree.mount(volume, '/api/volume', SETUP)
cherrypy.tree.mount(controls.Controls(play), '/api/controls', SETUP)
cherrypy.tree.mount(nowplaying.NowPlaying(), '/api/nowplaying', SETUP)
cherrypy.tree.mount(directories.Directories(), '/api/directories', SETUP)
cherrypy.tree.mount(applications.Applications(), '/api/applications', SETUP)

cherrypy.engine.subscribe('start', vol_thread.start)
cherrypy.engine.subscribe('stop', vol_thread.join)

cherrypy.quickstart(Root(), '/', CONF)


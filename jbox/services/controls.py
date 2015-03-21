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
import cherrypy

class Controls(object):
    exposed = True

    def __init__(self, player):
        self.player = player
        self.data = None

    @cherrypy.tools.json_in()
    def POST(self):
        self.data = cherrypy.request.json
        if 'command' not in self.data:
            raise cherrypy.HTTPError(400, "Expected 'command'")
        else:
            self.handle(self.data['command'])

    def handle(self, cmd):
        if cmd == 'play':
            if 'id' in self.data:
                songid = self.data['id']
                self.player.play(cmd, songid)
            else:
                raise cherrypy.HTTPError(400, "Expected 'id'")
        elif cmd == 'stop':
            self.player.stop()
        elif cmd == 'next':
            self.player.next()
        elif cmd == 'previous':
            self.player.previous()
        elif cmd == 'pause':
            self.player.pause()
        elif cmd == 'quit':
            # Quit
            pass
        else:
            cherrypy.HTTPError(400, "Invalid command '{0}'".format(cmd))



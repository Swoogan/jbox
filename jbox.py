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
from jbox.core import config
from jbox.player import player
from jbox.services import songs, volume, controls, nowplaying, directories, \
        applications

class Root(object):
    pass


if __name__ == '__main__':
    CONF = {
            '/': {
                'tools.staticdir.root': os.path.abspath(os.getcwd()),
                'tools.staticdir.on': True,
                'tools.staticdir.dir': 'site',
                'tools.staticdir.index': 'index.html'

            },
    }
    SETUP = {'/': {'request.dispatch': cherrypy.dispatch.MethodDispatcher()}}
    
    JBOX_CONF = config.Config('jbox.conf')

    play = player.Player(JBOX_CONF)

    cherrypy.tree.mount(songs.Songs(), '/api/songs', SETUP)
    cherrypy.tree.mount(volume.Volume(JBOX_CONF), '/api/volume', SETUP)
    cherrypy.tree.mount(controls.Controls(play), '/api/controls', SETUP)
    cherrypy.tree.mount(nowplaying.NowPlaying(), '/api/nowplaying', SETUP)
    cherrypy.tree.mount(directories.Directories(), '/api/directories', SETUP)
    cherrypy.tree.mount(applications.Applications(), '/api/applications', SETUP)
    cherrypy.quickstart(Root(), '/', CONF)


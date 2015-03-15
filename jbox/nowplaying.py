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
import sys
import cherrypy
from . import jsonfile

class NowPlaying(object):
    exposed = True

    @cherrypy.tools.json_out()
    def GET(self):
        filename = 'nowplaying.json'

        return {'id': 10, 'length': 0, 'frequency': 48, 'bitrate': 128, 'artist': 'Headstones', 'title': 'Absolutely'}

        if not os.path.isfile(filename):
            return {}

        nowplaying = jsonfile.load(filename)

        songid, info = nowplaying.popitem()

        try:
            artist, title = info['song'].split(' - ', 1)
        except:
            title = info['song']
            artist = '&nbsp;'

        return {'id': songid, 'length': info['length'], 'frequency': info['frequency'], 'bitrate': info['bitrate'], 'artist': artist, 'title': title}


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
import re
import os.path
import cherrypy
from . import jsonfile

class Songs(object):
    exposed = True

    @cherrypy.tools.json_out()
    def GET(self, pattern = None):
        songs_file = 'songs.json'
        if not os.path.isfile(songs_file):
            return {}

        songs = jsonfile.load(songs_file)
        ordered = sorted(songs.items(), key=lambda s: s[1]['song'])
        songlist = {}

        for song in ordered:
            if pattern == None or re.compile(pattern, re.IGNORECASE).search(song[1]['song']):
                cherrypy.log(str(song))
                songlist[song[0]] = song[1]

        return songlist


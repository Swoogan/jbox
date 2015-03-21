#!/usr/bin/env python
# Copyright (C) 2015 Colin Svingen
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
from jbox.core import jsonfile

MIXER = 'mixer_path'
MPG123 = 'mpg123'

class Applications(object):
    config = 'jbox.conf'
    exposed = True

    @cherrypy.tools.json_out()
    def GET(self):
        data = jsonfile.load(self.config)
        mpg123 = data[MPG123] if MPG123 in data else ''
        mixer_path = data[MIXER] if MIXER in data else ''
        return {MPG123: mpg123, MIXER: mixer_path}

    @cherrypy.tools.json_in()
    def PUT(self):
        newdata = cherrypy.request.json
        data = jsonfile.load(self.config)

        if MPG123 in newdata:
            data[MPG123] = newdata[MPG123]

        if MIXER in newdata:
            data[MIXER] = newdata[MIXER]

        jsonfile.save(self.config, data)


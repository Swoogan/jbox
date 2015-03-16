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
from jbox.core import volume, jsonfile

class Volume(object):
    exposed = True
    vol = volume.Volume('jbox.conf')

    @cherrypy.tools.json_out()
    def GET(self):
        return {'level': self.vol.level()}

    @cherrypy.tools.json_in()
    def PUT(self):
        json = cherrypy.request.json
        self.vol.set_level(json['level'])
        

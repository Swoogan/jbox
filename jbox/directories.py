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
import os
from . import jsonfile
import cherrypy

class Directories(object):
  config = 'jbox.conf' 
  exposed = True

  @cherrypy.tools.json_out()
  def GET(self):
    data = jsonfile.load(self.config)
    dirs = data['directories'] if 'directories' in data else ''
    return dirs

  # TODO: This should be a POST and need to check to see if dir exists
  @cherrypy.tools.json_in()
  def PUT(self):
    newdata = cherrypy.request.json
    data = jsonfile.load(self.config)

    # if os.path.exists(new):
    #   data['directories'][new] = recurse
    
    if 'directories' in newdata:
      data['directories'] = newdata['directories']

    jsonfile.save(self.config, data)
  

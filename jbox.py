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

class Jbox(object):
    @cherrypy.expose
    def index(self):
        return "Hello World!"

if __name__ == '__main__':
    conf = {
            '/': {
                'tools.staticdir.root': os.path.abspath(os.getcwd())
            },
            '/html': {
                'tools.staticdir.on': True,
                'tools.staticdir.dir': 'html'
            },
            '/js': {
                'tools.staticdir.on': True,
                'tools.staticdir.dir': 'js'
            },
            '/images': {
                'tools.staticdir.on': True,
                'tools.staticdir.dir': 'images'
            },
            '/css': {
                'tools.staticdir.on': True,
                'tools.staticdir.dir': 'css'
            }
    }
    
    cherrypy.quickstart(Jbox(), '/', conf)


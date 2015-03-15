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
from jbox import applications
from jbox import directories
from jbox import songs

class Root(object):
#    @cherrypy.expose
#    def index(self):
#        return open('site/index.html', 'rt')
    pass


if __name__ == '__main__':
    conf = {
            '/': {
                'tools.staticdir.root': os.path.abspath(os.getcwd()),
                'tools.staticdir.on': True,
                'tools.staticdir.dir': 'site',
                'tools.staticdir.index': 'index.html'

            },
#            '/js': {
#                'tools.staticdir.on': True,
#                'tools.staticdir.dir': 'site/js'
#            },
#            '/images': {
#                'tools.staticdir.on': True,
#                'tools.staticdir.dir': 'site/images'
#            },
    }
    setup = {'/': {'request.dispatch': cherrypy.dispatch.MethodDispatcher()} }
    
    cherrypy.tree.mount(applications.Applications(), '/api/applications', setup) 
    cherrypy.tree.mount(directories.Directories(), '/api/directories', setup) 
    cherrypy.tree.mount(songs.Songs(), '/api/songs', setup) 
    cherrypy.quickstart(Root(), '/', conf)


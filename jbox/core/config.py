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
import re
import cherrypy
import subprocess
from jbox.core import jsonfile

class Config(object):
    def __init__(self, config):
        self.data = jsonfile.load(config)

    def mixer(self):
        return self.data['mixer_path'] if 'mixer_path' in self.data else ''

    def set_mixer(self, path):
        self.data['mixer_path'] = path


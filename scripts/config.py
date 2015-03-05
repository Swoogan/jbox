#!/usr/bin/env python3
# Copyright (C) 2001 Colin Svingen <swoogan@hotmail.com>
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
import cgi
import json
from utilities import template, jsonfile

form = cgi.FieldStorage()

config = os.path.join('..','jbox.conf') 
data = jsonfile.load(config)

if form:
  data['MPG123_PATH'] = form['MPG123_PATH'].value
  jsonfile.save(config, data)

tpl = os.path.join('templates','config.tpl')
print(template.populateTemplate(tpl, data))
  

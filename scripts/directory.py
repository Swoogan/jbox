#!/usr/bin/env python
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

import cgi, os, json
from utilities import template, parseconf

table = ''

config = os.path.join('..','jbox.conf') 
data = parseconf.load(config)

if 'directories' not in data:
  data['directories'] = {}

form = cgi.FieldStorage()

if form:
  if form.has_key('add') and form.has_key('newdir'):
    new = form['newdir'].value

    recurse = False

    if form.has_key('recurse'):
      recurse = True if form['recurse'].value == 'Y' else False

    if new not in data['directories']:
      if os.path.exists(new):
          data['directories'][new] = recurse
      else:
        table += '<p style="font-size: 14px; color: red;" align="center">ERROR: path \'' + new + '\' does not exist</p>'

  elif form.has_key('del.x') and form.has_key('path'):
    path = form['path'].value
    del data['directories'][path]

  parseconf.save(config, data)

table += '<table class="center" style="width: 85%" border cellspacing="0">\n'     \
        '<tr><th>Existing Directorys</th><th style="width: 120px">Recursive</th><th style="width: 100px">Delete</th></tr>\n'

for path in data['directories']: 
  recurse = str(data['directories'][path])
  table += '<tr><td style="text-align: left">' + path + '</td>\n'    \
           '<td>' + recurse + '</td>\n'  \
           '<td><form action="directory.py" method="post">'   \
           '<input type="hidden" name="path" value="' + path + '">'  \
           '<input type="image" src="../images/delete.png" name="del" value="Delete"></td></form></tr>\n'

table += '</table>\n'

tags = {'TABLE':table}
print template.populateTemplate(os.path.join('templates','directory.tpl'), tags)


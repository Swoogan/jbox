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

import cgi, sys, os, flatdb
from utilities import template

table = ''

songdb = flatdb.Database()

try:
  songdb.connect(os.path.join('data','songdb'))
except flatdb.DBError:
  songdb.create(os.path.join('data','songdb'))
  songdb.createTable('Dirs',['ID','DIR','RECURSIVE'])

form = cgi.FieldStorage()
if form:
  if form.has_key('add') and form.has_key('newdir'):
    new = form['newdir'].value
    if form.has_key('recurse'):
      recurse = form['recurse'].value
    else:
      recurse = 'N'
    if os.path.exists(new):
      songdb.getTable('Dirs').insert([new,recurse])
    else:
      table += '<p style="font-size: 14px; color: red;" align="center">ERROR: path \'' + new + '\' does not exist</p>'
  elif form.has_key('del.x') and form.has_key('id'):
    dirid = form['id'].value
    try:
      songdb.getTable('Dirs').delete(dirid)
    except flatdb.TableError:
      pass

  songdb.commit()


table += '<table align="center" cellspacing="0" border width="80%">\n'     \
         '<tr align="center"><td>Existing Directorys</td><td>Recursive</td><td>Delete</td></tr>\n'
for directory in songdb.getTable('Dirs').getIds():
  dirinfo = songdb.getTable('Dirs').getRowById(directory)
  table += '<tr><td>' + dirinfo['DIR'] + '</td>\n'    \
           '<td align="center">' + dirinfo['RECURSIVE'] + '</td>\n'  \
           '<td align="center"><form action="directory.py" method="post">'   \
           '<input type="hidden" name="id" value="' + dirinfo['ID'] + '">'  \
           '<input type="image" src="../images/delete.png" name="del" value="Delete"></td></form></tr>\n'

table += '</table>\n'

tags = {'TABLE':table}
print template.populateTemplate(os.path.join('templates','directory.tpl'),tags)


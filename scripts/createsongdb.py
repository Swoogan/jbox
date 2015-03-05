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

from utilities import template, jsonfile, songdb
import os.path

songs_file = 'songs.json'

songlist = songdb.getSongs()
output = {}
html = ''

for directory in songlist:
  html += '<tr><td colspan=2><h2>Processing ' + directory + ':</h2></td></tr>\n'
  if len(songlist[directory]) == 0:
    html += '<tr><td width=20></td><td>No mp3s found</td></tr>\n'
    continue

  output.update(songlist[directory])

  for index in songlist[directory]:
    song = songlist[directory][index]
    html += '<tr><td width=20></td></tr><tr><td width=30></td><td>"' + song['path'] + '" added</td></tr>\n'

jsonfile.save(songs_file, output)

tags = {'TABLE_CONTENTS': html}
tpl = os.path.join('templates', 'createsongdb.tpl')
print(template.populateTemplate(tpl, tags))

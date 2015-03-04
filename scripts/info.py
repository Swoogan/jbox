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

import sys, os 
from utilities import template, jsonfile

sys.stderr = sys.stdout

filename = 'nowplaying.json'

if not os.path.isfile(filename):
  print 'Content-type: text/html\n\n<html>\n<META http-equiv="pragma" content="no-cache">\n<META HTTP-EQUIV="Refresh" CONTENT="15">\n<body bgcolor=black></body>\n</html>'
  sys.exit()

nowplaying = jsonfile.load(filename)

songid = nowplaying.keys()[0]
info = nowplaying.values()[0]

try:
  artist, title = info['song'].split(' - ', 1)
except:
  title = info['song']
  artist = '&nbsp;'

tags = {'ID': songid, 'LENGTH': info['length'], 'FREQUENCY': info['frequency'], 'BITRATE': info['bitrate'], 'ARTIST': artist, 'TITLE': title}
print template.populateTemplate(os.path.join('templates','info.tpl'),tags)


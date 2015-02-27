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

import flatdb, sys, os, mp3info
from utilities import template

sys.stderr = sys.stdout

try:
  fh = open(os.path.join('data','nowplaying'),'r')
  songid = fh.read()
  fh.close()
except IOError, msg:
  #print >> sys.stderr, msg
  print 'Content-type: text/html\n\n<html>\n<META http-equiv="pragma" content="no-cache">\n<META HTTP-EQUIV="Refresh" CONTENT="15">\n<body bgcolor=black></body>\n</html>'
  sys.exit()

songdb = flatdb.Database()
try:
  songdb.connect(os.path.join('data','songdb'))
  row = songdb.getTable('Songs').getRowById(songid)
  songpath = row['PATH']
  song = row['SONG']
  length = row['LENGTH']
except (flatdb.DBError, flatdb.TableError), err:
  print err
  print 'Content-type: text/html\n\n<html>\n<META http-equiv="pragma" content="no-cache">\n<META HTTP-EQUIV="Refresh" CONTENT="15">\n<body bgcolor=black></body>\n</html>'
  sys.exit()

try:
  artist, title = song.split(' - ', 1)
except:
  title = song
  artist = '&nbsp;'


mp3file = mp3info.Mp3(songpath)
info = mp3file.getInfo()
mp3file.close()
if info:
  bitrate = info['bitrate']
  frequency = info['frequency']
else:
  bitrate, frequency = '?','?'


tags = {'LENGTH':length,'FREQUENCY':frequency,'BITRATE':bitrate,'ARTIST':artist,'TITLE':title,'ID':songid}
print template.populateTemplate(os.path.join('templates','info.tpl'),tags)


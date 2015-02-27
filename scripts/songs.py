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
import sys, cgi, os, re, flatdb
from utilities import template

songdb = flatdb.Database()
form = cgi.FieldStorage()
songlist = ''
lengthlist = ''
dir_out = ''

if form.has_key('pattern'):
  pattern = form['pattern'].value
else:
  pattern = None

try:
  songdb.connect('data/songdb')
except flatdb.DBError:
  songlist += '<TR><TD align=center colspan=2 ' + AR_LI_CELL + '><FONT ' + AR_LI_FONT + '><B>Error: The database does not currently '           \
         'contain any directorys </B></font></TD></tr>'             \
         '<tr><td align=center colspan=2 ' + AR_LI_CELL + '><b><a href="admin.html" target="_top">Add songs</a></b></td></tr>'
else:
  for dirid in songdb.getTable('Dirs').getIds():
    songs = songdb.getTable('Songs').getRowsByValue({'DIR_ID' : dirid})
    songs.sort(lambda x, y: cmp(x['SONG'].lower(),y['SONG'].lower()))
    for row in songs:
      if pattern:
        if re.compile(pattern, re.IGNORECASE).search(row['SONG']):
          songlist += '<a href="javascript:void(0)" onclick="javascript:clicked(\'cmd=L&id=' + row['ID'] + '\')"' \
                      ' name="' + row['ID'] + '">' + row['SONG'][:54] + '</a><br>\n'
          lengthlist += row['LENGTH'] + '<br>\n'
      else:
        songlist += '<a href="javascript:void(0)" onclick="javascript:clicked(\'cmd=L&id=' + row['ID'] + '\')"' \
                    ' name="' + row['ID'] + '">' + row['SONG'][:54] + '</a><br>\n'
        lengthlist += row['LENGTH'] + '<br>\n'


tags = {'SONGS' : songlist, 'LENGTHS':lengthlist}

if pattern:
  print template.populateTemplate(os.path.join('templates','songs.tpl'), tags)
else:
  try:
    #need to add a mode here so that the file isn't created as 600 instead of 644
    fh = open('songs.html','w')
    fh.write(template.populateTemplate(os.path.join('templates','songs.tpl'), tags, online=0))
    fh.close
  except IOError, msg:
    print >> sys.stderr, msg

  print 'Content-type: text/html\n\n'     \
        '<html><body style="background: black; color: white;"><p align="center" style="font-family: Verdana,Geneva,Arial,Times;">Song page created successfully</p></body></html>'


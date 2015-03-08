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
import sys, cgi, os, re
from utilities import template, jsonfile

def generate(songs, pattern = None):
  songlist = ''
  lengthlist = ''

  for song in songs:
    if not pattern or re.compile(pattern, re.IGNORECASE).search(song[1]['song']):
      songlist += '<a href="javascript:void(0)" onclick="javascript:clicked(\'cmd=L&id=' + song[0] + '\')"' \
                  ' name="' + song[0] + '">' + song[1]['song'][:54] + '</a><br>\n'
      lengthlist += str(song[1]['length']) + '<br>\n'

  return {'SONGS': songlist, 'LENGTHS': lengthlist}
  

songs_file = 'songs.json'

if not os.path.isfile(songs_file):
  error = '<tr><td style="text-align: center" colspan=2><b>'  \
            'Error: The database does not currently contain any songs'    \
          '</b></td></tr>'  \
          '<tr><td style="text-align: center" colspan=2><b><a href="config.html" target="_top">Add songs</a></b></td></tr>'
  print(template.populateTemplate(os.path.join('templates','songs.tpl'), {'SONGS': error}))
  sys.exit()
  
songs = jsonfile.load(songs_file)
ordered = sorted(songs.items(), key=lambda s: s[1]['song'])

form = cgi.FieldStorage()

if 'pattern' in form:
  tags = generate(ordered, form['pattern'].value)
  print(template.populateTemplate(os.path.join('templates','songs.tpl'), tags))
else:
  tags = generate(ordered)

  try:
    #need to add a mode here so that the file isn't created as 600 instead of 644
    fh = open('songs.html','w')
    fh.write(template.populateTemplate(os.path.join('templates','songs.tpl'), tags, online=0))
    fh.close
  except IOError as msg:
    print(msg, file=sys.stderr)

  print('Content-type: text/html\n\n'     \
        '<html><body style="background: black; color: white;">' \
        '<p align="center" style="font-family: Verdana,Geneva,Arial,Times;">The static song page was created successfully.</p>' \
        '</body></html>')


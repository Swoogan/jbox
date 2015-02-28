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
import sys, os, time, flatdb, mp3info
from utilities import template

def walktree(path, dirid, recurse):
  output = ''
  has_mp3s = 0
  if os.path.exists(path):
    dirs = os.listdir(path)

    for item in dirs:
      if item[-4:].lower() == '.mp3':
        fullpath = os.path.join(path, item)
        mp3file = mp3info.Mp3(fullpath)
        info = mp3file.getInfo()
        mp3file.close()

        if info:
          print info
          length = info['seconds']
        else:
          length = '0'


        songdb.getTable('Songs').insert([dirid,item[:-4],fullpath,length])
        output += '<tr><td width=20></td></tr><tr><td width=30></td><td>"' + item + '" added</td></tr>\n'
        has_mp3s = 1

    if not has_mp3s:
      output += '<tr><td width=20></td><td>No mp3s found</td></tr>\n'

    if recurse == 'Y':
      for item in dirs:
        fullpath = os.path.join(path, item)
        if os.path.isdir(fullpath) and item[:2] is not '..':
          output += '<tr><td colspan=2><b>Recending into subdirectory ' + item + ':</b></td></tr>\n'
          output += walktree(fullpath, dirid, recurse)

  else:
    output += '<tr><td width=20></td><td>Directory does not exist</td></tr>\n'

  return output



db = os.path.join('data','songdb')
songdb = flatdb.Database()
try:
  songdb.connect(db)
  songdb.getTable('Songs').truncate()
except flatdb.DBError:
#  songdb.create(db)
  songdb.createTable('Songs',['ID','DIR_ID','SONG','PATH','LENGTH'])

output = ''
for dirid in songdb.getTable('Dirs').getIds():
  directory = songdb.getTable('Dirs').getRowById(dirid)
  output += '<tr><td colspan=2><font size=+1><b>Processing ' + directory['DIR'] + ':</b></font></td></tr>\n'
  output += walktree(directory['DIR'],directory['ID'],directory['RECURSIVE'])

try:
  songdb.commit()
except flatdb.TableError, err:
  print >> sys.stderr, err


tags = {'TABLE_CONTENTS':output}
print template.populateTemplate(os.path.join('templates','createsongdb.tpl'),tags)


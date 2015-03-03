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
import os
import mp3info
import fnmatch

from utilities import template, jsonfile

def findMp3s(path, recurse):
  songs = {}
  index = 0

  for root, dirs, files in os.walk(path):
    for name in fnmatch.filter(files, '*.mp3'):
      fullpath = os.path.join(root, name)

      mp3file = mp3info.Mp3(fullpath)
      info = mp3file.getInfo()
      mp3file.close()

      length = info['seconds'] if info else '0'
      songs[index] = {'song': name[:-4], 'path': fullpath, 'length': length}
      index += 1

    if not recurse:
      break

  return songs

def getSongs():
  config = os.path.join('..', 'jbox.conf') 
  data = jsonfile.load(config)

  songs = {}

  for path in data['directories']:
    recurse = data['directories'][path]
    songs[path] = findMp3s(path, recurse)

  return songs

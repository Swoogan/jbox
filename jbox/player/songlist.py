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
import os
import sys
import random
from jbox.core import jsonfile

#sys.stdout = sys.stderr

class Songlist(object):
    def __init__(self):
        self.songdb = jsonfile.load('songs.json')
        self.cursong = os.path.join('nowplaying.json')
        size = len(self.songdb)
        self.last = size - 1
        self.random = list(range(size))
        random.shuffle(self.random)
        self.index = 0

    def select(self, songid):
        try:
            index = int(songid)
            self.index = self.random.index(index)
#            print("Select: index " + songid + " self.index " + str(self.index))
        except ValueError:
#            print("ValueError, calling next")
            return self.next()

        while True:
            path = self.songdb[str(index)]['path']

            if os.path.exists(path):
                self.save()
                return path

            self.index += 1

            if self.index > self.last:
                self.index = 0

            index = self.random[self.index]

    def next(self):
        while True:
            self.index += 1

            if self.index > self.last:
                self.index = 0

#            print('Next: index: {0}, last: {1}:'.format(self.index, self.last))

            return str(self.random[self.index])

    def previous(self):
        while True:
            self.index -= 1

            if self.index < 0:
                self.index = self.last

#            print('Previous: index: {0}, last: {1}:'.format(self.index, self.last))

            return str(self.random[self.index])

    def save(self):
        i = str(self.random[self.index])
        info = self.songdb[i]
        song = {i: info}
        try:
            jsonfile.save('nowplaying.json', song)
#            print('Wrote: ' + info['song'] + ' to nowplay.json')
        except IOError as msg:
            print(msg, file=sys.stderr)


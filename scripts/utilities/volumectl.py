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
import sys, os, parseconf

config = os.path.join('..', 'jbox.conf') 
#try:
data = parseconf.load(config)
#except IOError:
#  pass

class Volume:
  def __init__(self):
    self.level = 50
    self.pixel = 129

    if 'volume' not in data:
      data['volume'] = {}
    else:
      self.load()

  def load(self):
    self.pixel = data['volume']['pixel']
    self.level = int(data['volume']['level'])

  def save(self):
    try:
      data['volume']['pixel'] = self.pixel
      data['volume']['level'] = self.level

      parseconf.save(config, data)
    except IOError, msg:
      print >> sys.stderr, msg

  def setVol(self, volume):
    self.level = volume

  def setPixel(self, pixel):
    self.pixel = pixel

  def getPixel(self):
    return self.pixel

  def changeVolume(self):
    try:
      aumix_path = data['AUMIX_PATH']
    except IOError:
      print >> sys.stderr, 'Could not find jbox.conf'
    except KeyError:
      print >> sys.stderr, 'Could not get mpg123 path from jbox.conf'

    #change the system volume
    os.system('%s -v %s' % (aumix_path, self.level))

if __name__ == '__main__':
  vol = Volume()
  vol.save()
  print vol.level


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

def hashFromConf(filename):
  confhash = {}
  file = open(filename,'r')
  for line in file.readlines():
    name,value = line.split('=',1)
    if value[-1] == '\n' or value[-1] == '\r\n':
      value = value[:-1] #strip off the '\n' on the end
    confhash.update({name : value})
  file.close()
  return confhash


if __name__ == '__main__':
  print hashFromConf('../../jbox.conf')                    


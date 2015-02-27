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

from types import StringType
import sys, os


class TemplateError:
  def __init__(self, msg):
    self.error = msg
  def __str__(self):
    return self.error

def populateTemplate(filename, tags=None, online=1):
  if online:
    contents = 'Content-type: text/html\n\n'
  else:
    contents = ''

  try:
    file = open(filename,'r')
    contents += file.read()
    file.close()
    if tags:
      for name, value in tags.items():
        if type(name) is not StringType:
          name = repr(name)
        elif type(value) is not StringType:
          value = repr(value)

        contents = contents.replace('[[' + name + ']]',value)

    return contents
  except IOError:
    raise TemplateError, 'Template: ' + filename + ' was not found'


if __name__ == '__main__':
  print hashFromConf('../../jbox.conf')                                     


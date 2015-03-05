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
from __future__ import print_function
import cgi, sys, os

print('Content-type: text/html')

form = cgi.FieldStorage()

if form.has_key('cmd'):
  command = form['cmd'].value
  if form.has_key('id'):
    command += ' ' + form['id'].value

  #print('\n\n' + command + "<p>")

  try:
    if not os.path.exists(os.path.join('data','player.pipe')):
      raise IOError
    fifo = open(os.path.join('data','player.pipe'), 'w+')
    fifo.write(command)
    fifo.close()
  except IOError, msg:
    print('\nThe player is currently not running.  <a href="playerctl.py?cmd=start">Start the player</a><p>')
    print(msg)
    sys.exit()

else:
  print('Invalid query string: ' + repr(form.keys()), sys.stderr)

print('Status: 204 No Response\n')


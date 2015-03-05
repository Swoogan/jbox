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
from utilities import playerutils
import os
import sys
import cgi
import signal

os.environ.update({'HOME': '/home/jbox','PATH': '/bin:/usr/bin:/usr/local/bin:/usr/bin/X11:/usr/X11R6/bin:/usr/games'})

def interrupt_handler(signal, frame):
  sys.exit()

def stop():
  try:
    if not os.path.exists(os.path.join('data','player.pipe')):
      raise IOError

    fh = open(os.path.join('data', 'player.pipe'), 'w+')
    fh.write('Q')
    fh.close()
  except IOError:
    print('Player already stopped', file=sys.stderr)

def start():
  if os.path.exists(os.path.join('data', 'player.pipe')):
    print('Player already started', file=sys.stderr)
  else:
    try:
      os.system('python player.py >> ' + os.path.join('data','player.log') + ' 2>&1 &')
    except OSError, msg:
      print(msg, file=sys.stderr)

#print(os.environ, file=sys.stderr) 

form = cgi.FieldStorage()
if form:
  if form.has_key('cmd'):
    cmd = form['cmd'].value
  else:
    print('Invalid usage. Must pass cmd == [start|stop|restart]', file=sys.stderr)
    sys.exit()

  print 'Content-type: text/html\nStatus: 204 No Response\n'

else:
  if len(sys.argv) < 2:
    print 'Usage: ' + sys.argv[0] + ' [start|stop|restart]'
    sys.exit()
  else:
    cmd = sys.argv[1]


if cmd == 'start':
  start()

elif cmd == 'stop':
  stop()

elif cmd == 'restart':
  stop()
  start()


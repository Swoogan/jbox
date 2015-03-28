#!/usr/bin/env python
# Copyright (C) 2015 Colin Svingen
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
import time, json, threading

class SongComplete(threading.Thread):
    def __init__(self, mpg123, done):
        super(SongComplete, self).__init__()
        self.stoprequest = threading.Event()
        self.mpg123 = mpg123
        self.done = done

    def run(self):
        while not self.stoprequest.isSet():
            message = self.mpg123.recv()
            if message and message[:-1] == '@P 0':
                self.done.put("done")

            #time.sleep(0.2)

    def join(self, timeout=None):
        self.stoprequest.set()
        super(SongComplete, self).join(timeout)


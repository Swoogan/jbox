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
import sys
import subprocess

class MpgWrap(object):
    def __init__(self, config):
        self.input = None
        self.output = None
        self.config = config

    def open_mpg(self):
        mpg123 = self.config.mpg123()
        proc = subprocess.Popen([mpg123, '-b 0', '-R'], stdin=subprocess.PIPE, \
                stdout=subprocess.PIPE, universal_newlines=True)
        (self.input, self.output) = (proc.stdout, proc.stdin)

    def send(self, command):
        try:
            self.output.write(command + '\n')
            self.output.flush()
        except IOError as msg:
            print('Error writing to mp3 player: ' + str(msg), file=sys.stderr)
            self.open_mpg()
            self.send(command)

    def recv(self):
        return self.input.readline()

    def quit(self):
        self.send('Q')

        try:
            self.input.close()
            self.output.close()
        except IOError as msg:
            print(msg, file=sys.stderr)


#!/usr/bin/env python
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

class MpgWrap:
    def __init__(self, mpg123):
        self.mpg123 = mpg123
        self.input = None
        self.output = None

    def run(self):
        try:
            proc = subprocess.Popen([self.mpg123, '-b 0', '-R'], stdin=subprocess.PIPE, \
                    stdout=subprocess.PIPE, universal_newlines=True)
            (self.input, self.output) = (proc.stdout, proc.stdin)
        except OSError:
            print('Could not open mpg123 for playing', file=sys.stderr)

    def send(self, cmd):
        try:
            self.output.write(cmd + '\n')
            self.output.flush()
        except IOError as msg:
            print('Error writing to mp3 player: ' + str(msg), file=sys.stderr)
            self.open_mpg()
            self.send(cmd)
        except ValueError:
            pass

    def recv(self):
        return self.input.readline()

    def quit(self):
        self.send('Q')

        try:
            self.input.close()
            self.output.close()
        except IOError as msg:
            print(msg, file=sys.stderr)

if __name__ == '__main__':
    mpg = MpgWrap('/usr/bin/mpg123')
    mpg.run()
    mpg.quit()

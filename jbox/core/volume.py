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
import os
import re
import subprocess
from jbox.core import config

class Volume(object):
    def __init__(self, conf):
        self.mixer = conf.mixer()

    def level(self):
        if os.path.isfile(self.mixer):
            cmd = [self.mixer, '-M', '-c', '0', 'get', 'Master', 'playback']
            result = subprocess.check_output(cmd)
            match = re.search('([0-9]+)%', result.decode('utf-8'))
            return match.group(1)
        else:
            print("Mixer path '{0}' seems to be invalid".format(self.mixer)) #, file=sys.stderr)

    def set_level(self, level):
        if os.path.isfile(self.mixer):
            cmd = [self.mixer, '-M', '-c', '0', 'set', 'Master', 'playback', '{0}%'.format(level)]
            with open(os.devnull, 'wt') as null:
                subprocess.call(cmd, stdout=null)
        else:
            print("Mixer path '{0}' seems to be invalid".format(self.mixer)) #, file=sys.stderr)

if __name__ == '__main__':
    vol = Volume(config.Config('../../jbox.conf'))
    vol.set_level(50)
    print(vol.level())

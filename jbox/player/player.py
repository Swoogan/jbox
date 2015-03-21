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
import sys
import time
import traceback
import threading
from jbox.core import config
from jbox.player import mpgwrap
from jbox.player import songlist

class Player:
    def __init__(self, conf):
        self.cursong = os.path.join('nowplaying.json')
        self.songlist = songlist.Songlist()
        self.mpg123 = mpgwrap.MpgWrap(conf.mpg123())
        self.mpg123.run()
        self.paused = False

    def stop(self):
        self.mpg123.send('S')

        if os.path.exists(self.cursong):
            os.unlink(self.cursong)

    def quit(self):
        self.mpg123.quit()

    def pause(self):
        self.paused = not self.paused
        self.mpg123.send('P')

    def next(self):
        self.mpg123.send('LOAD ' + self.songlist.next())

    def previous(self):
        self.mpg123.send('LOAD ' + self.songlist.previous())

    def play(self, songid):
        try:
            self.mpg123.send('LOAD ' + self.songlist.select(songid))
        except ValueError:
            self.songlist.previous()

        thread = threading.Thread(target=self.song_complete)
#         thread.daemon = True
        thread.start()

    def song_complete(self):
        while True:
            # If the current song is done, skip to the next
            if not self.paused:
                message = self.mpg123.recv()
                if message and message[:-1] == '@P 0':
                    self.next()
                    break

            #time.sleep(0.2)


    def deinit(self):
        try:
            self.mpg123.quit()

            if os.path.exists(self.cursong):
                os.unlink(self.cursong)

            print('Player closed', file=sys.stderr)
        except IOError:
            print(traceback.print_exc(), file=sys.stderr)
            #raise player error

if __name__ == '__main__':
    player = Player(config.Config('jbox.conf'))
    player.play("1")
    try:
        player.play("1")
    finally:
        player.deinit()


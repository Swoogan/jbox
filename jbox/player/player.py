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

class CheckForStop(threading.Thread):
    def __init__(self, mpg123):
        super(CheckForStop, self).__init__()
        self._stop = threading.Event()
        self.mpg123 = mpg123

    def stop(self):
        self._stop.set()

    def stopped(self):
        return self._stop.is_set()

    def run(self):
        while not self.stopped():
            # If the current song is done, skip to the next
            if self.paused:
                continue

            message = self.mpg123.recv()
            if message and message[:-1] == '@P 0':
                self.next()
                break

class PlayerStates(object):
    PLAYING = 0
    PAUSED = 1
    SONG_COMPLETE = 2
    STOPPING = 3
    STOPPED = 4

class Player(object):
    def __init__(self, conf):
        self.cursong = os.path.join('nowplaying.json')
        self.songlist = songlist.Songlist()
        self.mpg123 = mpgwrap.MpgWrap(conf.mpg123())
        self.mpg123.run()
        self._state = PlayerStates.STOPPED
        self._stop = threading.Event()
        self.thread = None

    def stop(self):
        self.mpg123.send('S')

        if os.path.exists(self.cursong):
            os.unlink(self.cursong)

        self.stop_thread()

    def quit(self):
        self.mpg123.quit()
        self.do_stop()

    def pause(self):
        self.paused = not self.paused
        self.mpg123.send('P')

    def next(self):
        self.play(self.songlist.next())

    def previous(self):
        self.play(self.songlist.previous())

    def play(self, songid):
        self.stop_thread()

        try:
            self.mpg123.send('LOAD ' + self.songlist.select(songid))
        except ValueError:
            self.songlist.previous()

        self._state = PlayerStates.PLAYING

        self._stop.clear()
        self.thread = threading.Thread(target=self.song_complete)
        self.thread.start()

    def song_complete(self):
        while True:
            if self._state == PlayerStates.STOPPING:
                break
            elif self._state != PlayerStates.PLAYING:
                continue 

            message = self.mpg123.recv()
            if message and message[:-1] == '@P 0':
                self._state = PlayerStates.SONG_COMPLETE
                break

    def stop_thread(self):
        self._state = PlayerStates.STOPPING

        self._stop.set()
        if self.thread is not None:
            self.thread.join()

        self._state = PlayerStates.STOPPED

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
    try:
        player.play("1")
    finally:
        player.deinit()


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
import queue
import cherrypy
import traceback
import threading
from jbox.core import config
from jbox.player import mpgwrap, songlist, song_complete

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
        self.done = queue.Queue(1)
        self.thread = song_complete.SongComplete(self.mpg123, self.done)
        self.thread.start()

    def stop(self):
        self.mpg123.send('S')
        self._state = PlayerStates.STOPPED

        if os.path.exists(self.cursong):
            os.unlink(self.cursong)

    def pause(self):
        if self._state == PlayerStates.PAUSED:
            self._state = PlayerStates.PLAYING 
            self.mpg123.send('P')
        elif self._state == PlayerStates.PLAYING:
            self._state = PlayerStates.PAUSED 
            self.mpg123.send('P')

    def next(self):
        self.play(self.songlist.next())

    def previous(self):
        self.play(self.songlist.previous())

    def play(self, songid):
        self._state = PlayerStates.PLAYING

        while self._state == PlayerStates.PLAYING:
            try:
                self.mpg123.send('LOAD ' + self.songlist.select(songid))
            except ValueError:
                self.songlist.previous()
    
            while True:
                try:
                    done = self.done.get(True, 0.05)
                    break
                except queue.Empty:
                    continue

            songid = self.songlist.next()


    def stop_thread(self):
        cherrypy.log('Attempting to stop thread...')
        self._state = PlayerStates.STOPPING
        self.thread.join()
        self._state = PlayerStates.STOPPED
        cherrypy.log('Thread stopped')

    def deinit(self):
        self.stop_thread()

        try:
            self.mpg123.quit()

            if os.path.exists(self.cursong):
                os.unlink(self.cursong)

            cherrypy.log('Player closed')
        except IOError:
            print(traceback.print_exc(), file=sys.stderr)



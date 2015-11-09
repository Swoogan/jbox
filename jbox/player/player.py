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
import vlc
import time
import queue
import cherrypy
import traceback
import threading
from jbox.core import config
from jbox.player import mpgwrap, songlist, song_complete

class Player(object):
    def __init__(self, conf):
        self.cursong = os.path.join('nowplaying.json')
        self.songlist = songlist.Songlist()
        self.vlc = vlc.Instance()
        self.player = self.vlc.media_player_new()
        self.player.event_manager().event_attach(vlc.EventType.MediaPlayerEndReached, self.finished)

    def stop(self):
        self.player.stop()

        if os.path.exists(self.cursong):
            os.unlink(self.cursong)

    def pause(self):
        self.player.pause()

    def next(self):
        cherrypy.log('In next...')
        self.play(self.songlist.next())

    def previous(self):
        self.play(self.songlist.previous())

    def play(self, songid):
        try:
            cherrypy.log('In play...')
            path = 'file:///' + self.songlist.select(songid)
            cherrypy.log('In play... ' + path)
            media = self.vlc.media_new(path)
            cherrypy.log('In play... media')
            self.player.set_media(media)
            cherrypy.log('In play... set_media')
            result = self.player.play()
            cherrypy.log('Playing... ' + str(result))

        except ValueError:
            self.songlist.previous()
        except:
            cherrypy.log(traceback.print_exc())
    
    def finished(self, *args, **kwargs):
        cherrypy.log('Finished song...')
        self.player = self.vlc.media_player_new()
        self.player.event_manager().event_attach(vlc.EventType.MediaPlayerEndReached, self.finished)
        self.next()

    def deinit(self):
        try:
            if os.path.exists(self.cursong):
                os.unlink(self.cursong)

            cherrypy.log('Player closed')
        except IOError:
            print(traceback.print_exc(), file=sys.stderr)


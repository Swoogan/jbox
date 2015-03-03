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
import flatdb, os, sys, random, jsonfile
import traceback

#sys.stdout = sys.stderr

class Songlist:
  def __init__(self):
    self.songdb = flatdb.Database()
    try:
      self.songdb.connect(os.path.join('data','songdb'))
    except flatdb.DBError, err:
      print >> sys.stderr, err

    self.cursong = os.path.join('nowplaying.json')
    self.songlist = []
    self.song_index = 0
    self.max_index = 0
    self.refresh()

  def refresh(self, songid=0):
    try:
      self.songlist = self.songdb.getTable('Songs').getIds()
    except flatdb.TableError, msg:
      print >> sys.stderr, msg
    except KeyError:
      print >> sys.stderr, "The table 'Songs' doesn't seem to exist"
      sys.exit()

    try:
      songindex = self.songlist.index(songid)
      del self.songlist[songindex]
      random.shuffle(self.songlist)
      self.songlist.insert(0,songid)
      self.song_index = 0
      self.max_index = len(self.songlist) - 1
    except ValueError, msg:
      pass

  def next(self):
    done = 0
    while not done:
      if self.song_index > self.max_index:
        self.song_index = 0

      songpath = self.songdb.getTable('Songs').getRowById(self.songlist[self.song_index])['PATH']

      if os.path.exists(songpath):
        done = 1

      self.song_index += 1
    return songpath


  def previous(self):
    done = 0
    self.song_index -= 1
    while not done:
      self.song_index -= 1
      if self.song_index < 0:
        self.song_index = self.max_index

      songpath = self.songdb.getTable('Songs').getRowById(self.songlist[self.song_index])['PATH']
      #songpath = self.songdb.getTable('Songs').getRowById(wak)['PATH']

      if os.path.exists(songpath):
        done = 1

    self.song_index += 1
    return songpath

  def savecur(self, song):
    try:
      data = {'current': song}  
      jsonfile.save(self.cursong, data)
      print >> sys.stderr, 'Wrote: ' + song + ' to ' + self.cursong
    except IOError, msg:
      print >> sys.stderr, msg

class mpgWrap:
  def open_mpg(self):
    config = os.path.join('..','jbox.conf') 
    try:
      data = jsonfile.load(config)
      mpg_path = data['MPG123_PATH']
    except IOError:
      print >> sys.stderr, 'Could not find jbox.conf'
    except KeyError:
      print >> sys.stderr, 'Could not get mpg123 path from jbox.conf'
    else:
      try:
        self.output, self.input = os.popen2(mpg_path + ' -b 0 -R 0',0)
      except OSError:
        print >> sys.stderr, 'Could not open mpg123 for playing'

  def send(self, cmd):
    try:
      print >> sys.stderr, cmd
      self.output.write(cmd + '\n')
      #self.output.write(cmd)
      self.output.flush()
    except IOError, msg:
      print >> sys.stderr, 'Error writing to mp3 player: ' + str(msg)
      self.open_mpg()
      self.send(cmd)
    except ValueError:
      pass

  def recv(self):
    #print >> sys.stderr, "in recv"
    return self.input.readline()

  def quit(self):
    self.send('Q')

    try:
      self.input.close()
      self.output.close()
    except IOError, msg:
      print >> sys.stderr, msg


class Player:
  def __init__(self):
    self.pipenam = os.path.join('data','player.pipe')
    self.cursong = os.path.join('nowplaying.json')
    self.mpg123 = mpgWrap()
    self.mpg123.open_mpg()
    self.songlist = Songlist()
    self.paused = 0


  def init(self):
    if not os.path.exists(self.pipenam):
      try:
        os.mkfifo(self.pipenam)
      except OSError, msg:
        print >> sys.stderr, msg

    try:
      self.fifo = open(self.pipenam,'r')
    except:
      sys.exit()


  def play(self):
    command = self.fifo.readline()
    songid = '0'
    while 1:
      if len(command) > 0:
        cmmd = command[0].upper()

        print >> sys.stderr, "Command: " + cmmd

        if cmmd == 'Q':
          self.mpg123.quit()
          break

        elif cmmd == 'S':
          self.mpg123.send(cmmd)
          self.songlist.savecur(0)

        elif cmmd == 'P':
          if self.paused:
            self.paused = 0
          else:
            self.paused = 1
          self.mpg123.send(cmmd)

        elif cmmd == 'N':
          self.mpg123.send('LOAD ' + self.songlist.next())
          self.songlist.savecur()

        elif cmmd == 'V':
          self.mpg123.send('LOAD ' + self.songlist.previous())
          self.songlist.savecur()

        elif cmmd == 'U':
          self.mpg123.send('V ' + command[1:])

        elif cmmd == 'L':
          try:
            songid = command[command.index(' ')+1:]
            self.songlist.refresh(songid)
            self.mpg123.send('LOAD ' + self.songlist.next())
            self.songlist.savecur()
          except:
            self.songlist.previous()


      ##Cant read from the player when nothing is sent (eg: stops and pauses)
      if cmmd != 'S' and not self.paused:
        message = self.mpg123.recv()
        if message:
          if message[:-1] == '@P 0':
            self.mpg123.send('LOAD ' + self.songlist.next())
            self.songlist.savecur()

      command = self.fifo.readline()

    self.deinit()

  def deinit(self):
    try:
      self.mpg123.quit()
      try:
        self.fifo.close()
      except:
        pass

      if os.path.exists(self.pipenam):
        os.unlink(self.pipenam)
      if os.path.exists(self.cursong):
        os.unlink(self.cursong)

      print >> sys.stderr, 'Player closed'
    except:
      print >> sys.stderr, traceback.print_exc()
      #raise player error


if __name__ == '__main__':
  player = Player()
  try:
    player.init()
    player.play()
  finally:
    player.deinit()


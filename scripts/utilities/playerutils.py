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
import random
import traceback
import subprocess
from utilities import jsonfile

#sys.stdout = sys.stderr

class Songlist:
  def __init__(self):
    self.songdb = jsonfile.load('songs.json')
    self.cursong = os.path.join('nowplaying.json')
    size = len(self.songdb)
    self.last = size - 1
    self.random = list(range(size))
    random.shuffle(self.random)
    self.index = 0

  def select(self, songid):
    try:
      index = int(songid)
      self.index = self.random.index(index)
      print("index " + songid + " self.index " + str(self.index))
    except:
      return self.next()

    while True:
      path = self.songdb[str(index)]['path']

      if os.path.exists(path):
        self.save()
        return path

      self.index += 1

      if self.index > self.last:
        self.index = 0

      index = self.random[self.index]

  def next(self):
    while True:
      self.index += 1

      if self.index > self.last:
        self.index = 0

      print('index: {0}, last: {1}:'.format(self.index, self.last))

      index = self.random[self.index]
      path = self.songdb[str(index)]['path']

      if os.path.exists(path):
        self.save()
        return path

  def previous(self):
    while True:
      self.index -= 1

      if self.index < 0:
        self.index = self.last

      print('index: {0}, last: {1}:'.format(self.index, self.last))

      index = self.random[self.index]
      path = self.songdb[str(index)]['path']

      if os.path.exists(path):
        self.save()
        return path

  def save(self):
    i = str(self.random[self.index])
    info = self.songdb[i]
    song = {self.index: info}
    try:
      jsonfile.save('nowplaying.json', song)
      print('Wrote: ' + info['song'] + ' to nowplay.json')
    except IOError as msg:
      print(msg, file=sys.stderr)

class mpgWrap:
  def open_mpg(self):
    config = os.path.join('..','jbox.conf') 

    try:
      data = jsonfile.load(config)
      mpg_path = data['MPG123_PATH']
    except IOError:
      print('Could not find jbox.conf', file=sys.stderr)
    except KeyError:
      print('Could not get mpg123 path from jbox.conf', file=sys.stderr)
    else:
      try:
        p = subprocess.Popen([mpg_path, '-b 0', '-R'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True)
        (self.input, self.output) = (p.stdout, p.stdin)
      except OSError:
        print('Could not open mpg123 for playing', file=sys.stderr)

  def send(self, cmd):
    try:
      print('Got command ', cmd)
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


class Player:
  def __init__(self):
    self.pipenam = os.path.join('data','player.pipe')
    self.cursong = os.path.join('nowplaying.json')
    self.mpg123 = mpgWrap()
    self.mpg123.open_mpg()
    self.songlist = Songlist()
    self.paused = False

  def init(self):
    if not os.path.exists(self.pipenam):
      try:
        os.mkfifo(self.pipenam)
      except OSError as msg:
        print(msg, file=sys.stderr)

    try:
      self.fifo = open(self.pipenam,'rt')
    except:
      sys.exit()


  def play(self):
    command = self.fifo.readline()

    while True:
      if len(command) > 0:
        cmmd = command[0].upper()

        print("Command: " + cmmd, file=sys.stderr)

        if cmmd == 'Q':
          self.mpg123.quit()
          break

        elif cmmd == 'S':
          self.mpg123.send(cmmd)
        
          if os.path.exists(self.cursong):
            os.unlink(self.cursong)

        elif cmmd == 'P':
          if self.paused:
            self.paused = False
          else:
            self.paused = True
          self.mpg123.send(cmmd)

        elif cmmd == 'N':
          self.mpg123.send('LOAD ' + self.songlist.next())

        elif cmmd == 'V':
          self.mpg123.send('LOAD ' + self.songlist.previous())

        elif cmmd == 'U':
          self.mpg123.send('V ' + command[1:])

        elif cmmd == 'L':
          try:
            songid = command[command.index(' ')+1:]
            self.mpg123.send('LOAD ' + self.songlist.select(songid))
          except:
            self.songlist.previous()


      # If the current song is done, skip to the next
      if cmmd != 'S' and not self.paused:
        message = self.mpg123.recv()
        if message and message[:-1] == '@P 0':
          self.mpg123.send('LOAD ' + self.songlist.next())

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

      print('Player closed', file=sys.stderr)
    except:
      print(traceback.print_exc(), file=sys.stderr)
      #raise player error


if __name__ == '__main__':
  player = Player()
  try:
    player.init()
    player.play()
  finally:
    player.deinit()


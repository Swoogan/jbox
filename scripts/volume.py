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
import os, cgi
from utilities import volumectl, template

#get the volume from the data file
volctrl = volumectl.Volume()
form = cgi.FieldStorage()

try:
  volume = form['volume'].value
  volctrl.setVol(volume)
  volctrl.setPixel(form['pixel'].value)
  # save the volume to the volume file
  volctrl.save()
  #print 'Content-type: text/html\nStatus: 204 No Response\n'
  print 'Location: controller.py?cmd=U&id=' + volume + '\n'

except KeyError:
  #output the html
  tags = {'LEFT':volctrl.getPixel()}
  print template.populateTemplate(os.path.join('templates','volume.tpl'),tags)


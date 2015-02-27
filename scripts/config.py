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
import sys, cgi, os
from utilities import template, parseconf

form = cgi.FieldStorage()
#print >> sys.stderr, dir(form)
#form.popitem('save')

if form:
  try:
    fh = open(os.path.join('..','jbox.conf'),'w')
    for key in form.keys():
      fh.write(key + '=' + form[key].value + '\n')
    fh.close()
  except IOError, msg:
    print >> sys.stderr, msg


tags = parseconf.hashFromConf(os.path.join('..','jbox.conf'))
print template.populateTemplate(os.path.join('templates','config.tpl'),tags)
  
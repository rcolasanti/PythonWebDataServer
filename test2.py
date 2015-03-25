#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  test2.py
#  
#  Copyright 2015 Dr Ricardo L Colasanti <ric@Chicago>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

#!/usr/bin/env python

import cgi
import json
# print header
print "Content-type: text/html\n\n"

print "<h1>Arguments</h1>"

form = cgi.FieldStorage()
arg1 = form.getvalue('os')
print "OS: " +arg1+"<br>"

arg2 = form.getvalue('cpu')
print "CPU: "+arg2+"<br>"

arg3 = form.getvalue('server')
print "Server: "+arg3+"<br>"

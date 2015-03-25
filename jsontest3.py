#!/usr/bin/env python

import sys
import json
import cgi

import cgitb
cgitb.enable()


def debug_log(text):
    # note thet the logfile has to be chmod 0666
    with open('logfile.log', 'a') as logfile:
        logfile.write(text+'\n')
        
        
fs = cgi.FieldStorage()
if fs.has_key('a'):
    debug_log("here is a")
    x = fs['a'].vaue
    debug_log(""+x)
    
sys.stdout.write("Content-Type: application/json")

sys.stdout.write("\n")
sys.stdout.write("\n")

result = {}
result['success'] = True
result['message'] = "The command Completed Successfully so thats good"

sys.stdout.write(json.dumps(result,indent=1))
sys.stdout.write("\n")

sys.stdout.close()

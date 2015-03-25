#!/usr/bin/env python

import sys
import json
import cgi





def num(s):
    try:
        return float(s)
    except ValueError:
        return s


def debug_log(text):
    # note thet the logfile has to be chmod 0666
    with open('logfile.log', 'a') as logfile:
        logfile.write(text+'\n')
        
fs = cgi.FieldStorage()

sys.stdout.write("Content-Type: application/json")

sys.stdout.write("\n")
sys.stdout.write("\n")

result = {}
result['success'] = True
result['message'] = "The command Completed Successfully"
result['keys'] = ",".join(fs.keys())


s=""
for a in fs:
    for b in fs.getvalue('g[]'):
        s=s+b+","


result['data'] =  s
debug_log(s)

sys.stdout.write(json.dumps(result,indent=1))
sys.stdout.write("\n")

sys.stdout.close()

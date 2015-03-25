#!/usr/bin/env python

import sys
import json
import cgi

fs = cgi.FieldStorage()

def debug_log(text):
    # note thet the logfile has to be chmod 0666
    with open('logfile.log', 'a') as logfile:
        logfile.write(text+'\n')

sys.stdout.write("Content-Type: application/json")

sys.stdout.write("\n")
sys.stdout.write("\n")

result = {}
result['success'] = True
result['message'] = "The command Completed Successfully"
result['keys'] = ",".join(fs.keys())

d = {}
for k in fs.keys():
    debug_info(json.dumps(fs.getvalue(k)))
    d[k] = fs.getvalue(k)

result['data'] = d

sys.stdout.write(json.dumps(result,indent=1))
sys.stdout.write("\n")

sys.stdout.close()

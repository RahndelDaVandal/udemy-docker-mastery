#!/usr/bin/env python3

# this creates urlencode-friendly files without EOL
import urllib

with open("postb", "w") as outfile:
    params = {"vote": "b"}
    encoded = urllib.parse.urlencode(params)
    outfile.write(encoded)
with open("posta", "w") as outfile:
    params = {"vote": "a"}
    encoded = urllib.parse.urlencode(params)
    outfile.write(encoded)

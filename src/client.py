#!/usr/bin/env python3

import sys # builtin
import requests # builtin

f = sys.argv[1]
i = open(f, "rb")
fi = {"image": i}

url = "http://localhost:5000/histogram"
# url = "http://127.0.0.1:5000/histogram"

r = requests.post(url, files=fi)
try:
    print(r.json())
except ValueError:
    print(r)
    print("Unrecognized return type")

import sys
from requests import Request, Session

line_number = 0
vars = []
for line in sys.stdin:
    line_number += 1
    vars.append(line.strip())
    if line_number == 4:
        break

formatted_vars = ", ".join(vars)
session = Session()
r = Request(
    "MEW",
    "http://127.0.0.1:7777",
    headers={
        "x-cat-variable": formatted_vars
    }    
)
prepared_r = r.prepare()
response = session.send(prepared_r)
headers = dict(**response.headers)
lowered_headers = {}
for k in headers.keys():
    lowered_headers[k.lower()] = headers[k]
values = lowered_headers["x-cat-value"].split(", ")
for value in values:
    print(value)
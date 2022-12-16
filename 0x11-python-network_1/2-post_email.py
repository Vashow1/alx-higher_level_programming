#!/usr/bin/python3
"""
Takes in a URL and an email, sends a POST request to the passed URL
with the email as a parameter, and displays the body of the response
(decoded in utf-8)
"""
import urllib.request
import urllib.parse
import sys
if __name__ == "__main__":
    url = sys.argv[1]
    param = sys.argv[2]
    values = {'email': param}
    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        content = response.read()

    print(content.decode('utf-8'))

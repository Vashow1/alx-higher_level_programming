#!/usr/bin/python3
"""
takes in a URL, sends a request to the URL and
displays the body of the response
The essence of this exercise is to practice on HTTP error handling
"""
from urllib.error import HTTPError
from urllib.request import urlopen
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    try:
        with urlopen(url) as response:
            content = response.read()
        print(content.decode('utf-8'))

    except HTTPError as error:
        print("Error code:", error.status)

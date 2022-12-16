#!/usr/bin/python3
"""
takes in a URL, sends a request to the URL and
displays the body of the response
But the main thing being practiced is error handling with 'requests'
"""
import sys
import requests

if __name__ == "__main__":
    response = requests.get(sys.argv[1])
    if response:
        print(response.text)
    else:
        print(f"Error code: {response.status_code}")

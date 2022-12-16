#!/usr/bin/python3
"""
 takes in a letter and sends a POST request to
 http://0.0.0.0:5000/search_user with the letter as a parameter.
"""
import requests
import sys

if __name__ == "__main__":
    dictio = {'q': sys.argv[1]}
    response = requests.get(url, params=dictio)
    json_response = response.json()
    print(json_response)

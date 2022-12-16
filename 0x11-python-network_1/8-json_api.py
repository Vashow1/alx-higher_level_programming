#!/usr/bin/python3
"""
 takes in a letter and sends a POST request to
 http://0.0.0.0:5000/search_user with the letter as a parameter.
"""
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) > 1:
        letter = sys.argv[1]
    else:
        letter = ""

    url = 'http://0.0.0.0:5000/search_user'
    dictio = {'q': letter}
    response = requests.post(url, data=dictio)
    try:
        json_response = response.json()
        if len(json_response) == 0:
            print("No result")
        else:
            print(f"[{json_response.get('id')}] {json_response.get('name')}")
    except ValueError:
        print("Not a vaid JSON")

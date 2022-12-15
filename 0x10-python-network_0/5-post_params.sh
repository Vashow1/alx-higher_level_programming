#!/bin/bash
# sends a POST request to the passed URL, using specified params
curl -s -XPOST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"

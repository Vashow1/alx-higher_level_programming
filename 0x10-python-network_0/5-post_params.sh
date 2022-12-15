#!/bin/bash
# sends a POST request to the passed URL, using specified params
curl -s -XPOST -d "e-mail=test@gmail.com&subject=I will always be here for PLD" "$1"

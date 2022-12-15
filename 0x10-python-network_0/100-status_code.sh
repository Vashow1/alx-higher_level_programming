#!/bin/bash
# sends a request and returns only the status code of the response
curl -s -I "$1" | grep 'HTTP' | cut -z -d " " -f 2

#!/bin/bash
# sends a request and returns only the status code of the response
curl -s -I 0.0.0.0:5000 | grep 'HTTP' | cut -d " " -f 2

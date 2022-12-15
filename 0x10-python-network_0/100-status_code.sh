#!/bin/bash
# sends a request and returns only the status code of the response
curl -s -o /dev/null -I -w "%{http_code}" "$1"

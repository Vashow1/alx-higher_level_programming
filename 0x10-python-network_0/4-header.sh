#!/bin/bash
# sends a header variable and sends a GET request to the url
curl -s -H "X-School-User-Id: 98" "$1"

#!/bin/bash
# displays all HTTP methods the server will accept.
curl -s --head "$1" | tail -n1 | cut -d " " -f 2- 

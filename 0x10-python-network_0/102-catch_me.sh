#!/bin/bash
script that makes a request that causes the server to respond You got me
curl -sL -X PUT -H "user_id=98" 0.0.0.0:5000/catch_me | echo ""

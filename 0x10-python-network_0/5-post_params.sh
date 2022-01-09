#!/bin/bash
# Script takes in a URL as an argument, sends a GET request to the URL, and displays the body of the response
curl -sX POST -d "email=test@gmail.com" -d "subject=I will always be here for PLD" "$1" 

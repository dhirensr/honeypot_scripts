# Honeypot scripts
A collection of honeypot scripts written in python3 for services like ssh,ftp,http,etc

Currently supported for HTTP,SSH services
Logs:
1. IP address of the client
2. PORT from where client is coming from.
3. Password used for logging
4. TIME of the attack

## HTTP SCRIPT

Takes a request with Admin ID and password ,logs the information and then directly send a blank response to the client.
This can be used as a basic honeypot system which could try to get the HTTP headers and passwords information.

## SSH Script

SSH script is just logging the username and password tried by the client and then sending a wrong password response everytime.
This could be used for getting the passwords and usernames which the hackers/clients try on the system to get into the system.


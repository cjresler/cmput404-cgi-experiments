#!/usr/bin/env python

import os		
from pprint import pprint
import json
import urlparse
from templates import login_page
import sys

print "Content-Type: text/html"
#print

username = "hello"
password = "hello"

content_length = os.environ['CONTENT_LENGTH']
cookie = os.environ['HTTP_COOKIE']

logged_in = False

if 'logged-in=True' in cookie:
    logged_in = True

if content_length:
    bytes_to_read = int(content_length)

    content = sys.stdin.read(bytes_to_read)
    params = urlparse.parse_qs(content)

    if (params['username'][0] == username 
            and params['password'][0] == password):
        print "Set-Cookie: logged-in=True"
        logged_in = True

#HTTP headers over./
print

if not logged_in:
    #print login_page()
    print r"""
        <h1> Welcome! </h1>

        <form method="POST" action="hello.py">
            <label> <span>Username:</span> <input autofocus type="text" name="username"></label> <br>
            <label> <span>Password:</span> <input type="password" name="password"></label>

            <button type="submit"> Login! </button>
        </form>
        """
else:
    print "This is a secret message for", username

#params = urlparse.parse_qs(os.environ['QUERY_STRING'])
#print params


#user_agent = os.environ['HTTP_USER_AGENT']

#if 'Firefox' in user_agent:
#    print "You're using Firefox"

#elif 'Chrome' in user_agent:
#    print "You're using Chrome"

#elif 'curl' in user_agent:
#    print "You're using curl"

#else:
#    print "what"

#!/usr/bin/env python3
# *-* coding:utf-8 *-*

"""

:mod:`lab_json` -- JSON Navigation
=========================================

LAB_JSON Learning Objective: Learn to navigate a JSON file and convert to a
                             python object. Practice file IO using with.
::

 a. Using urllib2, explore the GitHub JSON API.  Load the initial api page, parse it
    into JSON, and use it for the following tasks.

 b. Load the list of emojis from the GitHub API and print a random one from the list.
    Save the list to emojis.json

 c. Load the information for a GitHub username passed in from the command line, print
    the number of repositories the user has and what organizations they belong to.
    Save the user info to {{username}}.json

"""

# see https://docs.python.org/2/library/urllib2.html for more info on urllib2
# example use of urllib2 to get a web resource:
import urllib.request
import urllib.error
import urllib.parse
import json

# PART A
data = urllib.request.urlopen("https://api.github.com/")
response = data.read()
urls = json.loads(response.decode())

# PART B
emojis = json.loads(urllib.request.urlopen(urls['emojis_url']).read().decode())
import random
print(random.choice(list(emojis.keys())))

# PART C
import sys
username = sys.argv[1]

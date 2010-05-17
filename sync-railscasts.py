#!/usr/bin/env python
#
# sync-railscasts.py
# Script to download all Railscasts (http://railscasts.com)
# Copyright (C) 2010 Shreyank Gupta <sgupta@REDHAT.COM>
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import feedparser
import urllib
import os
from subprocess import Popen

FEED_URL = "http://feeds.feedburner.com/railscasts"

def file_name(url):
    return url.split('/')[-1]

def download(url):
    """
    Copy the contents of a file from a given URL to a local file.
    """
    name = file_name(url)
    web_fd = urllib.urlopen(url)
    local_fd = open(name, 'w')
    local_fd.write(web_fd.read())
    web_fd.close()
    local_fd.close()
    print "Downloaded: %s" % name

feed = feedparser.parse(FEED_URL)

for entry in feed['entries']:
    media = entry['enclosures'][0]
    url = media['href']
    name = file_name(url)
    if not os.path.exists(name):
        download(url)
    elif not (os.path.getsize(name) == long(media['length'])):
        download(url)
    else:
        print "Exists: %s" % name

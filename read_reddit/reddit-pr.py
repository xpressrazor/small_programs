#!/usr/bin/python

from functools import reduce
import os

file_url = '/path/reddit-list.txt'
browser = 'chromium'

file = open(file_url)
lines = file.read().splitlines()
file.close()

url_prefix = '"http://reddit.com/r/'

url_list = reduce(lambda x,y: x + [url_prefix + '{0}\"'.format(y)], lines, [])
formatted_text = " ".join(url_list)
os.system("{0} {1}".format(browser, formatted_text))

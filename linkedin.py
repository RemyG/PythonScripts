#! /usr/bin/env python

import urllib2
import requests
import StringIO
from lxml import etree

res = requests.get("http://fr.linkedin.com/in/remygardette")
parser = etree.HTMLParser()
tree   = etree.parse(StringIO.StringIO(res.content), parser)
for div in tree.xpath("//div[contains(@class, 'position')]"):
	if len(div.xpath("div/h3/span[@class='title']")) > 0:
		print(div.xpath("div/h3/span[@class='title']/text()")[0])


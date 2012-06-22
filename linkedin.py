#! /usr/bin/env python

import urllib2
import requests
import StringIO
import sys
from lxml import etree

if len(sys.argv) != 2: 
    print 'Usage: linkedin.py <profile_address>' 
    sys.exit(1) 

f = open('linkedin_resume', 'w')

res = requests.get(sys.argv[1])
parser = etree.HTMLParser()
tree   = etree.parse(StringIO.StringIO(res.content), parser)

f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
f.write('<resume>\n')

for div in tree.xpath("//div[contains(@class, 'position')]"):
	if len(div.xpath("div/h3/span[@class='title']")) > 0:
		f.write('<position>\n')
		if len(div.xpath("div/h3/span[@class='title']")) > 0:
			f.write('<title>')
			f.write(div.xpath("div/h3/span[@class='title']/text()")[0])
			f.write('</title>\n')
		if len(div.xpath("div/h4//span/text()")) > 0:
			f.write('<company>')
			f.write(div.xpath("div/h4//span/text()")[0])
			f.write('</company>\n')
		if len(div.xpath("p[@class='period']/abbr")) > 1:
			f.write('<from>')
			f.write(div.xpath("p[@class='period']/abbr/text()")[0])
			f.write('</from>\n')
			f.write('<to>')
			f.write(div.xpath("p[@class='period']/abbr/text()")[1])
			f.write('</to>\n')
		if len(div.xpath("p[contains(@class, 'description')]/text()")) > 0:
			f.write('<description>')
			desc = etree.tostring(div.xpath("p[contains(@class, 'description')]")[0])
			desc = desc[desc.find(">")+1:desc.rfind("<")].strip()
			f.write(desc)
			f.write('</description>\n')
		f.write('</position>\n')

f.write('</resume>\n')

f.close()


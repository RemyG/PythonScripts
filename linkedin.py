#! /usr/bin/env python
# -*- coding: UTF-8 -*-

"""
Copyright 2012 Remy Gardette

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

import cgi
import codecs
import dateconverter
import requests
import StringIO
import sys
from lxml import etree
from dateconverter import DateConverter


if len(sys.argv) != 3: 
	print 'Usage: linkedin.py <profile_address> <output_file>' 
	sys.exit(1)
	
profile_url = sys.argv[1]
output_file = sys.argv[2]

pos_nb = 0

f = codecs.open(output_file, encoding='utf-8', mode='w')

dc = DateConverter()

res = requests.get(profile_url)
parser = etree.HTMLParser()
tree   = etree.parse(StringIO.StringIO(res.content), parser)

f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
f.write('<resume>\n')

for div in tree.xpath("//div[contains(@class, 'position')]"):
	if len(div.xpath("div/h3/span[@class='title']")) > 0:
		pos_nb += 1
		f.write('<position>\n')
		if len(div.xpath("div/h3/span[@class='title']")) > 0:
			f.write('<title>')
			f.write(div.xpath("div/h3/span[@class='title']/text()")[0])
			f.write('</title>\n')
		if len(div.xpath("div/h4//span/text()")) > 0:
			f.write('<company>')
			f.write(div.xpath("div/h4//span/text()")[0])
			f.write('</company>\n')
		if len(div.xpath("p[@class='period']/span[@class='location']")) > 0:
			f.write('<location>')
			f.write(div.xpath("p[@class='period']/span[@class='location']/text()")[0])
			f.write('</location>\n')
		if len(div.xpath("p[@class='period']/abbr")) > 1:
			f.write('<from>')
			f.write(dc.dict_sub(div.xpath("p[@class='period']/abbr/text()")[0]))
			f.write('</from>\n')
			f.write('<to>')
			f.write(dc.dict_sub(div.xpath("p[@class='period']/abbr/text()")[1]))
			f.write('</to>\n')
		if len(div.xpath("p[contains(@class, 'description')]/text()")) > 0:
			f.write('<description>')
			desc = etree.tostring(div.xpath("p[contains(@class, 'description')]")[0])
			desc = desc[desc.find(">")+1:desc.rfind("<")].strip()
			desc = cgi.escape(desc)
			f.write(desc)
			f.write('</description>\n')
		f.write('</position>\n')

f.write('</resume>\n')

f.close()

print "Profile " + profile_url+ " successfully scraped"
print "with " + str(pos_nb) + " positions."
print "Output in " + output_file

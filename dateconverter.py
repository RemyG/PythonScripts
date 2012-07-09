# -*- coding: UTF-8 -*-

'''
Created on 9 Jul 2012

@author: ramy
'''

import re

class DateConverter:
	'''
	classdocs
	'''

	datedict = {
		'[Jj]anuary'	: 'Jan.',
		'[Ff]ebruary'	: 'Feb.',
		'[Mm]arch'		: 'Mar.',
		'[Aa]pril'		: 'Apr.',
		'[Mm]ay'		: 'May',
		'[Jj]une'		: 'June',
		'[Jj]uly'		: 'July',
		'[Aa]ugust'	: 'Aug.',
		'[Ss]eptember'	: 'Sept.',
		'[Oo]ctober'	: 'Oct.',
		'[Nn]ovember'	: 'Nov.',
		'[Dd]ecember'	: 'Dec.',
		'[Pp]resent'	: 'Now',
		
		'[Jj]anvier'	: 'Janv.',
		'[Ff]évrier'	: 'Févr.',
		'[Mm]ars'		: 'Mars',
		'[Aa]vril'		: 'Avril',
		'[Mm]ai'		: 'Mai',
		'[Jj]uin'		: 'Juin',
		'[Jj]uillet'	: 'Juil.',
		'[Aa]oût'		: 'Août',
		'[Ss]eptembre'	: 'Sept.',
		'[Oo]ctobre'	: 'Oct.',
		'[Nn]ovembre'	: 'Nov.',
		'[Dd]écembre'	: 'Déc.'
	}

	def __init__(self):
		'''
		Constructor
		'''
		
	def dict_sub(self, text): 
		""" Replace in 'text' non-overlapping occurences of REs whose patterns are keys
		in dictionary 'd' by corresponding values (which must be constant strings: may
		have named backreferences but not numeric ones). The keys must not contain
		anonymous matching-groups.
		Returns the new string.""" 
		# Create a regular expression  from the dictionary keys
		regex = re.compile("|".join("(%s)" % k for k in self.datedict))
		# Facilitate lookup from group number to value
		lookup = dict((i+1, v) for i, v in enumerate(self.datedict.itervalues()))
		# For each match, find which group matched and expand its value
		return regex.sub(lambda mo: mo.expand(lookup[mo.lastindex]), text)
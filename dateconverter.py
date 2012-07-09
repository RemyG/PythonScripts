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
		'January'	: 'Jan.',
		'February'	: 'Feb.',
		'March'		: 'Mar.',
		'April'		: 'Apr.',
		'May'		: 'May',
		'June'		: 'June',
		'July'		: 'July',
		'August'	: 'Aug.',
		'September'	: 'Sept.',
		'October'	: 'Oct.',
		'November'	: 'Nov.',
		'December'	: 'Dec.',
		'Present'	: 'Now',
		
		'Janvier'	: 'Janv.',
		'Février'	: 'Févr.',
		'Mars'		: 'Mars',
		'Avril'		: 'Avril',
		'Mai'		: 'Mai',
		'Juin'		: 'Juin',
		'Juillet'	: 'Juil.',
		'Août'		: 'Août',
		'Septembre'	: 'Sept.',
		'Octobre'	: 'Oct.',
		'Novembre'	: 'Nov.',
		'Décembre'	: 'Déc.'
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
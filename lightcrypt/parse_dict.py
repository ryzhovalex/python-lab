#!/usr/bin/env python
"""Parsing code book into local readable format for further crypting processes.

Parsed code book can use all in-package cryptors.
Package's cryptors will remake it into crypt books using particular cyphers.
"""

import sys
sys.path.append('C:\\python\\') #my main pc
sys.path.append('C:\\Users\\simen\\OneDrive\\Рабочий стол\\alex\\python\\') #hometown pc
from adaptopener import file_opener as fo

__author__ = "D4rkof"
__version__ = "1.0.1"
__maintainer__ = "D4rkof"
__email__ = "thed4rkof@gmail.com"
__status__ = "Production"

def cb_parse(code_book_path):
		'''
		|	Parse txt objects (A.K.A code books) for programms in lightcrypt. Returns parsed dictionary.
		|	Args:
		|	CODE_BOOK_PATH <str>: path to code_book.txt with letters and their code analogs	
		'''

		_file = fo.open_file(code_book_path, 'r', __file__)
		_parsed_dict = {}

		for x in _file: #ex.: x == 21U
			_key = ''
			_value = ''
			_reserve = x	
			x = x.split('-')

			#delete tabulations and new line jumps
			if len(x) > 1: #== has readable element
				if x[1].count('\\') == 1 and x[1][0] == '\\': #->
					#-> has special commands (standard line jump + predicted, like /n/n == 1 readable symbol) and additional check (if we have excess, like another/t/n)
					x[1] = x[1][0] + x[1][1] #save only first two chars
	
				else:
					x[1] = x[1].replace('\n', '')
					x[1] = x[1].replace('\t', '')
					x[1] = x[1].replace(' ', '') #excess spaces preventor

					#if key == '' it means that needed '-' has been deleted and needs recovery(for ex. '38--')
					if x[1] == '':
						if _reserve[-2] == '-':
							x[1] = '-'

			else: #== end of the book
				break 

			_key = x[1]
			_value = x[0]		
			_parsed_dict[_key] = _value

		return _parsed_dict

''''''
if __name__ == '__main__':
	cb_parse('resources/CODE_BOOK.txt')


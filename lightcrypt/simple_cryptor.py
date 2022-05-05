#!/usr/bin/env python
"""Crypting and decrypting string messages. 

Uses package's code book and parses it into crypt book with particular cypher key.
Crypt book furtherly uses for crypting or decrypting messages.
"""

import sys
sys.path.append('C:\\python\\') #my main pc
sys.path.append('C:\\Users\\simen\\OneDrive\\Рабочий стол\\alex\\python\\') #hometown pc
from adaptopener import file_opener as fo
import parse_dict as pd

__author__ = "D4rkof"
__version__ = "1.0.0"
__maintainer__ = "D4rkof"
__email__ = "thed4rkof@gmail.com"
__status__ = "Production"

class Crypt:
	'''
	|	This programm can be used for simple encryption and decryption strings. 
	|	You need to adjust code_book.txt with letters and their code analogs.	
	'''
	def __init__(self, 
		cypher_key: str = '2535',
		origin_path: str = 'input.txt', 
		result_path: str = 'output/simple_cryptor_result.txt', 
		code_book_path: str = 'resources/CODE_BOOK.txt'):
		'''
		|	--> INITIALIZATION
		|	After standard assignments, calls main class controller. 
		|	It means that if instance has called, automatically crypting operation calls too.         
		|	Args:
		|	origin_path <str>: relative path of file where string to encrypt contains
		|	CODE_BOOK_PATH <str>: path to code_book.txt with letters and their code analogs (default 'resources/CODE_BOOK.txt') 
		|	cypher_key <str>: key that will define encrypt style (default 'p2m5')
		|	result_path <str>: relative path of file where result will save to (default 'output/simple_cryptor_result.txt')	
		'''

		self._cypher_key = cypher_key                                         
		self._origin_path = origin_path
		self._result_path = result_path	
		self.code_book_path	= code_book_path
		self.class_controller()

	def class_controller(self):
		'''|	Sequency starts scripts from the class. '''	

		#origin content of the file
		self._content = fo.open_file(self._origin_path, 'r', __file__).read() 
		self._args_format_check()
		PARSED_DICT = pd.cb_parse(self.code_book_path)
		self._crypt_dict = self._create_crypt_dict(PARSED_DICT)
		self._mode_assembler()

		if self._mode == 'e':
				self._encrypt()

		elif self._mode == 'd':
				self._decrypt()

		self._result_write()
		self._result_print()
		self._quit_operator('', exception = False) #if everything happened correctly, programm ends

	def _args_format_check(self):
		'''|	Check all arguments and throw a message if them have wrong format. '''

		if self._content == '':
			self._quit_operator('Input file has no text inside.')

		#check proper length of cypher key
		if len(self._cypher_key) == 0:
			self._quit_operator('Empty string has sended to cypher key.')

		#check each symbol of cypher_key for digit
		for n in self._cypher_key:
			if not n.isdigit() or n == '0':
				self._quit_operator('Incorrect format of cypher key.')
				
	def _mode_assembler(self):
		'''|	Decides what work mode should be chosen. Returns mode name. '''
		
		if self._content.find(self._cypher_key) != -1 or self._content.find(self._hide_cypher(unhide = False)) != -1: #found cypher key in text
			self._mode = 'd'

		else:
			self._mode = 'e'			
				
	def _create_crypt_dict(self, PARSED_DICT):
		'''|	Crypting parsed dictionary with cypher key. Returns crypted dictionary. '''
		
		_crypt_dict = {}

		for k, v in PARSED_DICT.items():
			if k == 'space':
				k = ' '
			#check for control commands - its important to parse it correctly
			elif k == '\\n':
				k = '\n'

			elif k == '\\t':
				k = '\t'
			
			_int_v = int(v)

			for x in self._cypher_key:
				x = int(x)
				_counter = 0
				_operation_lst = ['+', '-', '*']
				#save current char to new var
				_cur_char = _operation_lst[_counter]
				_counter += 1

				#check if _counter break limit
				if _counter == len(_operation_lst):
					_counter == 0

				#arithmetic logic for choosen char
				if _cur_char == '+':
					_int_v += x

				elif _cur_char == '-':
					_int_v -= x

				elif _cur_char == '*':
					_int_v *= x

			_crypt_dict[k] = _int_v 

		return _crypt_dict

	def _hide_cypher(self, cypher: str = 'default', unhide: bool = False):
		'''
		|	Makes an encrypted cypher for further output or can decrypt it (depends on flag 'unhide')
		|	Returns crypted or encrypted cypher
		'''

		_crypt_dict = {
		'0': 'A', 
		'1': 'B', 
		'2': 'C', 
		'3': 'D', 
		'4': 'E', 
		'5': 'F', 
		'6': 'G', 
		'7': 'H', 
		'8': 'I', 
		'9': 'J' 
		}

		_result = ''

		if cypher == 'default':
			cypher = self._cypher_key

		if unhide:
			for x in cypher:
				for k, v in _crypt_dict.items():
					if x == v:
						_result += str(k)

		else:
			for x in cypher:
				for k, v in _crypt_dict.items():
					if x == k: 
						_result += str(v)

		return _result

	def _encrypt(self):
		'''|	Crypting string with crypting dict. Void. '''

		self._stream_message = self._content
		self._c_message = self._hide_cypher() #crypted mode marker
		self._c_message += '>'

		for x in self._content:
			for k, v in self._crypt_dict.items():
				if x == k:
					self._c_message += str(v)
					self._c_message += 'x' #separate symbol
				
	def _decrypt(self):
		'''|	Decrypting string with crypting dict. Void. '''
		
		self._d_message = ''

		#parse crypted message into list of strings with numbers
		self._numbers_lst = [] #list which will contain parsed numbers for further decrypting
		self._current_str = '' #dynamic string that constantly refreshes with new values

		for x in self._content:
			if x == 'x': #check for separators
				self._numbers_lst.append(self._current_str)
				self._current_str = ''

			elif x == '>':
				print(self._current_str)
				self._current_str = self._hide_cypher(self._current_str, unhide = True) #decrypt current string


				if self._current_str == self._cypher_key: #keys coincided
					self._current_str = '' #zero string and won't add it to general list

				elif self._current_str != self._cypher_key: #keys didn't coincided
					self._quit_operator("Can't decrypt this string: " + self._content)

			else: #x is encryptable digit
				self._current_str += str(x)

		for x in self._numbers_lst:
			for k, v in self._crypt_dict.items():
				if v == int(x):
					self._d_message += str(k)

		self._stream_message = self._d_message

	def _result_write(self):
		'''|	Writing result to a file (following format depends on mode). '''

		self._result_file = fo.open_file(self._result_path, 'w', __file__)

		if self._mode == 'e':
			self._result_message = 'encryption result of instance:' + str(self) + '----> ' + str(self._c_message)	

		if self._mode == 'd':
			self._result_message = 'decryption result of instance:' + str(self) + '----> ' + str(self._d_message)
		
		self._result_file.write(self._result_message)

	def _result_print(self):
		'''|	Writing result to a stream (following format depends on mode). '''

		if self._mode == 'e':
			print('Message: ' + self._stream_message)
			print('encrypted in ---> ' + self._result_path + ' <--- succesful!')

		elif self._mode == 'd':
			print('decrypted in ---> ' + self._result_path + ' <--- succesful!')
			print('Result encoded message: ' + self._stream_message)		

	def _quit_operator(self, quit_message: str = 'Closing programm...', exception: bool = True):
		'''|	Prints a message to stream and ends programm. If it is an exception, adds appropriate message. '''                              

		_reason_message = ''

		if exception:
			if quit_message == '':
				_reason_message += 'EXCEPTION: UndefinedException'
				print(_reason_message)

			elif quit_message != 'Closing programm...':
				_reason_message += 'EXCEPTION: '
				_reason_message += quit_message
				_reason_message += '\nClosing programm...'
				print(_reason_message)

		elif quit_message == '': #exception == False with empty string
			pass #just make further quit

		quit()	

	@property
	def c_message(self):
		return self._c_message

	@property
	def d_message(self):
		return self._d_message

''''''
if __name__ == '__main__':
	a = Crypt()


	



	




		


	

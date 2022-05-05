# module file_opener in package adaptopener made by D4rkof 3th October 2020
'''
example usage:
import sys
sys.path.append('..\\adaptopener\\')
import file_opener
'''
import file_opener as opener

import os

def open_file(target_path: str, open_mode: str = 'r', origin_path: str = None, encoding: str = 'utf-8'):
	'''
	|	Opens file relatively or absolutely to called script by path in read mode. Returns opened file.
	|	Args:
	|	target_path <str>: relative OR absolute path of file
	|	open_mode <str>: mode to open file (default 'r')
	|	origin_path <str>: relative path of called script (default None)
	|	encoding <str>: type of encode (default 'utf-8')	
	'''

	_path_type = _absrel_solver(target_path, origin_path)

	if  _path_type == 'abs':
		_file = open(target_path, open_mode, encoding = encoding)	

	elif _path_type == 'rel':
		_file = open(_get_abs_path(origin_path, target_path), open_mode, encoding = encoding)	

	return _file

def _absrel_solver(t_path, o_path):
	'''|	Decides what kind of path on join (relative or absolute). Returns file type string. '''

	if o_path == None:
		return 'abs'

	elif t_path.find(':\\') != -1:
		return 'abs'

	else:
		return 'rel'

def _get_abs_path(origin_path: str, target_path: str):
	'''|	Returns absolute path of target file. '''

	_script_dir = os.path.dirname(origin_path) 
	_rel_path = target_path
	_abs_file_path = os.path.join(_script_dir, _rel_path)

	return _abs_file_path


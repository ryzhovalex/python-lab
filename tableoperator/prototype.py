#
import sys
sys.path.append('..\\adaptopener')
import file_opener as opener

def sum_columns(path: str):
	file = opener.open_file(path, 'r+')
	lines = file.readlines()
	x = ''
	y = ''
	i = 0

	while i < len(lines):
		'''
		x = lines[i][0] + lines[i][1] + lines[i][2]
		y = lines[i][4] + lines[i][5] + lines[i][6]
		'''
		x = lines[i][0] + lines[i][1] + lines[i][2]
		y = lines[i][4] + lines[i][5] + lines[i][6] + lines[i][7]

		double_char_number = False
		try:
			test = int(lines[i][8])
		except:
			double_char_number = True
		finally:
			if not double_char_number:
				y += lines[i][8]


		z = (int(x) + int(y))

		file.write(str(z))
		file.write('\n')

		i += 1




if __name__ == '__main__':
	print('starting')
	sum_columns('data/table.txt')

# kata: https://www.codewars.com/kata/54d81488b981293527000c8f

# TODO: this code working properly, but slow
# original attempt's tests consists over 10000 numbers on input
# so i need a way to speed up process...
# Some thoughts: big performance issues may be caused from picking in two nested 'for' loops (maybe find another way there?)

def sum_pairs(ints, s):
	best = None
	for x in range(len(ints)-1):
		for y in range(x+1, len(ints)):
			current_control_sum = 2 * y
			if ints[x] + ints[y] == s:
				try:
					if current_control_sum < best_control_sum:
						best = [x, y]
						best_control_sum = current_control_sum
					else:
						continue
				except UnboundLocalError:
					best = [x, y]
					best_control_sum = current_control_sum
					
	## Deparse best tuples to result ##
	try:
		res = [ints[best[0]], ints[best[1]]]
	except TypeError:
		return None
	else:
		return res


def main(): 
	l1= [1, 4, 8, 7, 3, 15]
	l2= [1, -2, 3, 0, -6, 1]
	l3= [20, -13, 40]
	l4= [1, 2, 3, 4, 1, 0]
	l5= [10, 5, 2, 3, 7, 5]
	l6= [4, -2, 3, 3, 4]
	l7= [0, 2, 0]
	l8= [5, 9, 13, -3]

	assert sum_pairs(l1, 8) == [1, 7]
	assert sum_pairs(l2, -6) == [0, -6]
	assert sum_pairs(l3, -7) == None
	assert sum_pairs(l4, 2) == [1, 1]
	assert sum_pairs(l5, 10) == [3, 7]
	assert sum_pairs(l6, 8) == [4, 4]
	assert sum_pairs(l7, 0) == [0, 0]
	assert sum_pairs(l8, 10) == [13, -3]


if __name__ == "__main__":
	main()
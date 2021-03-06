__author__ = 'Vineets'


from math import sqrt

yellow = (5, 10)
blue = (20, 5)

def get_dis(x, y):
	return sqrt((x[0] - y[0])**2 + (x[1] - y[1])**2)

def check(upper_left, lower_right, y = True):
	global yellow, blue
	if y and get_dis(yellow, upper_left) > get_dis(blue, upper_left):
		return False
	elif y and get_dis(yellow, lower_right) > get_dis(blue, lower_right):
		return False
	elif y:
		return True
	if not y and get_dis(blue, upper_left) > get_dis(yellow, upper_left):
		return False
	elif not y and get_dis(blue, lower_right) > get_dis(yellow, lower_right):
		return False
	elif not y:
		return True

if __name__ == '__main__':
	"""
	output:
		True (correct answer)
	    False
	    False
	    False
	"""
	print check((7, 12), (12, 8)) and check((16, 19), (25, 12), y = False)
	print check((7, 12), (12, 8)) and check((16, 16), (18, 5), y = False)
	print check((3, 15), (13, 7)) and check((11, 5), (17, 2), y = False)
	print check((6, 15), (13, 7)) and check((16, 19), (25, 12), y = False)
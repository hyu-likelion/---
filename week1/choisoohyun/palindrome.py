from bwsi_grader.python.palindrome import grader

# make sure to execute this cell so that your function is defined
# you must re-run this cell any time you make a change to this function

def student_func(x):
	# `x` is a string
	# this function should return either `True` or `False`

	# write your code here
	# be sure to include a `return` statement so that
	# your function returns the appropriate object.
	x = x.replace(" ", "").lower()
	y = x[::-1]
	if x == y:
		result = True
	else:
		result = False
	return result

grader(student_func)

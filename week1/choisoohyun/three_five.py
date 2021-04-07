from bwsi_grader.python.three_five import grader

def student_func(x):
	# write your code here
	# be sure to include a `return` statement so that
	# your function returns the appropriate object.
	if x % 3 == 0 and x % 5 == 0:
		result = "threefive"
	elif x % 3 == 0:
		result = "three"
	elif x % 5 == 0:
		result = "five"
	else:
		result = int(x)
	return result

grader(student_func)

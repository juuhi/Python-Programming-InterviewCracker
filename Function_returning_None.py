"""
Demo of return None by Function
below code to test return values in fucntions;
any function ideally should return 1 on successful execution or else should return None on any other error.
"""

def myFun(val):
	if val == 'test':
		return
	else:
		return 1

var1 = myFun('test')

if var1 is None:
	print "matched and returned True"
elif var1 is 1:
	print "not mached and returned 1"

var1 = myFun('test1')

if var1 is None:
	print "matched and returned True"
elif var1 is 1:
	print "not mached and returned 1"
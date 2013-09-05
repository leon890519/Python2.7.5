# -*- coding:utf-8 -*-

def while_loop(count, addnum):
	i = 0
	numbers = []
	
	while i < count:
		print "At the top i is %d" % i
		numbers.append(i)	
		i = i + addnum
		print "Numbers now: ", numbers
		print "At the bottom i is %d" % i
	
	print "The numbers: "
	for num in numbers:
		print num
		
while_loop(3, 1)
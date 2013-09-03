# -*- coding: utf-8 -*-
# 使用非ASCII字符而且碰到了编码错误，比如有中文(注释中有中文也不行)，在代码顶端加上下面一行

my_name = '王小钢'
my_age = 35 # not a lie
my_height = 74 # inches
my_weight = 180 # lbs
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

print "Let's talk about %r." % my_name  # 可以使用%r代替，打印出任何东西
print "He's %r inches tall." % my_height
print "He's %r pounds heavy." % my_weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee." % my_teeth

# this line is tricky, try to get it exactly right	
print "If I add %d, %d, and %d I get %d." % (my_age, my_height, 
	my_weight, my_age + my_height + my_weight)
	
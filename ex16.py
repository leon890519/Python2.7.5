# *-* coding:utf-8 *-*

from sys import argv

script, filename = argv

print "We're going to erase %r." % filename


print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")

print "Opening the file ..."
target = open(filename, 'w+') # 以写模式打开文件时自动清空文件内容

print "Truncating the file. Goodbye!"
#target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

#target.write(line1)
#target.write("\n")
#target.write(line2)
#target.write("\n")
#target.write(line3)
#target.write("\n")

content = line1 + "\n" + line2 + "\n" + line3 + "\n"
content2 = "%s\n%s\n%s\n" % (line1, line2, line3)
target.write(content2)

print "And finally, we close it."
target.close()
target = open(filename, 'r+')
print target.read()   # 如果不先关闭文件再打开，而是直接读取的时候会多读出好多空字符NUL
target.close()

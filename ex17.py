# *-* coding:utf-8 *-*
from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

# We could do these two on one line too, how?
#in_file = open(from_file)
indata = open(from_file).read()  # 如果以这种方式打开文件，在读写完文件后自动关闭文件，无须再调用close()

print "The input file is %d bytes long" % len(indata)

print "Does the output file exist? %r" % exists(to_file)
#print "Ready, hit RETURN to continue, CTRL-C to abort."
#raw_input()

#out_file = open(to_file, 'w')
open(to_file, 'w').write(indata)

print "All right, all done."

#out_file.close()
#in_file.close()

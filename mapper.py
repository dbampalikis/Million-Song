#!/usr/bin/env python
#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys

#load()
similarList = []
for line in sys.stdin:
	similarList.append(line.strip())
for similar in similarList:
	print '%s\t%s' % (similar, 1)
	#sys.stdout.write(similar+"\t"+"1")
	#sys.stdout.write('%s\t%s' % (similar, 1))
	#sys.stdout.write("test\tasd")

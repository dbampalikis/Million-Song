#!/usr/bin/env python
#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys

#load()

# New list
similarList = []

# Input comes from STDIN (standard input)
for line in sys.stdin:
	similarList.append(line.strip()) # append to list
	
# Print all elements in the list
for similar in similarList:
	print '%s\t%s' % (similar, 1)
	

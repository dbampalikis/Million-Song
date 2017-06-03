# A file to sort the output from the MapReduce
import os
import operator

# Open the result file
f = open('/Users/dbampalikis/output.txt', 'r')

# Read the content
content = f.readlines()
t = {}

# Sort the content
for line in content:
	word, count = line.split()

	if int(count) > 100:
		t[word] = count
sorted_t = sorted(t.items(), key=operator.itemgetter(1), reverse=True)

# Print the sorted content
print sorted_t

# Close the file
f.close()

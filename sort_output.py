import os
import operator


f = open('/Users/dbampalikis/output.txt', 'r')
content = f.readlines()
t = {}
for line in content:
	word, count = line.split()

	if int(count) > 100:
		t[word] = count
sorted_t = sorted(t.items(), key=operator.itemgetter(1), reverse=True)
print sorted_t
f.close()
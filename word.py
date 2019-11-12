name = input("Enter a file name:")
txt = open(name)
dic= {}
for lin in txt:
	lin = lin.rstrip()
	words = lin.split()

	for word in words:
		dic[word] = dic.get(word,0) + 1
print([(k,v) for v,k in (sorted([(v,k) for k,v in dic.items()], reverse=True))[:10]])

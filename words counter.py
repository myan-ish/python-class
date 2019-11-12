name = input("Enter a file name:")
txt = open(name)
dic= {}
for lin in txt:
	lin = lin.rstrip()
	words = lin.split()

	for word in words:
		dic[word] = dic.get(word,0) + 1
print(dic)
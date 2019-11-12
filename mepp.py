def magic():
	for i in range(1,8):
		counter=1
		while True:
			while True:
			#Fliter the input
				while True:
					try:
						e = int(input("Enter your respective day's expense:"))
						print("Your day",counter, "expense is",e)
						val= int(e)
						break
					except ValueError:
						print("Please enter a number")
				#saving list
				dic.append((counter,e))
				counter+=1	

				#adding inputs
				while True:
					q= input("Do you want to add new value?(y/n)")
					if q in ('y','n'):
						break
					print("invalid input")
				if q == "y":
					continue
				else:
					break
			break
		break
	return






 #main process
sum = 0
big=-1


#opening data file
while  True:
	file_loc = input("Do you want to create a new file or open existing one? (n/e)")
	if file_loc in ("n", "e"):
		break
	Print("invalid input")

if file_loc =="n":
	name = input("Enter a file name: ")
	file = open(name,"a")
	dic=list()
	magic()

else:
	name = input("Existing file name: ")
	file = open(name,"r+")
	dic = list(file.read())
	print(dic)
	magic()

	#process
for (k,v) in dic:
	file.write(list(dic))
	sum += v
	if k> big:
		big=k



mean = sum/big

print("By the end of the week you will spend",(mean*7) )


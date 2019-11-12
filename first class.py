number = int(input('Enter a number '))
check = True
prime = []
for i in range(2, number):
    for j in range(2, i):
        if j % i == 0:
            check = False
            break
    if check == True:
        prime.append(i)
print(prime)

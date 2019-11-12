maths={"j":50, 's':20}
sci={"ja":50, 'sa':20}
sc={"jac":50, 'sac':20}
total={}
maths["k"]=30
for d in (maths, sci,sc):
	total.update(d)
maths.update(sci)

print(total)



'''
print(maths)'''
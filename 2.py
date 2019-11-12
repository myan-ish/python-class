'''dic={'roll':[1,2,3,4], 'name':["Ram", "Sita", "Hari", "Geeta"], 'marks':[10,20,30,40], 'gen':['male','female','male','female']}


for i in range(len(dic['roll'])):
	if dic['gen'][i]=="male":
		print(dic['marks'][i])
		print(dic['name'][i])'''


d1 = {'jajo':['male',35], 'rohila':['female',40], 'nimesh':['male',55]}
list = []
for (k,v) in d1.items():
    if v[0] == 'male':
        print(k,v[1])
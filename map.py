#  list of 5number using map
n= [x for x in range(6)]  
double=set(map(lambda x:x**2,n ))
for i in double:
    print(i)
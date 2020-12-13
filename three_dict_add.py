dic1={1:10, 2:20}
dic2={3:30,2:40}
dic3={5:50,6:60}
n={}
for x,y,z in zip(dic1,dic2,dic3):
    if x==y:
        a=(dic1[x]+dic2[y])
        n[x]=a
    elif y==z:
        a=(dic2[y]+dic3[z])
        n[y]=a
    elif z==x:
        a=(dic3[z]+dic1[x])
        n[z]=a
dic1.update(dic2)
dic1.update(dic3)
dic1.update(n)
print(dic1)


# output
# {1: 10, 2: 60, 3: 30,  5: 50, 6: 60} 




# dic1={1:10, 2:20}
# dic2={3:30,2:40}
# dic3={5:50,6:60}
# a=[]
# for x in dic1:
#     a.append(x)
# b=[]
# for x in dic2:
#     b.append(x)
# c=[]
# for x in dic3:
#     c.append(x)
# d=a+b+c
# print(d)
# i=0
# sum=0
# while i<len(d):
    


# # dic1.update(dic2)
# # dic1.update(dic3)

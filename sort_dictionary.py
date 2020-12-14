n={'bijender':45,'deepak':60,'param':20,'anjili':30,'roshini':50}
a=[]
b=[]
for x in n:
    a.append(x)
    b.append(n[x])
i=0
n={}
while i<len(b):
    j=0
    while j<len(b):
        if b[i]>b[j]:
            b[i],b[j]=b[j],b[i]
            a[i],a[j]=a[j],a[i]  
        j=j+1
    i=i+1
i=0
n={}
while i<len(b):
    n[a[i]]=b[i]
    i=i+1
print(n)

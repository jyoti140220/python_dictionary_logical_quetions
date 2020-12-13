a="MISSISSIPPI"
i=0
y=[]
while i<len(a):
    if a[i] not in y:
        y.append(a[i])
    i=i+1
t=y
i=0
n={}
while i<len(t):
    count=0
    j=0
    while j<len(a):
        if t[i]==a[j]:
            count=count+1
        j=j+1
    n[y[i]]=count
    i=i+1
print(n)


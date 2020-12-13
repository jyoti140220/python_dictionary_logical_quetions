a=[
     {"first":"1"}, 
     {"second": "2"}, 
     {"third": "1"}, 
     {"four": "5"}, 
     {"five":"5"}, 
     {"six":"9"},
     {"seven":"7"}
] 
i=0
p=[]
while i<len(a):
    for x in a[i]:
        c=(a[i][x])
        if c not in p:
            p.append(c)
    i=i+1
print(p)
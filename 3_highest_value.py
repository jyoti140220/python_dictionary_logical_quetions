a= {
    'a':50, 
    'b':58, 
    'c':56,
    'd':40, 
    'e':100, 
    'f':20
    }
m=0
for x in a:
    if a[x]>m:
        m=a[x]
s=0
for y in a:
    if a[y]<m and a[y]>s:
        s=a[y]
t=0
for z in a:
    if a[z]<s and a[z]>t:
        t=a[z]
print([m,s,t])










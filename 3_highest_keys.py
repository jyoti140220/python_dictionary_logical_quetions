m= {
    'a':50, 
    'b':58,
    'c': 56,
    'd':40,
    'e':100, 
    'f':20
    } 
a=[]
b=[]
for x in m:
    a.append(x)
    b.append(m[x])
i=0
frist_max_value=0
while i<len(b):
    if  b[i]>frist_max_value:
        frist_max_value=b[i]
        frist_max_key=a[i]
    i=i+1
# print(frist_max_value)
# print(frist_max_key)
second_max_value=0
i=0
while i<len(b):
    if b[i]>second_max_value and b[i]<frist_max_value:
        second_max_value=b[i]
        second_max_key=a[i]
    i=i+1
# print(second_max_value)
third_max_value=0
i=0
while i<len(b):
    if b[i]>third_max_value and b[i]<second_max_value:
        third_max_value=b[i]
        third_max_key=a[i]
    i=i+1
print([frist_max_key,second_max_key,third_max_key])


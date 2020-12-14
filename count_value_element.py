a=  {
   'Alex': ['subj1', 'subj2', 'subj3'], 
   'David': ['subj1', 'subj2']}
count=0
for x in a:
    for i in a[x]:
        count=count+1
print("total count :",count)


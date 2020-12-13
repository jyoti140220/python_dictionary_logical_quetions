dic= {
    1: 'NAVGURUKUL',
    2: 'IN',  
  	3:{    
        'A' : 'WELCOME',
        'B' : 'To',
        'C' : 'DHARAMSALA'
      }
        }
# a=[]
# for x in dic:
#   a.append(x)
# i=0
# while i<ldicen(a):
#   if a[i] in dic.keys:
#     print("yes")
#   else:
#     print("no")
#   i=i+1

del dic[3]["A"]
print(dic)
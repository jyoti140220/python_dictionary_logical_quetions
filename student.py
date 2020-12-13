# OUTPUT:-
# {
#     'sonu':85,
#     'Kartik':90,
#     'Deepak':96,
#     'Aman':76,
#     'Somesh':60,
#     'Umesh':85,
#     'Amarpal':70,
#     'Roshan':57,
#     'Riyaz':98,
#     'Shabid':56
# } 

i=1
n={}
while i<=10:
    s=input("enter the student name :")
    m=int(input("enter the marks :"))
    n[s]=m
    i=i+1
print(n)

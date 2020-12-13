a= [
    {
    "name":"komal",
    
    "score":40,
    "school":"pyds"
},
{
    "name":"koma",
    
    "score":40,
    "school":"pyd"
},
{
    "name":"jaya",
    
    "score":60,
    "school":"pyds"
},
{
    "name":"Sonam",
    "score":60,
    "school":"Union"
},
{
    "name":"Akshit",
    "score":50,
    "school":"Summer Fileld school"
}
]
i=0
while i<len(a):
    if a[i]["score"]>50 and a[i]["school"]=="pyds":
        print((a[i]))
    i=i+1
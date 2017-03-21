database=open('db.txt','r')

org_list=[]
address_list=[]

for line in database:
    field=line.split('|')
    if field[1]==" ":
        found=False
    else:
        found=True
        org_list.append(field[1])
        
database=open('db.txt','r')

for line in database:
    field=line.split('|')
    if field[3]=="":
        found=False
    else:
        found=True
        address_list.append(field[3])



if found==False:
    print ("No organisations found in database!")
else:
    print ("Organisations in database: \n")
    for org, address in zip(org_list, address_list):
        print (org.title())
        print ("Address: "+address.title()+'\n')


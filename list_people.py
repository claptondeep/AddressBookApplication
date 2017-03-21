database=open('db.txt','r')

people_list=[]
org_list=[]
phone_list=[]
email_list=[]

for line in database:
    field=line.split('|')
    if field[0]=="":
        found=False
    else:
        found=True
        people_list.append(field[0])

database.close()
    

database=open('db.txt','r')

for line in database:
    field=line.split('|')
    if field[1]=="":
        found=False
    else:
        found=True
        org_list.append(field[1])

database.close()

database=open('db.txt','r')

for line in database:
    field=line.split('|')
    if field[4]=="":
        found=False
    else:
        found=True
        phone_list.append(field[4])

database.close()

database=open('db.txt','r')

for line in database:
    field=line.split('|')
    if field[5]=="":
        found=False
    else:
        found=True
        email_list.append(field[5])

database.close()

        
if found==False:
    print ("No people found in database!")
else:
    print ("People in database: \n")
    for person, org, phone, email in zip(people_list, org_list, phone_list, email_list):
        print (person.title())
        print ("Organisation: "+org.title())
        print ("Work phone number: "+phone)
        print ("Email address: "+email+'\n')
        


database=open('db.txt','r')
lines=database.readlines()
database.close()

org=raw_input("Please enter the name of an organisation you would like to edit\n")
org=org.lower()



for line in lines:
    field=line.split('|')
    if field[1]==org:
        org_addr==[]
        org_addr==field[3]
        found=True
        break
    else:
        found=False
        continue

if found==True:
    choice=raw_input("""Would you like to:
                          1 - Change the name of the organisation
                          2 - Change the organisation address
                          3 - Add a new person to the organisation
Enter 1-3\n""")

    if choice=="1":
        new_org=raw_input("Please enter the new name of the organisation: \n")
        new_org=new_org.lower()
        database=open('db.txt','w')
        for line in lines:
            field=line.split('|')
            if field[1]!=org:
                database.write(line)
            else:
                database.write(field[0]+"|"+new_org+"|"+field[2]+"|"+field[3]+"|"+field[4]+"|"+field[5])
    database.close()

    if choice=="2":
        new_addr=raw_input("Please enter the new organisation address:\n")
        new_addr=new_addr.lower()
        database=open('db.txt','w')
        for line in lines:
            field=line.split('|')
            if field[1]!=org:
                database.write(line)
            else:
                database.write(field[0]+"|"+field[1]+"|"+field[2]+"|"+new_addr+"|"+field[4]+"|"+field[5])
    database.close()


    if choice=="3":
        name=raw_input("Please enter the first and last names of the person to be added to the organisation:\n")
        name=name.lower()
        database=open('db.txt','a')
        for line in lines:
            field=line.split('|')

    if field[1]!=name:
        work_addr=raw_input("Please enter the work address of the person to be added to the organisation\n")
        work_addr=work_addr.lower()
        work_phone=raw_input("Please enter the work phone number of the person to be added to the organisation\n")
        email=raw_input("Please enter the email address of the person to be added to the organisation\n")
        email=email.lower()
        org_addr=raw_input("Please enter the address of the organisation\n")
        database.write(name+"|"+org+"|"+work_addr+"|"+org_addr+"|"+work_phone+"|"+email+"\n")
        print ("Person added to database!")
    database.close()

else:
    if found==False:
        print ("Organisation not found, quitting...")
    

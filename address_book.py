## Application that mimics the back-end of an address book style web application
## Written by Matt Muir
## March 2017

import sys

def main():
    # main function presenting user menu and inputting choice
    print "Welcome to the address book \n"
    print "Please choose from the options below: \n"

    print "[*]1: Search for a person"
    print "[*]2: List organisations"
    print "[*]3: List people"
    print "[*]4: Create organisation"
    print "[*]5: Edit organisation"
    print "[*]6: Delete organisation"
    print "[*]7: Press 'q' to quit\n"

    choice=raw_input("Enter your option \n")
    choice=choice.lower()

    if choice!='q':
        if choice=="1":
            search()
        elif choice=="2":
            list_org()
        elif choice=="3":
            list_people()
        elif choice=="4":
            create_org()
        elif choice=="5":
            edit_org()
        elif choice=="6":
            delete_org()
    else:
        print ("Quitting...")
        sys.exit()
        
        
def search():
    # Function to search for person
    name=raw_input("Please enter the first and last names of the person you want to search for: \n")
    name=name.lower()

    database=open("db.txt", 'r')

    for line in database:
        field=line.split('|')
        if field[0]==name:
            found=True
            break
        else:
            found=False
            continue
    
    name=field[0].title()
    organisation=field[1].title()
    work_address=field[2].title()
    organisation_address=field[3].title()
    work_phone=field[4]
    email=field[5]

    if found==False:
        print("Name not found, try another search term!")
    else:
        print('\nName: '+name)
        print('Organisation: '+organisation)
        print('Work Address: '+work_address)
        print('Organisation Address: '+organisation_address)
        print('Work Phone:  '+work_phone)
        print('Email Address: '+email)

    database.close()

def list_org():
    # Function to list organisations in database
    database=open('db.txt','r')

    org_list=[]
    address_list=[]

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

    database.close()

def list_people():
    # Function to list people in database
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
        
        
def create_org():
    # Function to create organisation in database with option to add person
    database=open("db.txt",'r')

    name=raw_input("Please enter the name of the organisation to be added to the database\n")
    name=name.lower()

    for line in database:
        field=line.split('|')
        if field[1]==name:
            found=True
            break
        else:
            found=False
            continue

    if found==True:
        print("Organisation already in database!\n")
        answer=raw_input("Would you like to add a new person to the organisation? (Y or N)\n")
        answer=answer.lower()
        if answer=="y":
            person=raw_input("Please enter the first and last names of a person to be added to the organisation\n")
            person=person.lower()

            work_addr=raw_input("Please enter the work address of the person to be added to the organisation\n")
            work_addr=work_addr.lower()

            work_phone=raw_input("Please enter the work phone number of the person to be added to the organisation\n")
            work_phone=work_phone.lower()

            email=raw_input("Please enter the email address of the person to be added to the organisation\n")
            email=email.lower()
            
            database=open("db.txt",'a')
            database.write("\n"+person+"|"+name+"|"+work_addr+"|"+org_addr+"|"+work_phone+"|"+email)

        else:
            print "Quitting to main menu"
    else:
        org_addr=raw_input("Please enter the address of the organisation to be added to the database\n")
        org_addr=org_addr.lower()
        answer=raw_input("Would you like to add a person to the organisation? (Y or N)\n")
        if answer=="y":
            person=raw_input("Please enter the first and last names of a person to be added to the organisation\n")
            person=person.lower()

            work_addr=raw_input("Please enter the work address of the person to be added to the organisation\n")
            work_addr=work_addr.lower()

            work_phone=raw_input("Please enter the work phone number of the person to be added to the organisation\n")
            work_phone=work_phone.lower()

            email=raw_input("Please enter the email address of the person to be added to the organisation\n")
            email=email.lower()

            database=open("db.txt",'a')
            database.write("\n"+person+"|"+name+"|"+work_addr+"|"+org_addr+"|"+work_phone+"|"+email)
            database.close()
        else:
            print "Adding organisation"
            database.write("\n |"+name+"| |"+org_addr+"| | ")
            database.close()

def edit_org():
    # Function to edit organisation in database with options to change name, address and add new person
    database=open('db.txt','r')
    lines=database.readlines()
    database.close()

    org=raw_input("Please enter the name of an organisation you would like to edit\n")
    org=org.lower()

    for line in lines:
        field=line.split('|')
        if field[1]==org:
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
            org_addr=org_addr.lower
            database.write("\n"+name+"|"+org+"|"+work_addr+"|"+field[3]+"|"+work_phone+"|"+email+"\n")
            print ("Person added to database!")
        database.close()

    else:
        if found==False:
            print("Organisation not found, quitting...")
             

def delete_org():
    # Function to delete organisation in database
    name=raw_input("Please enter the name of the organisation you would like to delete: \n")
    name=name.lower()

    database=open('db.txt','r')
    lines=database.readlines()

    for line in lines:
        field=line.split('|')
        if field[1]==name:
            found=True
            break
        else:
            found=False
            continue

    if found==False:
        print "Organisation not found!"
        database.close()
    else:
        database=open('db.txt','w')
        for line in lines:
            field=line.split('|')
            if field[1]!=name:
                database.write(line)

        print "Organisation deleted\n"

    database.close()
            
if __name__ == '__main__':
    main()

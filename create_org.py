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

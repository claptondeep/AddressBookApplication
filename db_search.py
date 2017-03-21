name=raw_input("Please enter the first and last name of the person you want to search for: ")
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


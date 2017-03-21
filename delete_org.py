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

        

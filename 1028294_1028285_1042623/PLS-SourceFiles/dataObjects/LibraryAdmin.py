import csv
import json
import Person
import LoanItem

class LibraryAdmin(Person):
    def AddMember(membersList, member):
        membersList.append(member)
        
    def EditMember(membersList, member, newMember):
        membersList.pop(membersList.index(member))
        membersList.append(newMember)
        
    def DeleteMember(membersList, member):
        membersList.pop(membersList.index(member))
        


    def ImportMembers(path):
        with open(path, 'r', newline= '') as csvFile: 
            header = csvFile.readline().split(";")
            memberslist = []
            for line in csvFile:
                fields = line.split(";")
                entry = {}
                for i,value in enumerate(fields):
                    entry[header[i].strip()] = value.strip()
                memberslist.append(entry)
            csvFile.close()
            return memberslist
        
        
    def ExportMembers(membersList, path):
        with open(path, 'w', newline= '') as csvFile: 
            first = True
            for el in membersList:
                if first == True:
                    first = False

                    f = True
                    for key in el:
                        if f == True:
                            f = False
                        else:
                           csvFile.write(';') 
                        csvFile.write(key)
                    csvFile.write('\n')

                f = True
                for key in el:
                    if f == True:
                        f = False
                    else:
                        csvFile.write(';') 
                    csvFile.write(el[key])
                csvFile.write('\n')
            csvFile.close()
        
    def LoanBookItem(loanedItemsList, bookItem, member):
        loanItem = LoanItem(bookItem.objectKey, member.objectKey)
        loanedItemsList.append(loanItem)
        
    def BackupSystem(path):
        print("Creating backup \n")
        
    def RestoreFromBackup(path):
        print("restoring from backup \n")


#    members = ImportMembers("../../Members - Members.csv")
#    members.append({"Number": str(len(members) + 1),"GivenName": "Michael","Surname": "Heerkens","StreetAddress": "Klaverstraat 64","ZipCode": "4322CG","City": "asdf","EmailAddress": "asdf","Username": "aasff","Password": "asdf","TelephoneNumber": "asdfa"})
#    ExportMembers(members, "data/members.csv")

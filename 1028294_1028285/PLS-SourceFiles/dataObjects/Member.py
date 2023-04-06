import Person
class Member(Person):
    firstname = ""
    surname = ""
    address = ""
    zipcode = ""
    city = ""
    email = ""
    phonenumber = -1
    
    def __init__(self):
        print("Inititalize member \n")
        
    def LoanBook():
        return True
    
    def ReturnLoanedItem():
        return True
    
    def Search(membersList, filter):
        return membersList
    

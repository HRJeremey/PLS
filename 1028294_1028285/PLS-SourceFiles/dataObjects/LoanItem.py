class LoanItem:
    bookItemKey = -1
    memberKey = -1
    objectKey = -1
    
    def __init__(self, bookItemKey, memberKey):
        self.bookItemKey = bookItemKey
        self.memberKey = memberKey
        print("Inititalize loan item \n")
    
    def Check(loanItemsList, loanItem):
        print("Check loan item \n")


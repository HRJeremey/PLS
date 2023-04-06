import Book
class BookItem(Book):
    objectKey = -1
    serialNumber = -1
    
    def __init__(self, objectKey, serialNumber):
        self.objectKey = objectKey
        self.serialNumber = serialNumber
        print("Inititalize book item \n")
        
    def Check(bookItemList, key):
        bookItem = bookItemList.index(key);
        return bookItem
    
    def Add(bookItemList, bookItem):
        bookItemList.append(bookItem)
        
    def Edit(bookItemList, bookItem, newBookItem):
        bookItemList.pop(bookItemList.index(bookItem))
        bookItemList.append(newBookItem)
        
    def Delete(bookItemList, bookItem):
        bookItemList.pop(bookItemList.index(bookItem))
        
    def Search(bookItemList, bookItem):
        return bookItemList
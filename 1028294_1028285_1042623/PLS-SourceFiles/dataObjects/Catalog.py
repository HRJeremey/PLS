import json
import os
class Catalog:
    bookList = {}
    bookItemList = {}
    
    def __init__(self):
        with open('data/books.json', 'r') as f:
            data = json.load(f)
            global bookList
            bookList = data
            f.close()
        
    def ShowBookList(self):
        with open('data/books.json', 'r') as f:
            data = json.load(f)
            self.bookList = data
            f.close()
            
       # os.system("cls")
        idx = 0
        for book in self.bookList:
            idx = idx + 1
            print(str(idx) + ". " + book["title"])
        print("\n")

    def AddBook(self):
        newBook = {}
        newBook["author"] = input("Author: ")
        newBook["country"] = input("Country: ")
        newBook["imageLink"] = input("Image link: ")
        newBook["language"] = input("Language: ")
        newBook["link"] = input("Link: ")
        newBook["pages"] = int(input("Pages: "))
        newBook["title"] = input("Title: ")
        newBook["ISBN"] = input("ISBN: ")
        newBook["year"] = int(input("Year: "))
        
        with open('data/books.json', 'r+') as f:
            data = json.load(f)
            f.seek(0)
            data.append(newBook)
            json.dump(data, f)
            f.truncate()
            f.close() 
    
    def EditBook(self):
        self.ShowBookList()
        index = int(input("Select book ID to edit the book: "))
        
        idx = 0
        editBook = {}
        for book in self.bookList:
            idx = idx + 1
            if idx == index:
                editBook = book
            else:
                self.bookList[idx - 1] = book
        
        if editBook == {}:
            return
        
        string = ("Author (Currently: ", editBook["author"], "): ")
        author = input(string)
        if author:
            editBook["author"] = author
            
        string = "Country (Currently: " + editBook["country"] + "): "
        country = input(string)
        if country:
            editBook["country"] = country
            
        string = "Image link (Currently: " + editBook["imageLink"] + "): "
        imageLink = input(string)
        if imageLink:    
            editBook["imageLink"] = imageLink
            
        string = "Language (Currently: " + editBook["language"] + "): "
        language = input(string)
        if language:
            editBook["language"] = language
         
        string = "Link (Currently: " + editBook["link"] + "): "
        link = input(string)
        if link:
            editBook["link"] = link
         
        string = "Pages (Currently: " + str(editBook["pages"]) + "): "
        pages = input(string)
        if pages:
            editBook["pages"] = int(pages)
          
        string = "Title (Currently: " + editBook["title"] + "): "
        title = input(string)
        if title:    
            editBook["title"] = title
            
        string = "ISBN (Currently: " + editBook["ISBN"] + "): "
        ISBN = input(string)
        if ISBN:     
            editBook["ISBN"] = input("ISBN: ")
        
        string = ("Year (Currently: " + str(editBook["year"]) + "): ")
        year = input(string)
        if year:
            editBook["year"] = int(year)
        else:
            editBook["year"] = int(editBook["year"])
            
        with open('data/books.json', 'r+') as f:
            f.seek(0)
            json.dump(self.bookList, f)
            f.truncate()
            f.close() 
        
    def DeleteBook(self):
        self.ShowBookList()
        index = int(input("Select book ID to edit the book: "))
        
        del self.bookList[index - 1]
        
        with open('data/books.json', 'r+') as f:
            f.seek(0)
            json.dump(self.bookList, f)
            f.truncate()
            f.close() 

        
    def AdminMenu(self):
        return {1: {"Show book list": self.ShowBookList}, 2: {"Create new book": self.AddBook}, 3: {"Edit book": self.EditBook}, 4: {"Remove book": self.DeleteBook}}
    
    def MemberMenu(self):
        return {1: {"Show book list": self.ShowBookList}}
class Author:
    def __init__(self,name,age,contry):
        self.name=name
        self.age = age
        self.country = contry
        self.books=[]
        
    def add_book(self,book_title):
        self.books.append(book_title)
class Book:
    def __init__(self, title,published_year):
        self.title=title
        self.published_year=published_year
        
#creating instances and establishing Relationships
author1=Author("George Orwell","25","UK")
author2=Author("Paulo Coelho","47","Brazil")

#adding books to authors
book1=Book("1984",1949)
book2=Book("The Alchemist", 1963)

#Establishing the one to one relationship 
author1.add_book(book1.title)
author1.add_book(book2.title)
author2.add_book(book2.title)

#AcessingRelated data
print(f"Books by {author2.name}:")
for book in author2.books:
    print(book)




        
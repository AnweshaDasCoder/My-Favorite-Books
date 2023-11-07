
class Book: 
    def __init__(self,name,series,author,published,price,genre,longago):
        self.book_name = name
        self.book_series = series
        self.book_author = author
        self.book_published = published
        self.book_price = price
        self.book_genre = genre
        self.book_longago = longago
        
    def add_book(self):
        print("")
        print("Name Of Book: "+self.book_name)
        print("From The Series: "+self.book_series)
        print("Author: "+self.book_author)
        print("Published In: "+self.book_published)
        print("Price Of Book: "+self.book_price)
        print("Genre: "+self.book_genre)
        print("Book Was Published: "+self.book_longago)
        print("Book Added")

book1 = Book("Legends Of Darkstalker", "Wings Of Fire", "Tui T. Sutherland", "June 28, 2016", "$7.39 USD (Amazon: Paperback)", "Fantasy", "7 Years Ago")
book1.add_book()

book2 = Book("Aru Shah And The End Of Time", "Aru Shah: A Pandava Novel", "Roshani Chokshi", "March 27, 2018", "$10.41 USD (Amazon: Hardcover)", "Fantasy", "5 Years Ago")
book2.add_book()

book3 = Book("Tintin In The Land Of Soviets", "The Adventures of Tintin", "Hergé", "January 10, 1929", "$11.69 USD (Amazon: Papaeback)", "Adventure Fiction", "94 Years Ago")
book3.add_book()

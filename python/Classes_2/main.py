from Book import Book

def main():
    book1 = Book("The Cat in the Hat")
    print(book1.getTitle())
    book1.setAuthor("Dr. Seuss")
    print(book1.getAuthor())
    
if __name__ == "__main__":
    main()
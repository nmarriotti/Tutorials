class Book():
    def __init__(self, title):
        print("Book object created.")
        self.title = title
    
    def getTitle(self):
        return self.title

    def setAuthor(self, author):
        self.author = author

    def getAuthor(self):
        return self.author
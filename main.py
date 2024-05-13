def main():
    book = GetText()
    print(book)
    countWords(book)

def countWords(book):
    words = book.split()
    print(len(words))

def GetText():
    with open("books/frankenstein.txt", "r") as book:
        bookText = book.read()
        return bookText
main()

filePath = "books/frankenstein.txt"

def main():
    book = GetText()
    print(f"---Beginning report on {filePath}---")
    print(f"{CountWords(book)} words found in the book\n")

    Display(SortDictionary(CountLetters(book)))

def CountWords(book):
    words = book.split()
    return len(words)

def GetText():
    with open(filePath, "r") as book:
        bookText = book.read()
        return bookText
    
def CountLetters(bookText):
    #return number of times each character appears
    lower = bookText.lower()
    letterCountDict = {}

    for letter in lower:
        letterCount = 0
        if letter in letterCountDict:
            letterCount = letterCountDict[letter]
        letterCountDict[letter] = letterCount + 1
    return letterCountDict

def SortOn(list):
    return list["count"]

def SortDictionary(dict):
    sorted = []
    for letter in dict:
        if letter.isalpha():
            letter_dict = {"letter": letter, "count": dict[letter]}
            sorted.append(letter_dict)
    sorted.sort(reverse=True, key=SortOn)
    return sorted

def Display(sorted):
    for x in sorted:
        print(f"The '{x["letter"]}' character was printed {x["count"]} times")

main()

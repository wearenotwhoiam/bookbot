import sys
import stats

def Display(sorted):
    for letter in sorted:
        print(f"{letter["char"]}: {letter["num"]}")

def DisplayCounts():
    print("============ BOOKBOT ============")
    print("----------- Word Count ----------")
    print(f"Found {stats.count_words(stats.get_book_text(sys.argv[1]))} total words")
    print("----------- Character Count ----------")
    Display(stats.sort_dictionary(stats.count_characters(stats.get_book_text(sys.argv[1]))))
    print("============= END ===============")

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    DisplayCounts()

if __name__ == "__main__":
    main()
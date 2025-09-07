def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def count_words(text):
    return len(text.split())

def count_characters(text):
    letter_count = {}
    for word in text.lower().split():
        for letter in word:
            if letter not in letter_count:
                letter_count[letter] = 1
            else:
                letter_count[letter] += 1
    return letter_count

def sort_on(items):
    return items["num"]

def sort_dictionary(dict_to_sort):
    sorted_list = []
    for letter in dict_to_sort:
        if letter.isalpha():
            letter_dict = {"char":letter, "num":dict_to_sort[letter]}
            sorted_list.append(letter_dict)
    sorted_list.sort(key=sort_on, reverse = True)
    return sorted_list


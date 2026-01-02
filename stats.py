def open_book(path):
    with open(path) as f:
        book = f.read()
        return book

def wordcount(path):
    book = open_book(path)
    return len(book.split())

def lettercount(path):
    book = open_book(path)
    low_book = book.lower()
    letters = dict()
    for letter in low_book:
        if letter not in letters:
            letters[letter] = 1
        else:
            letters[letter] += 1
    return letters

def sort_by_count(dic):
    return dic["num"]

def report_sort(path):
    letters = lettercount(path)

    list_convert = []
    for item in letters:
        if item.isalpha():
            pair = {"char": item, "num": letters[item]}
            list_convert.append(pair)

    list_convert.sort(reverse = True, key = sort_by_count)

    return list_convert
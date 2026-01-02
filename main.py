import sys
from stats import wordcount, lettercount, report_sort

def argparse():
    if len(sys.argv) == 2:
        return sys.argv[1]
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)


def printer(wordnum, reportlist):
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {wordnum} total words")
    print("--------- Character Count -------")
    for lettercount in reportlist:
        print(f"{lettercount["char"]}: {lettercount["num"]}")
    print("============= END ===============")

def main():
    path = argparse()
    wordnum = wordcount(path)
    reportlist = report_sort(path)

    printer(wordnum, reportlist)

main()
from stats import wordcount, lettercount, report_sort

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
    wordnum = wordcount("books/frankenstein.txt")
    reportlist = report_sort("books/frankenstein.txt")

    printer(wordnum, reportlist)

main()
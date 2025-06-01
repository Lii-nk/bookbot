from stats import get_book_words, character_count, characters_sorted
from pathlib import Path
import sys


file = sys.argv[1]
path = Path(sys.argv[1])

#file = '/mnt/c/Users/Sam/Documents/Code/github/bootdotdev/bookbot/books/frankenstein.txt' 
#path = Path("/mnt/c/Users/Sam/Documents/Code/github/bootdotdev/bookbot/books/frankenstein.txt")

def main():
    no_words = get_book_words(file)
    characters = characters_sorted(file)
    location = Path(path.parent.name) / path.name
    print('============ BOOKBOT ============')
    print(f'Analyzing book found at {location}')
    print('----------- Word Count ----------')
    print(f'Found {no_words} total words')
    print('--------- Character Count -------')
    for dict_item in characters:
        print(str(dict_item['char']) + ': ' + str(dict_item['num']))
    print('============= END ===============')




main()

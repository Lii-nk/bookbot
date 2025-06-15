def get_book_text(filepath):
    with open(filepath) as f:
        book_contents = f.read()
        return(book_contents)

def get_book_words(filepath):
        book_words = get_book_text(filepath).split()
        book_words_num = len(book_words)
        return(book_words_num)

def character_count(filepath):
    book_text = get_book_text(filepath).lower()
    character_dict = {}
    for letter in book_text:
        if letter in character_dict:
            character_dict[letter] += 1
        else:
            character_dict[letter] = 1
    return(character_dict)

def sort_on(dict):
    return dict['num']

#sorts cahracters
def characters_sorted(filepath):
    unsorted = character_count(filepath)
    dict_list = []
    for count in unsorted:
        if count == ' ':
            None
        else:
            new_dict_inner = {}
            number = unsorted[count]
            new_dict_inner['char'] = count
            new_dict_inner['num'] = number
            dict_list.append(new_dict_inner)
    dict_list.sort(reverse=True, key=sort_on)
    return(dict_list)


    
    


    

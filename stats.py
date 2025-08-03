def word_count(book):
    word_list = book.split()
    return len(word_list)

def character_count(book):
    lower_book = book.lower()
    character_dict = {}
    for character in lower_book:
        if character in character_dict:
            character_dict[character] += 1
        else:
            character_dict[character] = 1
    return character_dict

def sort_on(items):
    return items["num"]

def sorted_count(character_dict):
    dict_list = []
    for key in character_dict:
        new_dict = {}
        new_dict["char"] = key
        new_dict["num"] = character_dict[key]
        dict_list.append(new_dict)
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list

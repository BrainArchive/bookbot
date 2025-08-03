import sys
from stats import word_count, character_count, sorted_count

def get_book_text(filepath):
    with open(filepath) as f:
        file_content = f.read()
    return file_content

def main():
    if len(sys.argv) != 2:
        print(len(sys.argv))
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file_path = sys.argv[1] 
    text = get_book_text(file_path)
    num_words = word_count(text)
    character_count_dict = character_count(text)
    sorted_dict = sorted_count(character_count_dict)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for dict in sorted_dict:
        if dict["char"].isalpha():
            print(f"{dict["char"]}: {dict["num"]}")
    print("============= END ===============")

main()

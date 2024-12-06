
def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_count = get_num_characters(text)
    print(f"{num_words} words found in the document")

# def sort_on(dict):
#     return dict[]

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_num_words(text):
    words = text.split()
    return len(words)

def get_num_characters(text):
    lower_words = text.lower()

    dict = {}

    for char in lower_words:
        if char.isalpha():
            if char in dict:
                dict[char] += 1
            else:
                dict[char] = 1 

    sorted_list = sorted(dict.items(), key=lambda x: x[0]) 

    for key, value in sorted_list:
        print(f"The '{key}' character was found {value} times.")

    # for i in len(sorted_list):
    #     print(f"The {sorted_list}")





main()
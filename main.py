def main():
    # This function reads the contents of a book file and returns it in a string format to the console.
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    # print(f"{file_contents}")
    return file_contents


def word_count(str):
    # Takes txt from book as string then returns number of words in the string
    words = str.split()
    return len(words)


def num_of_characters(str):
    lower_str = str.lower()
    final_dict = {}

    for i in lower_str:
        if i.isalpha():
            final_dict[i] = final_dict.get(i, 0) + 1

    # Create a new empty list to hold dictionaries
    char_list = []

    for char, count in final_dict.items():
        # Create a new dictionary in the format we want
        char_dict = {"char": char, "num": count}
        char_list.append(char_dict)

    char_list.sort(reverse=True, key=sort_on)

    return char_list


def sort_on(dict):
    return dict["num"]


if __name__ == "__main__":
    file = main()
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count(file)} words found in document")

    character_nums = num_of_characters(file)

    for i in character_nums:
        print(f"The '{i["char"]}' character was found {i["num"]} times")

    print("--- End report ---")


# import string


# def main():
#     book_path = "books/frankenstein.txt"
#     text = get_book_text(book_path)
#     num_words = get_num_words(text)
#     chars_dict = get_chars_dict(text)
#     sorted_chars = sorted(chars_dict.items(), key=filter_and_sort_chars, reverse=True)
#     print(f"{num_words} words found in the document")
#     print(sorted_chars)


# def get_num_words(text):
#     words = text.split()
#     return len(words)


# def get_chars_dict(text):
#     chars = {}
#     for c in text:
#         lowered = c.lower()
#         if lowered in chars:
#             chars[lowered] += 1
#         else:
#             chars[lowered] = 1
#     return chars


# def filter_and_sort_chars(tuple):
#     lrt_keys_dict = {}
#     for i in tuple[0]:
#         if i in string.ascii_letters:
#             lrt_keys_dict[i] = tuple[1]
#     return lrt_keys_dict


# def get_book_text(path):
#     with open(path) as f:
#         return f.read()


# main()


def get_word_count(string_text):
    words = string_text.split()
    return len(words)

def main():
    path_to_file = "books/Frankenstein.txt"
    file_string = ""
    with open(path_to_file) as f:
        file_contents = f.read()

    file_string += file_contents

    print(f'--- Begin report of {path_to_file} ---')
    print(f"{get_word_count(file_string)} words found in the document")
    print("")

    char_count = get_char_count(file_string.lower())
    for (k,v) in char_count:
        print(f"The '{k}' character was found {v} times")

    print("--- End report ---")


def get_char_count(string_text):
    words = string_text.split()
    char_string_text = "".join(words)

    chars = {}

    for c in char_string_text:
        if c.isalpha() :
            if not c in chars:
                chars[c] = 0
            chars[c] += 1


    sorted_chars = sorted(chars.items(), key=lambda item: item[1], reverse=True)

    return sorted_chars


main()
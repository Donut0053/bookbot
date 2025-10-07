def get_num_words(book):
    with open(f"/home/denver/webflyx/bookbot/books/{book}.txt") as f:
        file_contents = f.read()
        words = file_contents.split()
        num_words = len(words)
    return num_words, file_contents


def get_num_letters(text):
    letter_count = {}
    for char in text.lower():
        if char in letter_count:
            letter_count[char]+= 1
        else:
            letter_count[char] = 1

    return letter_count

def dict_to_list(counts):
    made_list = []
    for char, num in counts.items():
        if not char.isalpha():
            continue
        made_list.append({"char": char, "num": num})
    made_list.sort(key=lambda X:  X["num"], reverse=True)
    return made_list


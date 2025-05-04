def get_word_count(text):
    words = text.split()
    return len(words)

def get_char_count(text):
    count_dict = {}
    for char in text:
        char = char.lower()
        if char not in count_dict:
            count_dict[char] = 0
        count_dict[char] += 1
    return count_dict

def sort_dict(dict):
    sorted_list = []
    for char in dict:
        if not char.isalpha():
            continue
        sorted_list.append({ "char": char, "count": dict[char]})
    sorted_list.sort(key=lambda x: x["count"], reverse=True)
    return sorted_list
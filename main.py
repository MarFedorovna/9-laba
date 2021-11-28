def sort_sentence(sentence):
    list_of_words = sorted(sentence.split(), key=len)
    new_string_with_lower_char = ' '.join(list_of_words).lower()
    answer_string = new_string_with_lower_char[0].upper() + new_string_with_lower_char[1:]
    return answer_string

if __name__ == '__main__':
    s = input("Введите строку для сортировки: \n")
    print(sort_sentence(s))

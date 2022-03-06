def print_word(word, number):
    word1 = word[0:number]
    word2 = word[number:len(word)]
    print(f"{word1.upper()}{word2}")


word_ = input("enter word here: ")
number_ = int(input("number of chars to capitalise: "))
print_word(word_, number_)


def starts_with_a(word):
    if word[0] == "A":
        return True
    else:
        return False


# main routine
word_to_check = input("enter the word ").upper()
print(starts_with_a(word_to_check))

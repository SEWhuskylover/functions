def longest_word(word_list):
    longest = [""]
    for word in word_list:
        if len(word) > len(longest[0]):
            longest = [word]
        elif len(word) == len(longest[0]):
            longest.append(word)
    return longest

# main


words = []
word_ = ""
while word_ != "1":
    word_ = input("add word to list or 1 to end: ")
    words.append(word_)

print(f"the longest word in the list{words} is {longest_word(words)}")

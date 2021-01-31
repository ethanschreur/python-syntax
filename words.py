def print_upper_words(my_list, must_start_with):
    '''for every string in my_list, print that string in all uppercase letters'''
    for word in my_list:
        word = word.upper()
        if word[0] in must_start_with or word[0].lower() in must_start_with:
            print(word)
print_upper_words(['ello', 'hey', 'yo', 'yes'], {"h", "y"})


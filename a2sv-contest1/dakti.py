for _ in range(int(input())):
    string = input()
    stringList = string.split()
    list_str = [None] * len(stringList)

    for word in stringList:
        num = ""
        new_word = ""
        for char in word:
            if char.isdigit():
                num += char
            else: new_word += char
        list_str[int(num)-1] =  new_word
    print(' '.join(list_str))
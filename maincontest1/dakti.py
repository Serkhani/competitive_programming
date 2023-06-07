for _ in range(int(input())):
    string = input()
    stringList = string.split()
    list_str = []

    for word in stringList:
        for chIdx in range(len(word)):
            if word[chIdx].isdigit():
                i = 1
                while (not word[chIdx:].isdigit()) and word[chIdx: chIdx+i].isdigit():
                    i+=1
                list_str.insert(int(word[chIdx: chIdx+i-1])-1, word.replace(word[chIdx: chIdx+i-1],''))
                chIdx += i
                print(f'chIdx2: {chIdx}')
                break
    print(' '.join(list_str))
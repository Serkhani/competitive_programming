n = int(input())
patterns = [input() for _ in range(n)]
pattern = ""

for i in range(len(patterns[0])):
    characters = set(pattern[i] for pattern in patterns)
    if len(characters) == 1:
        if '?' in characters:
            pattern += 'x'
        else: pattern += characters.pop()
    elif len(characters) > 2:
        pattern += '?'
    else:#len(characters) == 2
        if '?' in characters: 
            for ch in characters:
                if ch != '?':
                    pattern += ch
                    break
        else: 
            pattern += '?'

print(pattern)

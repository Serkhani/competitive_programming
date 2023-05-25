def swap_case(s):
    res_str = ""
    for i in s:
        if i == i.upper():
            res_str += i.lower()
        else:
            res_str += i.upper()
    return res_str
if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
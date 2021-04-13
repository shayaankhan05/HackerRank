def swap_case(s):
    r = ""
    for i in range(len(s)):
        if(s[i].isupper()):
            r += s[i].lower()
        elif(s[i].islower()):
            r += s[i].upper()
        else:
            r += s[i]
    return r


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)

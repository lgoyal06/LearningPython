def swap_case(s):
    mystr=""
    for ch in s:
        code = ord(ch)
        if code >= 65 and code <=90:
            mystr = mystr+chr(code+32)
        elif code >= 97 and code <=122:
            mystr = mystr+chr(code-32)
        else:
            mystr = mystr+ch
    return mystr

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)

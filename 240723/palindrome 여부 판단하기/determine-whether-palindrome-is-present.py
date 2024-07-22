str_ = input()

def palindrome(str):
    if str == str[::-1]:
        print('Yes')
    else:
        print('No')

palindrome(str_)
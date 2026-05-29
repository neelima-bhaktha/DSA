def is_palindrome(string):
    strng1= string[::-1]
    if string != strng1:
        return False
    else:
        return True

assert is_palindrome("abcd") == False
assert is_palindrome("mom") == True
print("all test cases passed")
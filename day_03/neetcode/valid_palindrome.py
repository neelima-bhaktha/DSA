def valid_palindrome(str):
    cleaned = ""
    for char in str:
        if char == " ":
            continue
        elif char.isalnum():
            cleaned += char.lower()

    return cleaned == cleaned[::-1]

assert valid_palindrome("was it a car or a cat i saw?") == True
print("passed")
def palindrome(word: str) -> bool:
    word = word.lower()
    return word[::-1] == word


print(palindrome("Mother"))
print(palindrome("Mom"))

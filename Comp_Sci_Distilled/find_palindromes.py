#a function that uses recursion to find palindromes

def palindrome(word):
    if len(word) <= 1:
        return True
    elif len(word) == 2:
        if word[0] == word[-1]:
            return True
        else:
            pass
    elif word[0] != word[-1]:
        return False
    word = word.lstrip(word[0])
    word = word.rstrip(word[-1])
    return palindrome(word)


print(palindrome(input("Type the word you want to test for palindrome characteristics: ")))

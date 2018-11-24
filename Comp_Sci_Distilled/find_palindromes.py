#!C:\Users\kruser\PycharmProjects\Comp_Sci_Distilled python
#a function that uses recursion to find palindromes

def palindrome(n):
    """receives an input and checks to see if it's a palindrome"""
    n = n.replace(" ", "")
    n = n.replace(",", "")
    n = n.lower()
    if len(n) <= 1:
        return True
    elif len(n) == 2:
        if n[0] == n[-1]:
            return True
        else:
            pass
    elif n[0] != n[-1]:
        return False
    n = n.lstrip(n[0])
    n = n.rstrip(n[-1])
    return palindrome(n)


print(palindrome(input("Type the word or phrase you want to test for palindrome characteristics: ")))

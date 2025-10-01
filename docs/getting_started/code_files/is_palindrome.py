def is_palindrome(word):
    # intentional bugs: 
    #   - accepts all words with odd length as palindromes
    #   - is not case-insensitive for palindromes with even length
    if len(word) % 2 != 0 or word == word[::-1]:
        return True
    else:
        return False

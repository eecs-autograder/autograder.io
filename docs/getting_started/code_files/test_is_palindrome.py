from is_palindrome import is_palindrome

def test_is_palindrome():
    palindromes = [
        'abba',
        'Abba',
        'abcba'
    ]

    not_palindromes = [
        'abc',
        'ab',
    ]

    # Start with fullpoints and subtract 1 for each incorrect result
    score = 5
    for word in palindromes:
        # we want to make sure that student code doesn't crash the program,
        # preventing us from outputting a score (or worse, them outputting their
        # own score and then crashing the program)
        try:
            if not is_palindrome(word):
                score -= 1
                print("-1: {} is a palindrome,".format(word),
                      'but is_palindrome("{}") returned False'.format(word))
        except:
            score -= 1
            print("-1: is_palindrome({}) raised an exception".format(word))

    for word in not_palindromes:
        # we want to make sure that student code doesn't crash the program,
        # preventing us from outputting a score (or worse, them outputting their
        # own score and then crashing the program)
        try:
            if is_palindrome(word):
                score -= 1
                print("-1: {} is not a palindrome,".format(word),
                      'but is_palindrome("{}") returned True'.format(word))
        except:
            score -= 1
            print('-1: is_palindrome("{}") raised an exception'.format(word))

    print("<!! score: {} !!>".format(score))

if __name__ == '__main__':
    test_is_palindrome()

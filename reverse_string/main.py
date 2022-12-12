def reverse(word: str):
    """
    Directions:
        Given a string, return a new string with the reversed
        order of characters
    Examples:
        reverse('apple') === 'leppa'
        reverse('hello') === 'olleh'
        reverse('Greetings!') === '!sgniteerG'
    """
    return word[::-1]


if __name__ == '__main__':
    print(reverse('apple'))

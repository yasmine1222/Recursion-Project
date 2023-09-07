# Script includes syntax errors
"""
This program converts an inputted word into a format common in a Swedish
word game (Rovarkspraket).
The rules are:
  1. Each consonant is doubled and the supplied letter
     is inserted between the doubled consonant 
     (e.g. "n" becomes "non" when "o" is supplied)
  2. Pre-existing vowels remain untouched
"""

def convert(letter, word):
    """Transforms the word using the rules of Rovarkspraket.
    The supplied letter is used as the separator.
    """
    for char in range(word)
        if char in 'aeiou':
            answer += char
        else:
            answer += char + letter + char
    return answer


def test(ltr, wrd):
    """Calls convert on ltr and wrd and prints the return value."""
    rovarks = convert(ltr,wrd
    print("Let's call convert on " + ltr + " and " + wrd)
    print("  it returns " + rovarks)


if __name__ == "__main__":
    test_cases = [['u', ''], ['o', 'stubborn'], ['o', "pp"]]
    for letter, word in test_cases:
        test(letter, word)

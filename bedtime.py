"""
Lab 7, Task 1

Accumulating recursion with lists of strings.
Inspired by https://stackoverflow.com/questions/3021/what-is-recursion-and-when-should-i-use-it
"""

def first_sentence(object, subject):
    """Given the strings object and subject, return a string representing the
    first sentence of the story about those characters. DO NOT MODIFY."""
    return  "The mother of the " + object + " told " + \
            "a story about a " + subject + "..."

def last_sentence(object):
    """Given the string object, return a string representing the second (last)
    sentence of the story about that character.  DO NOT MODIFY."""
    return "and then the " + object + " fell asleep."

def bedtime_story(characters):
    """
    Main (recursive) function for producing a bedtime story based on a list of
    strings (story characters). Returns a list of strings where each element is
    a sentence in the bedtime story.

    >>> bedtime_story(['ant', 'fly'])
    ['The mother of the ant told a story about a fly...', 'and then the ant fell asleep.']
    >>> bedtime_story(['li', 'pi'])
    ['The mother of the li told a story about a pi...', 'and then the li fell asleep.']
    """
    #initialize a base case
    if len(characters) <2:
        return []
    #recursive call
    else:
        object = characters[0]
        subject =characters[1]
        #we call on our recursive function to do the work 
        return [first_sentence(object, subject)] + bedtime_story(characters[1:]) + [last_sentence(object)]

def format_print(story_list):
    """Given a list of strings as story list, prints out the full story to the
    terminal in a nicely indented fashion.  DO NOT MODIFY."""
    n = len(story_list)

    # Print the first half of the list, with increasing indentation.
    for i in range(n // 2):
        print("   " * i + story_list[i])

    # Print the second half of the list, with decreasing indentation.
    for i in range(n // 2, n):
        print(("   " * (n - i - 1)) + story_list[i])

# Run the doctests, and also generate a list of characters from you provide
# when you run your program from the terminal.  Eg:
# 
#    python3 bedtime.py parrot flamingo heron cow
#
if __name__ == "__main__":
    """Testing code.  DO NOT MODIFY."""
    from doctest import testmod
    testmod()

    from sys import argv
    chars = argv[1:]
    format_print(bedtime_story(chars))

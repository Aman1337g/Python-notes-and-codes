def rev(s):
    '''Reversing a string s ''' '''Hahahaha!!!'''
    '''Creating an empty string s1'''
    s1 = ""
    for i in s:
        s1 = i + s1  # '''reversing logic'''
    # print(s1)
    return s1


def chk_palindrome(s):
    '''Taking a string and checking if it's a palindrome or not

Hello user, Welcome!!'''
    if s == rev(s):
        print(f"{s} is Palindrome!!")
    else:
        print(f"{s} is Not Palindrome!!")


s = 'Aman Kumar Gupta'
print(rev(s))
chk_palindrome(s)
print()
s1 = 'racecar'
print(rev(s1))
chk_palindrome(s1)

# Docstring
print(rev.__doc__)
print(chk_palindrome.__doc__)
'''
OUTPUT

atpuG ramuK namA
Aman Kumar Gupta is Not Palindrome!!

racecar
racecar is Palindrome!!
Reversing a string s Hahahaha!!!
Taking a string and checking if it's a palindrome or not

Hello user, Welcome!!
'''

# Example


def add(num1, num2):
    """
    Add up two integer numbers.

    This function simply wraps the ``+`` operator, and does not
    do anything interesting, except for illustrating what
    the docstring of a very simple function looks like.

    Parameters
    ----------
    num1 : int
        First number to add.
    num2 : int
        Second number to add.

    Returns
    -------
    int
        The sum of ``num1`` and ``num2``.

    See Also
    --------
    subtract : Subtract one integer from another.

    Examples
    --------
    >>> add(2, 2)
    4
    >>> add(25, 0)
    25
    >>> add(10, -10)
    0
    """
    return num1 + num2


print(add(4, 5))
print(add.__doc__)
'''
OUTPUT

9

    Add up two integer numbers.

    This function simply wraps the ``+`` operator, and does not
    do anything interesting, except for illustrating what
    the docstring of a very simple function looks like.

    Parameters
    ----------
    num1 : int
        First number to add.
    num2 : int
        Second number to add.

    Returns
    -------
    int
        The sum of ``num1`` and ``num2``.

    See Also
    --------
    subtract : Subtract one integer from another.

    Examples
    --------
    >>> add(2, 2)
    4
    >>> add(25, 0)
    25
    >>> add(10, -10)
    0

'''

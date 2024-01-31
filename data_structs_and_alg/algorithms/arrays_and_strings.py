import numpy as np


def is_unique(s: str) -> bool:
    """
    Returns true if s has all unique characters

    Time complexity: We need to loop through all the characters of s
        to check if there's a duplicate. Getting and inserting into
        a python dictionary is performed in constant time. Time complexity
        is O(n)

    Space complexity: We need to store all the characters of s into a dictionary,
        which takes O(n) space.

    """

    ht = {}
    for char in s:
        if ht.get(char, None) is not None:
            return False
        ht[char] = 1
    return True


def is_unique_no_data_struct(s: str) -> bool:
    """
    The only way too tell if a string is unique or not is by
    keeping some kind of memory of the characters you've seen before.
    Without a data structure, that isn't possible. The only solution
    is to sort the string, then check if adjacent characters are the same

    Time complexity: Sorting takes O(nlogn)

    Space complexity: We're storing the sorted string into a variable. Space
        complexity remains O(n)
    """

    sorted_s = ''.join(sorted(s))
    for i in range(len(sorted_s) - 1):
        if sorted_s[i] == sorted_s[i + 1]:
            return False
    return True


def check_permutation(s1: str, s2: str) -> bool:
    """
    Returns True if s1 is a permuation of s2. s1 is a permuation
    of s2 (and vice versa) if s1 and s2 have the exact same characters
    and the exact same character count.

    Time complexity: s1 and s2 need to have the same length if they're
        permutations of each other. We need to loop through s1 and s2, both
        of size n, so time complexity is O(n). If one makes the assumption
        that both s1 and s2 are ASCII strings, then one can argue that the time
        compelxity is O(128*2) == O(1)

    Space complexity: We create one array of size 128, O(1)
    """
    if len(s1) != len(s2):
        return False

    char_count = [0] * 128

    for char in s1:
        char_count[ord(char) - ord('a')] += 1

    for char in s2:
        char_count[ord(char) - ord('a')] += 1

    return sum(char_count) % 2 == 0


def urlify(s: str) -> str:
    """
    Returns s with all spaces relaced with '%20'.

    Time Complexity: Have to loop through all characters of s
        to find the spaces. O(n)
    Space Complexity: Storing result into a string of size n. O(n)
    """
    result = ''
    s_stripped = s.strip()
    for char in s_stripped:
        if char == ' ':
            result += '%20'
        else:
            result += char
    return result


def palindrome_permutation(s: str) -> bool:
    """
    Returns true if s is a permutation of a palindrome. s is a
    palindrome if it's read in the same way both forward and backward.
    For s to be a palindrome, it has to have an even number of each character,
    except for one (middle character)

    Time Complexity: Have to loop over all the characters of s. O(n)

    Space Complexity: Assuming s is ASCII, char_count will have a max size
    of 128, so space is O(1). If this assumption doesn't hold, then O(c) where
    c is the max number of characters in the encoding scheme of s.
    """
    s = s.lower().replace(' ', '')
    char_count = {char: 0 for char in s}
    num_odd = 0
    for char in s:
        char_count[char] += 1
    for count in char_count.values():
        if count % 2 != 0:
            num_odd += 1
        if num_odd > 1:
            return False
    return True


def one_way(s1: str, s2: str) -> bool:
    """
    Returns True if s1 and s2 are one edit away from eachother.

    Time Complexity: len(s1) <= len(s2) <= 1, so in the worst case len(s1) == len(s2) -1,
        or vice versa. We can say O(n) because we have to loop through all the characters

    Space Complexity: O(1) assuming s1 and s2 are ASCII encoded, O(n) otherwise.
    """

    if abs(len(s1) - len(s2)) > 1:
        return False

    s1_arr = [0] * 128
    s2_arr = [0] * 128

    for char in s1:
        s1_arr[ord(char) - ord('a')] += 1
    for char in s2:
        s2_arr[ord(char) - ord('a')] += 1
    return np.sum(np.abs(np.subtract(s1_arr, s2_arr))) <= 2

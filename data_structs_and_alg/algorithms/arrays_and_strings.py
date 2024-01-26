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

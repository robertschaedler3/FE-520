'''
    name: assignment_2.py
    author: Robert Schaedler III
    date: 3/11/2020
    pledge: I pledge my honor that I have abided by the Stevens Honor System.
'''

import string
import collections


def Ball_Drop(height, drop_num):
    while drop_num > 0:
        drop_num -= 1
        height *= 0.25
    return height


def Get_Token(given_string):
    words = given_string.split()
    freq = collections.defaultdict(int)

    for word in words:
        # remove punctuation
        for c in string.punctuation:
            word = word.replace(c, "")
        word = word.lower()
        freq[word] += 1

    return dict(freq)


def Step_2_Fibo(num, isIncrement=True):
    if num == 0 or num == 1:
        return 0
    a, b, c = 0, 1, 1
    while c < num:
        a, b, c = b, b + a, c + b

    if num == c:
        return 0
    return (c - num) if isIncrement else (num - b)


def identi_Substring(given_string):
    str_len = len(given_string)
    if str_len == 0:
        return 0

    substr_count = 0

    i, j = 0, 1
    while j < str_len:
        if given_string[i] == given_string[j]:
            j += 1
        else:
            diff = j - i
            substr_count += (diff * (diff + 1)) / 2
            i, j = j, j + 1

    rem = str_len - i
    substr_count += (rem * (rem + 1)) / 2
    return int(substr_count)


if __name__ == "__main__":

    # Test Question 1
    Heights = 100
    drop_num = 3

    print("\nQ1")
    Heights_after = Ball_Drop(Heights, drop_num)
    print(Heights_after)

    Given_str_1 = '''
    "He has indicated he is prepared to sign the bill.
    He will also be issuing a national emergency declaration at the same time,"
    McConnell said. "I've indicated to him that I'm going to support the national emergency
    declaration. So for all of my colleagues, the President will sign the bill.
    We will be voting on it shortly."
    '''

    print("\nQ2")
    res_dict = Get_Token(Given_str_1)
    print(res_dict)

    # test question 3
    print("\nQ3")
    print(Step_2_Fibo(5, False))

    print("\nQ4")
    print(identi_Substring('zzzyz'))

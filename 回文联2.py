def palindrome(string):
    list1 = list(string)
    list2 = reversed(list1)
    if list1 == list(list2):
        return '是回文联'
    else:
        return '不是回文联'


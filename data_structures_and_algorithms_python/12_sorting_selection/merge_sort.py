"""
My Implementation of merge-sort

"""


def merge(s1, s2, s):
    """ Merges two previously sorted seq S1 and S2 """
    i = j = k = 0

    while i + j < len(s):
        if j == len(s2) or i < len(s1) and s1[i] < s2[j]:
            s[k] = s1[i]
            i += 1
        else:
            s[k] = s2[j]
            j += 1
        k += 1
    # return s


def merge_sort(s):
    """ Divide and conquer merge sort algorithm """
    n = len(s)

    if n <= 1:
        return

    # divide
    mid = n // 2
    s1 = s[0:mid]
    s2 = s[mid:n]

    # conquer (with recursion)
    merge_sort(s1)
    merge_sort(s2)

    # merge results into s
    merge(s1, s2, s)




if __name__ == '__main__':
    s1 = [1, 3, 5]
    s2 = [2, 4, 6]
    s = s1 + s2
    print("First s: ", s)
    # print(merge(s1, s2, s))
    print(merge_sort(s))
    print(s)


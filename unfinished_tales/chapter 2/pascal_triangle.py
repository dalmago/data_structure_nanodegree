
def next_row_pascal(l, n):
    if n == 0:
        return l

    new_list = []
    for i in range(len(l)):
        if i == 0:
            new_list.append(1)
        else:
            new_list.append(l[ i -1] + l[i])

    new_list.append(1)

    return next_row_pascal(new_list, n-1)


def nth_row_pascal(n):
    """
    :param: - n - index (0 based)
    return - list() representing nth row of Pascal's triangle
    """
    return next_row_pascal([1], n)

print(nth_row_pascal(4))

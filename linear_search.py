def linear_search(li, val):
    for ind, v in enumerate(li):
        if v == val:
            return ind
    return None


print(linear_search([1, 2, 3, 4, 5, 6, 7], 3))

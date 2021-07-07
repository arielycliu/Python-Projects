
def solution(x, y):
    if len(y) > len(x):
        x, y = y, x
    ID = [n for n in x if n not in y]
    for n in ID:
        return n

# def solution(list1, list2):
#     if len(list2) > len(list1):
#         list2, list1 = list1, list2
#
#     for n in list1:
#         if len(list1) == 1:
#             return n
#         try:
#             list2.remove(n)
#         except:
#             return n

def test():
    assert solution([13, 5, 6, 2, 5], [5, 2, 5, 13]) == 6
    assert solution([14, 27, 1, 4, 2, 50, 3, 1], [2, 4, -4, 3, 1, 1, 14, 27, 50]) == -4
    assert solution({13, 5, 6, 2, 5}, {5, 2, 5, 13}) == 6
    assert solution({14, 27, 1, 4, 2, 50, 3, 1}, {2, 4, -4, 3, 1, 1, 14, 27, 50}) == -4
    assert solution([5], []) == 5
    assert solution([5, 6], [6]) == 5
    assert solution([7, 5], [5]) == 7

test()

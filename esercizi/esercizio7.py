'''
Write a Python program to find elements in a given set that are not in another set.
'''


def find_diff(set1, set2):
    diff = []
    for i in set1:
        if i not in set2:
            diff.append(i)
    return set(diff)


sn1 = {1, 2, 3, 4, 5}
sn2 = {4, 5, 6, 7, 8}

print(find_diff(sn1, sn2))
print(find_diff(sn2, sn1))
print(sn1.difference(sn2))
print(sn2.difference(sn1))
print(sn1 - sn2)
print(sn2 - sn1)

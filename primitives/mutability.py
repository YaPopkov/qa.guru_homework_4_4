# Списки, словари и множества - изменяемые!

from copy import deepcopy


a = [1, 2, 3]
b = a.copy()
b.append(4)

print(a)
print(b)


a = [1, 2, 3, [4, 5, 6]]
b = deepcopy(a)
b[-1].append(7)

print(a)
print(b)


# Кортежи, frozenset  - нет

print(frozenset([1, 2, "3", 4, 5]))

a = (1, 2, 3, "4", "5")


d = {"key": "value", "first": "second"}
dd = (("key", "value"), ("first", "second"))
print()

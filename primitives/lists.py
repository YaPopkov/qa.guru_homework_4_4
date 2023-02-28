
# Делаем списки!

l = []
l = [1, 2, 3, 4, 5]
l = [1, 2, 3, "4", "5", [1, 2, 3]]

print(l[-1][2])

# Функции списков

l[0] = 10
print(l)

zero_element = l.pop(0)
l.extend([1, 2, 3])
print(l)

# "\n".join(l)

print(list("abcdef"))


# Множества

s = set([10, 9, "2", 5, 5, 3])
ss = s | {1, 2}
ss = s & {1, 2}

print(s)

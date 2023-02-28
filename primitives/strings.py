"""
Это примеры работы со строками
"""
# Учимся писать строки!

s = "Hello, 'world'!"
print(s)

s = 'Hello, "world"!'
s = """'Hello', "world"!"""
s = '''Hello """,""" world!'''
s = "Hello, \"world\"!"

s = "Hello, \nworld!"
s = """Hello,
World!"""
print(s)

# Сырые строки

s = r"\n\n\n\\n\n\n\n\n"

# Индексы и слайсы

s = "abcdefg"
print(s[0])
print(s[3])
print(s[-1])

print(s[1:5])
print(s[0:5:2])
print(s[::-1])

print(len(s))

# Оперируем

s = "abcdefgggg".title()
s = s.strip("ag")
print(s)

# Форматируем

hello = "Hello"
world = "world"
s = hello + ", " + world + "!"
print(s)

s = f"{hello}, {world.upper()}!"
s = "{}, {}!".format(hello, world)
s = "{w}! {h}, {w}!".format(h=hello, w=world)
print(s)

url_template = "https://google.com/{}"

url_template.format("my_address")
url_template.format("another_address")

# Строку в число, и наоборот

a = 123
s = "123"

assert int(s) == 123
assert s == str(a)


"abcdefg".split()
# Заводим словарики

d = {
    "name": 'Oleg',
    "age": 28,
    "married": True
}

name = d["name"]
print(name)

d["age"] += 1

# Функции словарей

d.items()
d.keys()
d.values()

print(d.get("age", "default value"))
print(d.get("unexpected", "default value"))

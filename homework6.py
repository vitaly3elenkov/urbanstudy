my_dict={"Иван, год рождения-":1990, "Василий, год рождения-":2000}
print(my_dict)

print("Существующий ключ:",my_dict["Иван, год рождения-"])
print("Не существующий ключ:",my_dict.get("Василиса, год рождения-"))

my_dict.update({"Гоша, год рождения-":1980, "Петя, год рождения-":2005})
print(my_dict)
my_dict.pop("Петя, год рождения-")
print(my_dict)

my_set={9,8,7,7,8,9}
print(my_set)
my_set.add(4)
my_set.add(5)
print(my_set)
my_set.discard(7)
print(my_set)

Author="Zelenkov Vitaly"
print("ДЗ №5 выполнил:",Author)






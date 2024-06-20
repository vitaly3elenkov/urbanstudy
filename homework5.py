immutable_var=(1,2,"a,b,c")
print("Кортеж:", immutable_var)
#immutable_var[0]=1000 # кортеж - это неизменяемые упорядоченные коллекции элементов. Попытка изменения приведет к ошибке
mutable_list=(10,9,8)
print("Неизменяемый списк:",mutable_list )
mutable_list1=([10,9],8)
mutable_list1[0][0] =6
mutable_list1[0][1] =7
print("Изменяемый список:",mutable_list1)

Author="Zelenkov Vitaly"
print("ДЗ №5 выполнил:",Author)
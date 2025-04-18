'''
Списки
len() - определение длинны списка
max() - для нахождения макс значения
min() - для нахождения мин значения
sum() - для вычисления суммы
sorted() - для сортировки

+ -соединение двух списков в один
* -дублирование списка
in -проверка вхождения элемента в список
del -удаление элемента списка
'''

numbers = [1, 24, 3, 44, 15, 236, 72, 8, 9]
print(sorted(numbers))
print(sorted(numbers, reverse=True)) # Меняет порядок теперь от большего к меньшему

numbers_second = [111, 223]
print(sorted(numbers_second + numbers)) # Плюсуем два листа и сортируем все числа по порядку

vegetables = ["carrot", "onion", "brocoli", "pee"]
print("pee" in vegetables) # Проверяем наличие элемента в списке
# Or
print("strawberry" not in vegetables) # Проверяем отсутствие элемента в списке

print(sum(numbers)) # Сумма всех элементов

print(max(numbers)) # Макс элемент

fruits = ["apple", "banana", "cherry"]
fruits.insert(0, "orange") # Вставляет на позицию одного элемента другой
print(fruits)

fruits.remove("orange") # Удаляет выбранный элемент
print(fruits)

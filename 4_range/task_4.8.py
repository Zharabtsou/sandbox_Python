#возводим в квадрат и кубы)

print(2**2) #2 на конце это квадрат
print(2**3) #3 на конце возведение в куб и т.д
list_items = []
for item in range(1,11):
    list_items.append(item**3)

print(list_items)
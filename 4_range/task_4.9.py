
#генератор кубов)
list_item = [item**3 for item in range(1,11)]
print(list_item)

#генератор кубов range можно и с одни числом но тогда отсчет начнется с 0
list_item = [item**3 for item in range(11)]
print(list_item)
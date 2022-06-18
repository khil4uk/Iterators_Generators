nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None],
]

# Задание 1 (Iterators)
class FlatIterator:

    def __init__(self, new_list):
        """Определение атрибута нового списка"""
        self.new_list = new_list

    def __iter__(self):
        """Определение атрибута иттерации списка"""
        self.first_cursor = 0
        self.second_cursor = -1 # смещаем курсор на одну позицию для отображения всех элементов списка
        return self

    def __next__(self):
        """Определение и возвращение каждого элемента списка"""
        self.second_cursor += 1
        if len(self.new_list[self.first_cursor]) == self.second_cursor:
            self.first_cursor += 1
            self.second_cursor = 0
        if len(self.new_list) == self.first_cursor:
            raise StopIteration
        return self.new_list[self.first_cursor][self.second_cursor]


for item in FlatIterator(nested_list): # вызов иттератора
    print(item)

print("-"*40)
print()

flat_list = [item for item in FlatIterator(nested_list)] # comprehension выражение
print(flat_list)

print("-"*40)
print()

# Задание 2 (Generators. Yield)
def flat_generator(new_list):
    """Генератор, который принимает список списков и возвращает их плоское представление"""
    for second_list in new_list:
        for item in second_list:
           yield item

for item in flat_generator(nested_list):  # вызов генератора
    print(item)
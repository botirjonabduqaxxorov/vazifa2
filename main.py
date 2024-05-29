# 1
# class MyRange:
#     def __init__(self, start, end):
#         self.current = start
#         self.end = end

#     def __iter__(self):
#         return self

#     def __next__(self):
#         if self.current >= self.end:
#             raise StopIteration
#         else:
#             current = self.current
#             self.current += 1
#             return current

# my_range = MyRange(1, 5)

# for number in my_range:
#     print(number)


# 2
# class IterableClass:
#     _instances = []  # Barcha yaratilgan obyektlarni saqlash uchun

#     def __init__(self, name):
#         self.name = name
#         self._instances.append(self)

#     @classmethod
#     def __iter__(cls):
#         return iter(cls._instances)

# # Obyektlarni yaratish
# obj1 = IterableClass("Obj1")
# obj2 = IterableClass("Obj2")
# obj3 = IterableClass("Obj3")

# # Iteratsiya qilish
# for obj in IterableClass:
#     print(obj.name)







# 3
# class MyIterableClass:
#     # Class-level ro'yxat
#     _instances = []

#     def __init__(self, value, category):
#         self.value = value
#         self.category = category
#         # Har bir yangi obyektni class-level ro'yxatga qo'shamiz
#         MyIterableClass._instances.append(self)

#     # Bu metod barcha ob'ektlarni iteratsiya qilishni boshlash uchun kerak
#     def __iter__(self):
#         # Iterator obyektini qaytarish
#         return MyIterableClassIterator(MyIterableClass._instances)

#     @classmethod
#     def filter(cls, **kwargs):
#         # Filtrlangan ob'ektlarni saqlash uchun ro'yxat
#         filtered_instances = cls._instances
#         # Kiritilgan barcha filtrlarni ko'rib chiqamiz
#         for key, value in kwargs.items():
#             filtered_instances = [instance for instance in filtered_instances if getattr(instance, key) == value]
#         return MyIterableClassIterator(filtered_instances)

# class MyIterableClassIterator:
#     def __init__(self, instances):
#         self._instances = instances
#         self._index = 0

#     def __iter__(self):
#         return self

#     def __next__(self):
#         if self._index < len(self._instances):
#             result = self._instances[self._index]
#             self._index += 1
#             return result
#         else:
#             raise StopIteration

# # MyIterableClass'dan foydalanish
# obj1 = MyIterableClass('first', 'A')
# obj2 = MyIterableClass('second', 'B')
# obj3 = MyIterableClass('third', 'A')
# obj4 = MyIterableClass('fourth', 'C')

# # Barcha obyektlarni iteratsiya qilish
# print("All objects:")
# for obj in MyIterableClass():
#     print(obj.value, obj.category)

# # 'category' xususiyati bo'yicha filtrlangan obyektlarni iteratsiya qilish
# print("\nFiltered objects (category='A'):")
# for obj in MyIterableClass.filter(category='A'):
#     print(obj.value, obj.category)


# 4
class MyIterableClass:
    # Class-level ro'yxat
    _instances = []

    def __init__(self, value):
        self.value = value
        # Har bir yangi obyektni class-level ro'yxatga qo'shamiz
        MyIterableClass._instances.append(self)

    # Bu metod barcha ob'ektlarning ID'larini iteratsiya qilishni boshlash uchun kerak
    def __iter__(self):
        # ID'larni iteratsiya qilish uchun iterator obyektini qaytarish
        return MyIterableClassIDIterator(MyIterableClass._instances)

class MyIterableClassIDIterator:
    def __init__(self, instances):
        self._ids = [id(instance) for instance in instances]
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index < len(self._ids):
            result = self._ids[self._index]
            self._index += 1
            return result
        else:
            raise StopIteration

# MyIterableClass'dan foydalanish
obj1 = MyIterableClass('first')
obj2 = MyIterableClass('second')
obj3 = MyIterableClass('third')

# Barcha obyektlarning ID'larini iteratsiya qilish
print("All object IDs:")
for obj_id in MyIterableClass():
    print(obj_id)

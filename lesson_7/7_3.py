class Category:
    categories = []

    @classmethod
    def add(cls, name: str):
        if len(cls.categories) == 0:
            cls.categories.append(name)
            return print(f"{name}, {cls.categories.index(name)}")
        try:
            for _ in cls.categories:
                if name not in cls.categories:
                    cls.categories.append(name)
                    return print(f"{name}, {cls.categories.index(name)}")
                else:
                    raise ValueError
        except ValueError:
            print(f"Ошибка: данная категория уже есть в списке!")

    @classmethod
    def get(cls, index: int):
        try:
            print(cls.categories[index])
        except IndexError:
            print(f"IndexError")

    @classmethod
    def delete(cls, index):
        try:
            cls.categories.pop(index)
        except IndexError:
            return None

    @classmethod
    def update(cls, index: int, new_name: str):
        try:
            for _ in cls.categories:
                if new_name in cls.categories:
                    raise ValueError
        except ValueError:
            print("You are lox")
        if new_name not in cls.categories and index > len(cls.categories) - 1:
            cls.categories.append(new_name)
        if new_name not in cls.categories and index <= len(cls.categories) - 1:
            cls.categories.insert(index, new_name)


# Category.add("Movie")
# Category.add("Music")
# # Category.add("Movie")
# # Category.get(1)
# # Category.delete(2)
# Category.update(2, "Cartoon")
# print(Category.categories)

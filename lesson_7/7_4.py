class Category:
    categories = []

    @classmethod
    def add(cls, name: str, is_published: bool):
        some_dict = {"Name": name, "is_published": is_published}
        if len(cls.categories) == 0:
            cls.categories.append(some_dict)
            return print(f"{some_dict}, {cls.categories.index(some_dict)}")
        try:
            for i in cls.categories:
                for _ in i.values():
                    if name != i.get("Name"):
                        cls.categories.append(some_dict)
                        return print(f"{some_dict}, {cls.categories.index(some_dict)}")
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
    def update(cls, index: int, new_name: str, is_published: bool):
        new_dict = {"Name": new_name, "is_published": is_published}
        try:
            for i in cls.categories:
                if new_name == i.get("Name"):
                    raise ValueError
        except ValueError:
            print("You are lox")
        for i in cls.categories:
            if new_name != i.get("Name") and index > len(cls.categories) - 1:
                cls.categories.append(new_dict)
                break
        for i in cls.categories:
            if new_name != i.get("Name") and index <= len(cls.categories) - 1:
                cls.categories.insert(index, new_dict)
                break


Category.add("Movie", True)
Category.add("Music", False)
Category.add("Cartoon", True)
Category.add("Game", False)
# Category.add("Movie", False)
Category.delete(2)
print(Category.categories)

# Дан словарь словарей, ключ внешнего словаря - id пользователя, значение -
# словарь с данными о пользователе (имя, фамилия, телефон, почта), вывести
# имена тех, у кого не указана почта (нет ключа email или значение этого ключа -
# пустая строка)
id_dict = {
    "ID1": {"Name": "Alex", "SurName": "Smith", "Tel": 6765432, "email": ""},
    "ID2": {"Name": "Mike", "SurName": "Dilan", "Tel": 654326},
    "ID3": {"Name": "Till", "SurName": "Lindemann", "Tel": 124999, "email": "fdaaww@sd.com"},
    "ID4": {"Name": "Alice", "SurName": "Cooper", "Tel": 7839673, "email": "ddsff@sd.com"},
    "ID5": {"Name": "Einar", "SurName": "Selvik", "Tel": 1148867, "email": "dsfgyu@sd.com"},
}


def foo():
    for data in id_dict.values():
        if "email" not in data.keys():
                a = data.get("Name", 0)
                b = data.get("SurName", 0)
                print(f"{a} {b} has't email")
        if data.get("email", 0) == "":
                a = data.get("Name", 0)
                b = data.get("SurName", 0)
                print(f"{a} {b} has't email")


foo()

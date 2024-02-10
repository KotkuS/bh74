# Дан список содержащий в себе различные типы данных,
# отфильтровать таким образом, чтобы остались только строки,
# использование дополнительного списка незаконно
data_list = ["Hello", 2, "1", (1, 2), {"a": True}, None, "world", 194]
new_data_list = list(filter(lambda x: isinstance(x, str), data_list))
print(new_data_list)

text = input("Введите предложение:")
print(text.replace(" " , "-"))
newtext = text.split()
print("-".join(newtext))

def calc(expression):
    try:
        return eval(expression)                         #Вычисление выражения
    except Exception:                                   #Перехват, в случае ошибки ввода
        return "Ошибка ввода"

expression = input("Введите математическое выражение: ")
result = calc(expression)
print("Ответ:", result)
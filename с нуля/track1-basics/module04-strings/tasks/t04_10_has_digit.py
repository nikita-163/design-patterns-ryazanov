"""
Задача 04-10. Есть ли цифра

Прочитайте строку и выведите True, если в ней есть хотя бы одна цифра,
иначе False. Как только цифра найдена — перебор можно прервать.

Пример
------
Ввод:
abc1
Вывод:
True
"""

# TODO: переберите символы и проверьте isdigit()
text = input()

has_digit = False
for ch in text:
    if ch.isdigit():
        has_digit = True
        break

print(has_digit)


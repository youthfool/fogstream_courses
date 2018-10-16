""" 
В некоторой школе занятия начинаются в 9:00.
Продолжительность урока — 45 минут, после 1-го, 3-го,
5-го и т.д. уроков перемена 5 минут, а после 2-го, 4-го,
6-го и т.д. — 15 минут. Дан номер урока (число от 1 до 10).
Определите, когда заканчивается указанный урок.
Выведите два целых числа: время окончания урока в часах и минутах.
"""


# nice input
# print("Enter the number of lesson")
lesson_number = int(input())

hours = 9
minutes = lesson_number * 45 + int(lesson_number / 2) * 5 + int((lesson_number - 1) / 2) * 15

hours += int(minutes / 60)
minutes = minutes % 60

# nice output
# print("Lesson ends at {:0>2}:{:0>2}".format(hours, minutes))
print(hours)
print(minutes)


""" 
С начала суток прошло H часов, M минут,
S секунд (0 ≤ H < 12, 0 ≤ M < 60, 0 ≤ S < 60).
По данным числам H, M, S определите угол (в градусах),
на который повернулаcь часовая стрелка с начала суток и
выведите его в виде действительного числа.
"""


# nice input
# print("Enter hours")
hours = int(input())
# print("Enter minutes")
minutes = int(input())
# print("Enter seconds")
seconds = int(input())

total_seconds_count = 12 * 60 * 60

rotation_seconds_count = hours * 60 * 60 + minutes * 60 + seconds

angle = rotation_seconds_count / total_seconds_count * 360

# nice output
# print("Rotation angle is {}".format(angle))
print(angle)



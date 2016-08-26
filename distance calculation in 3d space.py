def calc_distance_3d(x1, y1, z1, x2, y2, z2):
    return abs(((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2) ** .5)

x1 = int(input("Please input x1: "))
y1 = int(input("Please input y1: "))
z1 = int(input("Please input z1: "))

x2 = int(input("Please input x2: "))
y2 = int(input("Please input y2: "))
z2 = int(input("Please input z2: "))


x = calc_distance_3d(x1, y1, z1, x2, y2, z2)

print('The distance between the two points is ' + str(x))

input('')

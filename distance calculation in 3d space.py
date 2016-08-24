def calc_distance_3d(x1, y1, z1, x2, y2, z2):
    return abs(((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)**.5)

x1 = input("Please input x1: ")
y1 = input("Please input y1: ")
z1 = input("Please input z1: ")

x2 = input("Please input x2: ")
y2 = input("Please input y2: ")
z2 = input("Please input z2: ")

print calc_distance_3d(x1, y1, z1, x2, y2, z2)

x = raw_input('')


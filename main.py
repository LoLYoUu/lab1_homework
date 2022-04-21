a = float(input())
b = float(input())
c = float(input())
D = b ** 2 - 4 * a * c
print(D)
if D >= 0:
    x1 = (-b + D ** 0.5)/(2 * a)
    x2 = (-b - D ** 0.5)/(2 * a)
    print(x1)
    print(x2)
else:
    print("корней нет")
a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
c = int(input("Введите третье число: "))
if a == b == c:
    print(3)
elif a == b or a != c and b == c or b != a and c == a or c != b:
    print(2)
else:
    print(0)

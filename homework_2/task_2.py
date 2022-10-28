a = int(input("Введіть довжину сторони а: "))
b = int(input("Введіть довжину сторони b: "))
c = int(input("Введіть довжину сторони c: "))
perimeter = a + b + c
while True:
    if a == 0 or b == 0 or c == 0:
        print("Таких трикутників не існує")
    break
if a != 0 and b != 0 and c != 0:
    if perimeter < 10:
        print("Периметр трикутника: ", perimeter)
        if a < b and a < c:
            print("Найменша строрна: ", a)
        if b < a and b < c:
            print("Найменша строрна: ", b)
        if c < a and c < b:
            print("Найменша строрна: ", c)
    elif perimeter > 20:
        print("Периметр трикутника: ", perimeter)
        if a > b and a > c:
            print("Найбільша строрна: ", a)
        if b > a and b > c:
            print("Найбільша строрна: ", b)
        if c > a and c > b:
            print("Найбільша строрна: ", c)
    else:
        print("Периметр трикутника: ", perimeter)

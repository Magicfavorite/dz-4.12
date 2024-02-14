number = input("Введите четырехзначное число: ")
product = 1

for digit in number:
    product *= int(digit)

print("Произведение цифр:", product)

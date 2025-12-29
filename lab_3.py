# task 1
f = open('example.txt').readlines()
print("modes: 1 - all, 2 - lines, 3 - a line")
mode = int(input())
if mode == 1:
    print(f)
if mode == 2:
    for x in f:  # по строчно
        print(x)

# task 2
text = int(input())
F = open('user_input.txt', 'w')
F.write(text + "\n")
F.close()

# task 3
try:
    FF = open('example.txt', 'r')
    print("modes: 1 - all, 2 - lines")
    MODE = int(input())

    if MODE == 1:
        print(FF.read())
    if MODE == 2:
        for X in FF:
            print(X)
except FileNotFoundError:
    print("Файл не найден")

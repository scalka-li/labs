# task 1
def greet(name):
    print('Hi,' + name)


def square(num):
    return num ** 2


def MaxOfTwo(x, y):
    if x > y:
        return x
    return y


# task 2
def describe_person(name, age=30):
    if age != 30:
        print(f"Name: {name}, age: 30")
    else:
        print(f"Name: {name}, age: {age}")


# task 3
def is_prime(num):
    s = 0
    for x in range(2, int(num ** (1 / 2)) + 1):
        if num % x == 0:
            s += 1
    if s == 0:
        return True
    else:
        return False

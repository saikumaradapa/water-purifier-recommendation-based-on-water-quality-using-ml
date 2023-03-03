import math


def is_even(n):
    return int(n) % 2 == 0


def is_prime(n):
    n = int(n)
    if n < 2:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    else:
        for i in range(3, math.isqrt(n) + 1, 2):
            if n % i == 0:
                return False
        return True


test_cases = int(input())
for case in range(test_cases):
    lenght = int(input())
    num = int(input())
    count = 0
    flag = False
    for i in range(10 ** (lenght - 1), num + 1):

        for j in range(len(str(i))):
            if j % 2 == 0 and not is_even(str(i)[j]):
                flag = True

            elif j % 2 != 0 and not is_prime(str(i)[j]):
                flag = True
            if flag:
                count += 1
                continue

    print(count)

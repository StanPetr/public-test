import random

def qsort(array, left=None, right=None, middle=None, debug=False, rnd=False, desc=False):

    if left is None:
        left = 0
    if right is None:
        right = len(array) - 1
    if rnd:
        middle = random.choice(array[left:right + 1])
    if middle is None:
        middle = array[(left + right) // 2]
    if debug:
        print('sorting ' + ('sub' if left > 0 or right < len(array) - 1 else '')
              + f'array: {array[left:right + 1]}, middle = {middle}' + (' (random)' if rnd else ''))

    M = middle
    L, R = left, right
    while L <= R:
        while not desc and array[L] < M or desc and array[L] > M:
            L += 1
        while not desc and array[R] > M or desc and array[R] < M:
            R -= 1
        if L <= R:
            array[L], array[R] = array[R], array[L]
            L += 1
            R -= 1

    if R > left:
        qsort(array, left, R, debug=debug, rnd=rnd, desc=desc)
    if right > L:
        qsort(array, L, right, debug=debug, rnd=rnd, desc=desc)

    return array


s = input('Введите числа в любой последовательности через пробел: ')
while not all(map(lambda x: x.isdigit(), s.split())):
    s = input('Ошибка. Введите числа через пробел: ')
array = list(map(int, s.split()))

s = input('Введите любое число: ')
while not s.isdigit() or all(map(lambda x: x > int(s), array)) or all(map(lambda x: x < int(s), array)):
    s = input('Ошибка. Введите цифры: ')
middle = int(s)

array = qsort(array, middle=middle)

i = 0
while array[i+1] < middle:
    i += 1
R = 11 + sum(map(lambda x: len(str(x)) + 2, array[:i+1]))

print('Упорядоченный список:', array)
print(' ' * R, '^')
print('Номер позиции элемента, который меньше введенного пользователем числа, а следующий за ним больше или равен этому числу:', i)
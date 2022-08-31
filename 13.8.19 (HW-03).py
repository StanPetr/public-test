def price(cstmr_age: int):

    prices = {
        (0, 18): 0,
        (18, 25): 990,
        (25, 200): 1390
    }

    price = None

    for a in prices.keys():
        if a[0] <= cstmr_age < a[1]:
            price = prices[a]

    return price

def totals(cstmrs_list: list, return_discount=False):
    total_sum = 0
    discount = len(cstmrs_list) > 3

    for a in cstmrs_list:
        if discount and return_discount:
            total_sum += price(a) * 0.1
        elif discount:
            total_sum += price(a) * 0.9
        elif not return_discount:
            total_sum += price(a)

    return total_sum

print("Сегодня вы можете получить скидку 10% при заказе от 3х билетов")
n = input("Введите количество билетов, которое вы хотите приобрести: ")

while (not n.isdigit() or int(n) == 0):
    n = input("Введите цифру, соответствующую количеству гостей: ")

n = int(n)
L = []
age = 0

for i in range(1, n + 1):
    age = input("Введите возраст {}-го пользователя: ".format(i))

    while not age.isdigit() or age.isdigit() and int(age) >= 120:
        age = input(("Столько не живут! " + ("Введите возраст не более 120 лет" if age.isdigit() else "Введите число")
                     + ". Повторите ввод возраста {}-го пользователя: ").format(i))

    L.append(int(age))

print('')
if len(L) > 3:
    print("Вы делаете заказ со скидкой. Ваша скидка", totals(L, True))
else:
    print("Извините, но количество билетов 3 или менее, скидка не применяется")

print('Итоговая сумма заказа составит', round(totals(L), 2))
money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

counter = 0
while True :
    money_capital = money_capital + salary - spend*((1+increase)**counter)
    if money_capital <= 0 :
        break
    counter += 1

print(f'Количество месяцев, которое можно протянуть без долгов: {counter}') # терпеть не могу двойные кавычки для текста


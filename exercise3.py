def hanoi(n, source, target, auxiliary, state):
    """
    Функція для вирішення задачі Ханойських башт з логуванням стану.
    
    :param n: Кількість дисків
    :param source: Початковий стрижень (ім'я)
    :param target: Цільовий стрижень (ім'я)
    :param auxiliary: Допоміжний стрижень (ім'я)
    :param state: Словник стану стрижнів
    """
    if n == 1:
        # Переміщуємо диск і логуємо стан
        disk = state[source].pop()
        state[target].append(disk)
        print(f"Перемістити диск з {source} на {target}: {disk}")
        print(f"Проміжний стан: {state}")
        return

    # Переміщуємо n-1 дисків на допоміжний стрижень
    hanoi(n - 1, source, auxiliary, target, state)

    # Переміщуємо найбільший диск на цільовий стрижень
    disk = state[source].pop()
    state[target].append(disk)
    print(f"Перемістити диск з {source} на {target}: {disk}")
    print(f"Проміжний стан: {state}")

    # Переміщуємо n-1 дисків з допоміжного стрижня на цільовий
    hanoi(n - 1, auxiliary, target, source, state)

# Введення кількості дисків
n = int(input("Enter the number of disks: "))

# Початковий стан стрижнів
state = {
    'A': list(range(n, 0, -1)),  # Диски на стрижні A
    'B': [],  # Порожній стрижень B
    'C': []   # Порожній стрижень C
}

print(f"Початковий стан: {state}")
hanoi(n, 'A', 'C', 'B', state)
print(f"Кінцевий стан: {state}")
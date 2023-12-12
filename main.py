user_data = []
ages = []

while True:
    print("1. Добавить пользователя")
    print("2. Удалить пользователя")
    print("3. Вывести информацию о пользователях")
    print("4. Вычислить средний возраст")
    print("5. Выйти")

    choice = input("Выберите действие (1/2/3/4/5): ")

    if choice == '1':
        name = input("Введите имя пользователя: ")
        age = int(input("Введите возраст пользователя: "))

        user_data.append({'name': name, 'age': age})
        ages.append(age)

    elif choice == '3':
        print("Информация о пользователях:")
        for user in user_data:
            print(f"Имя: {user['name']}, Возраст: {user['age']}")

    elif choice == '4':
        if not ages:
            print("Нет данных о возрасте пользователей.")
        else:
            average_age = sum(ages) / len(ages)
            print(f"Средний возраст пользователей: {average_age}")

    elif choice == '5':
        print("Выход из программы.")
        break
    
    elif choice == '2':
        name = input("Введите имя пользователя, которого нужно удалить: ")
        removed = False

        for user in user_data:
            if user['name'] == name:
                user_data.remove(user)
                ages.remove(user['age'])
                removed = True
                break

        if removed:
            print(f"Пользователь {name} удален.")
        else:
            print(f"Пользователь с именем {name} не найден.")

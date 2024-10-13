def warehouse():

    food_warehouse = {}



    while True:
        key = input('Введите название продукта или "стоп", для завершения": ')
        if key.lower() == 'стоп':
            break
        value = int(input('Введите количество продукта или "стоп", для завершения: '))
        food_warehouse[key] = value

    filtered_data = {key: value < 20 for key, value in food_warehouse.items()}
    return filtered_data

filtered_data = warehouse()
print(filtered_data)
















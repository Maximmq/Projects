try:
    byytes = int(input("Введите размер файла в байтах: "))  # пользователь вводит целое значение размера файла в байтах
    kilobytes = byytes // 1024
    print(f"Размер файла в килобайтиах: {kilobytes}")
except ValueError:
    print("Неправильный ввод!")
# Задача на функции. Мы пишем программу для ветеренарной клиники, в которой пользователь вводит данные о питомце (Имя, возраст, вид, имя владельца), и у нас создается запись в базе. После Пользователь может редактировать, удалять, создавать новые записи. Имена питомцев являются ключами в словаре, по которым и можно найти необхолимую запись.
pets = {}


def create(): 
    """ Создаёт новую запись в словаре """
    while True:
        print('Для завершения нажмите 0')   
        name_pet = input('Введите имя питомца: ').capitalize()
        if name_pet == '0':
            break
        type_pet = input('Введите вид питомца: ').lower()
        age_pet = input('Введите возраст питомца: ')
        boss = input('Введите имя владельца: ').capitalize()
        pets[name_pet] = {'Вид':f'{type_pet}','Возраст':f'{age_pet}','Владелец':f'{boss}'}


def read():
    """ Выводит описание питомца по имени """
    pet_of_num = input('Введите имя питомца или слово (все): ').capitalize() 
    if pet_of_num in pets.keys():
        print(pets[pet_of_num])
    elif pet_of_num.lower() == 'все':
        print(pets)
    elif pet_of_num not in pets.keys():
            print('Такой записи НЕТ!!!')
            print('Создать новую запись ????')
            yes_no = input('ДА/НЕТ: ')

            if yes_no.lower() == 'да':
                    create()
            elif yes_no.lower == 'нет':
                print('')


def delete():
    """ Удаляет питомца по имени или очищает весь словарь"""
    name = input('Введите имя питомца или слово (очистить): ').capitalize()
    if name.lower() == 'очистить':
        print('Список полностью очищен')
        pets.clear()
    if name in pets.keys():
        print('Данный питомец, удалён из списка')
        del pets[name]




while True:
    command = input('Введите одну из команд (стоп, создать, читать, обновить, удалить): ').lower()
    if command == 'стоп':
        break
    elif command == 'создать':
        create()
    elif command == 'читать':
        read()
    elif command == 'удалить':
        delete()





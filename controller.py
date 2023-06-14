import phone_book
import contact

pb = phone_book.PhoneBook('phone_db.txt')

while True:
    print(pb.main_menu())
    choice = int(input('Выберите пункт меню: '))
    match choice:
        case 1:
            print(pb)
        case 2:
            name = input('Введите имя: ')
            phone = input('Введите номер телефона: ')
            comment = input('Введите комментарий: ')
            pb.new_contact(name, phone, comment)
        case 3:
            word = input('Введите запрос для поиска: ')
            print(pb.search(word))
        case 4:
            print(pb)
            index = int(input('Введите номер контакта, который будем изменять: '))
            name = input('Введите имя (Enter -  если изменений нет): ')
            phone = input('Введите номер телефона (Enter -  если изменений нет): ')
            comment = input('Введите комментарий (Enter -  если изменений нет): ')
            pb.change(index - 1, name, phone, comment)
        case 5:
            print(pb)
            index = int(input('Введите номер контакта, который необходимо удалить: '))
            pb.delete(index-1)
        case 6:
            pb.save()
        case 7:
            break
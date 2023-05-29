def add_contact(f):
    input_name = input('Введите Имя: ')
    input_last_name = input('Введите Фамилию: ')
    input_phone = input('Введите номер телефона: ')
    data = f'({input_last_name}; {input_name}; {input_phone}'
    with open(f, 'a', encoding='utf-8') as fd:
        fd.write(f'{data}\n')
    print(f'Запись {data} добавлена')


def read_all(f):
    with open(f, 'r', encoding='utf-8') as fd:
        file_list = fd.readlines()
        return file_list


def print_all(f):
    adr_book = read_all(f)
    for line in adr_book:
        line = line.replace(";", "")
        line = line.replace("\n", "")
        print(line)


def search_contact(f):
    last_name = input("Введите фамилию для поиска: ").capitalize()
    adr_book = read_all(f)
    find_list = []
    for idx in range(len(adr_book)):
        if last_name in adr_book[idx]:
            find_list.append(idx)
    if find_list is None:
        print("Запись не найдена")
    else:
        for find_idx in find_list:
            print(find_idx, adr_book[find_idx])
        


def change_contact(f):
    last_name = input("Введите фамилию для поиска: ").capitalize()
    adr_book = read_all(f)
    find_list = []
    for idx in range(len(adr_book)):
        if last_name in adr_book[idx]:
            find_list.append(idx)
            print(adr_book[idx], [idx])
    idx = int(input("Введите индекс для замены: "))
    last_name, name = adr_book[idx].split("; ")[:2]
    phone = input("Введите новый номер: ")
    new_record = f'{last_name}; {name}; {phone}'
    adr_book[idx] = new_record
    with open(f, "w", encoding="utf-8") as fd:
        fd.writelines(adr_book)

def delit_contact(f):
    adr_book = read_all(f)
    if not adr_book: 
        print('Книжка и так пуста!\n') 
    else: 
        act_choice = input('Выберите действие: 1 - очистить книжку, 2 - удалить контакт ')
    if act_choice == '1': 
        adr_book.clear() 
    elif act_choice == '2': 
        for i in range(len(adr_book)): 
            print(f'{i+1} - {adr_book[i]}') 
        idx = int(input('Укажите номер контакта, который хотите удалить: ')) - 1 
        del adr_book[idx] 
    with open(f, 'w', encoding='utf-8') as fw: 
        fw.writelines(adr_book) 
        print('Данные удалены!\n')



def main():
    file = 'address_book.txt'
    while True:
        user_choice = input('1 - добавить запись,\n2 - прочитать всю тел.книгу,\n3 - поиск,\n4 - изменение,\n5 - удаление,\nz - для выхода: ')
        if user_choice == '1':
            add_contact(file)
        elif user_choice == '2':
            print_all(file)
        elif user_choice == '3':
            search_contact(file)
        elif user_choice == '4':
            change_contact(file)
        elif user_choice == '5':
            delit_contact(file)
        elif user_choice == 'z':
            print('Всего хорошего')
            break

if __name__ == '__main__':
    main()



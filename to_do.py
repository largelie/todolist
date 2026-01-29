import os
import time

to_do_list = []

def add():
    os.system("cls")

    added = input("Введите текст задачи для добавления:\n")
    to_do_list.append(added)
    print("Задача успешно добавлена")

    time.sleep(3)

    os.system("cls")

def sholist():
    os.system("cls")

    if len(to_do_list) > 0:
        print("Список задач:")
        for i, item in enumerate(to_do_list):
            print(f"{i+1}. {item}")

        time.sleep(3)
        os.system("cls")
    else:
        print("Задач пока нету.")

        time.sleep(3)
        os.system("cls")

def ready(to_do_list):
    os.system("cls")
    if not to_do_list:
        print("Cписок задач пуст")
        time.sleep(3)
        os.system("cls")
        return
    
    deleted = int(input("Введите номер задачи для пометки как выполненной и ее удаления:\n"))
    

    if 1 <= deleted <= len(to_do_list):
        deleted -= 1
        to_do_list.pop(deleted)
        print("Задача удалена.\n")

        time.sleep(3)
        os.system("cls")

while True:
    print("Что вы хотите сделать? Введите\n/ для просмотра всех задач\n+ для добавления задачи\n- для пометки задачи как выполненной и её удаления\n\n")
    ans = input()
    if ans == "/":
        sholist()
    elif ans == "+":
        add()
    elif ans == "-":
        ready(to_do_list)
    else:
        print("Команда не найдена")





    

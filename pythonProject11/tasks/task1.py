#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def add_student(students):
    full_name = input("Фамилия и инициалы? ")
    group_number = input("Номер группы? ")
    grades_str = input("Успеваемость (через пробел)? ")

    grades = [float(grade) for grade in grades_str.split()]

    student = {
        'full_name': full_name,
        'group_number': group_number,
        'grades': grades,
    }

    students.append(student)
    students.sort(key=lambda item: item.get('group_number', ''))

def list_students(students):
    line = '+-{}-+-{}-+-{}-+'.format(
        '-' * 30,
        '-' * 15,
        '-' * 20
    )
    print(line)
    print(
        '| {:^30} | {:^15} | {:^20} |'.format(
            "Ф.И.О.",
            "Номер группы",
            "Успеваемость"
        )
    )
    print(line)

    for student in students:
        average_grade = sum(student.get('grades', 0)) / len(student.get('grades', 1))
        if average_grade > 4.0:
            print(
                '| {:<30} | {:<15} | {:<20} |'.format(
                    student.get('full_name', ''),
                    student.get('group_number', ''),
                    ', '.join(map(str, student.get('grades', [])))
                )
            )
    print(line)

def help_command():
    print("Список команд:\n")
    print("add - добавить студента;")
    print("list - вывести список студентов;")
    print("help - отобразить справку;")
    print("exit - завершить работу с программой.")

def main():
    students = []

    while True:
        command = input(">>> ").lower()

        if command == 'exit':
            break
        elif command == 'add':
            add_student(students)
        elif command == 'list':
            list_students(students)
        elif command == 'help':
            help_command()
        else:
            print(f"Неизвестная команда {command}")

if __name__ == '__main__':
    main()

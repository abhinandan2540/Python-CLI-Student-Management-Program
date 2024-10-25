import os
import json
from argparse import ArgumentParser


data_sheet = 'SMP.txt'
if os.path.exists(data_sheet):
    with open(data_sheet, 'r') as file:
        students = json.load(file)
else:
    students = []


def save_data():
    with open(data_sheet, 'w') as file:
        json.dump(students, file, indent=4)


def add_data(name, name_class, name_age):
    student = {
        "name": name,
        "name_class": name_class,
        "name_age": name_age
    }
    students.append(student)
    save_data()
    print("data added sucessfully")


def view_data():
    if students:
        for student in students:
            print(
                f"Name {student['name']}, Class {student['name_class']}, Age{student['name_age']}")
    else:
        print("no record found")


def update_data():
    stdn = input("enter student name tp update :")
    for student in students:
        if student['name'] == stdn:
            student['name_class'] = int(input("name class:"))
            student['name_age'] = int(input("name age :"))
            save_data()
        else:
            print(f"{stdn} not found")


def main():
    parser = ArgumentParser()
    parser.add_argument("--add", action="store_true", help="add of student")
    parser.add_argument("--view", action="store_true",
                        help="visuaziling the student list")
    parser.add_argument("--name", type=str, help="name of the student")
    parser.add_argument("--name_class", type=int, help="class of name")
    parser.add_argument("--name_age", type=int, help="age of name")
    parser.add_argument("--update", action="store_true",
                        help="update the student list")
    # parser.add_argument("-v","--verbose",type=int, choices=[0,1,2])

    args = parser.parse_args()

    if args.add and args.name and args.name_class and args.name_age:
        add_data(args.name, args.name_class, args.name_age)
    elif args.view:
        view_data()
    elif args.update:
        update_data()
    else:
        print(parser.print_help())


if __name__ == "__main__":
    main()

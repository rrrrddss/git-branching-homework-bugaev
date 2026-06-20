# subjects.py

SUBJECTS = [
    "Основы программирования",
    "Git и системы контроля версий",
    "Базы данных",
    "Веб-разработка",
]


def print_subjects():
    print("\nДисциплины:")
    for number, subject in enumerate(SUBJECTS, start=1):
        print(f"{number}. {subject}")

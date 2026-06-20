# grades.py
GRADES = {
    "Основы программирования": 5,
    "Git и системы контроля версий": 5,
    "Базы данных": 4,
    "Веб-разработка": 5,
}


def average():
    return sum(GRADES.values()) / len(GRADES)


def print_grades():
    print("\nОценки:")
    for subject, mark in GRADES.items():
        print(f"- {subject}: {mark}")
    print(f"Средний балл: {average():.2f}")

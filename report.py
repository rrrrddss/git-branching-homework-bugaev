# report.py
from profile import get_profile
from subjects import SUBJECTS


def build_report():
    profile = get_profile()
    lines = [
        "Итоговый отчёт по Git Branching App",
        f"Студент: {profile['name']}",
        f"Группа: {profile['group']}",
        f"Количество дисциплин: {len(SUBJECTS)}",
        "Статус: ветки, merge и Pull Request отработаны",
    ]
    return "\n".join(lines)


def print_report():
    print("\n" + build_report())

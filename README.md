# Git Branching Homework — Student Branching App

## Описание проекта
Учебный мини-проект на Python для отработки процесса разработки через ветки Git.
Ветка `main` хранит рабочую версию, а каждая новая возможность создаётся в отдельной
ветке и попадает в `main` только после коммитов и слияния (merge / Pull Request).

Запуск:
```
python main.py
```

## Использованные ветки
| Ветка | Что делал | Как попала в main |
|---|---|---|
| feature/profile | модуль профиля студента (`profile.py`) | merge локально (--no-ff) |
| feature/subjects | список дисциплин (`subjects.py`) | merge локально (--no-ff) |
| feature/report | итоговый отчёт (`report.py`) | Pull Request (merge --no-ff) |
| experiment/broken-idea | тестовая идея (`idea.txt`) | удалена без merge |

## Pull Request
Pull Request создан и слит на GitHub:
**https://github.com/rrrrddss/git-branching-homework-bugaev/pull/1**
(`feature/grades → main`, добавлен модуль оценок, слит кнопкой Merge pull request).
Также через отдельные ветки и слияния добавлены модули profile, subjects и report.

## Коммиты (8+)
1. docs: добавить README проекта
2. feat: добавить базовый запуск приложения
3. feat(profile): добавить модуль профиля студента
4. feat(profile): подключить вывод профиля в main.py
5. feat(subjects): добавить модуль списка дисциплин
6. refactor(main): подключить вывод дисциплин
7. feat(report): добавить генерацию итогового отчёта
8. feat(report): подключить отчёт в main.py
+ merge-коммиты feature/profile, feature/subjects и Pull Request feature/report

## Скриншоты
Положите в `docs/screenshots/`:
- `01-branches-before-merge.png` — граф веток до merge;
- `02-merge-result.png` — результат merge;
- `03-pull-request-merged.png` — созданный и закрытый Pull Request;
- `04-final-github-main.png` — финальная ветка main на GitHub.

## Вывод
Ветки позволяют вести независимую разработку, не ломая рабочую версию в `main`.
Merge переносит готовые изменения, Pull Request делает их видимыми и проверяемыми,
а неудачные эксперименты можно изолировать в отдельной ветке и удалить без следа.

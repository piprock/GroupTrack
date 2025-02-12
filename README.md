# GroupTrack
GroupTrack — це програма для обробки списків присутніх у Google Meet, яка додає студентів до списку, сортує та визначає групу з бази даних. Вона доповнює розширення Google Meet Attendance List і спрощує управління студентськими групами.

## Завантаження та запуск
### Завантаження релізу
1. Завантажте останню версію програми з GitHub Releases.
2. Запустіть виконуваний файл
### Завантаження репозиторію
1. Клонуйте репозиторій
2. В папці клонованого репозиторію виконайте команду `python src/main.py`

## Основні можливості
- Імпорт списку присутніх (CSV).
- Автоматичне визначення групи студентів.
- Сортування за логіном та групою.
- Редагування бази
  - В Excel
  - В програмі

## База даних
База реалізована в Excel, дані розділяються комою.
Шлях `src\database\groups.csv`

## Редагування бази в програмі
У програмі в поточному списку можна вибрати студентка *(або кілька студентів зажимаючи Shift або Ctrl)* і вибрати відповідну кнопку **Редагувати групи вибраних студентів**

## Алгоритм роботи
- Зчитується вхідний CSV-файл із списком присутніх.
- Програма знаходить відповідний логін у базі та додає групу до поточного списку.
- Якщо студента немає в базі, користувач може додати його.
- Якщо студенти з однаковим логіном належать до різних груп, в програмі можна приззначити одразу дві групи одному логіну

## Вихідні дані
CSV-файл містить поля у вигляді

*логін,група*

Якщо 2 студента з одинаковим логіном

*логін,група група*

## Використані технології
- Python
- pandas - для роботи з CSV
- tkinter - для графічного інтерфейсу

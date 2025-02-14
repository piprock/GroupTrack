# GroupTrack
GroupTrack — це програма для обробки списків присутніх у Google Meet, яка додає студентів до списку, сортує та визначає групу з бази даних. Вона доповнює розширення Google Meet Attendance List і спрощує управління студентськими групами.

# Відео огляд
<a href="https://www.youtube.com/watch?v=6h7mcS2DbqI" target="_blank">
  <img src="https://img.youtube.com/vi/6h7mcS2DbqI/0.jpg" alt="Video" />
</a>

## Розширення для скачування списку присутніх
Google Meet Attendance List

<a href="https://chromewebstore.google.com/detail/%D1%81%D0%BF%D0%B8%D1%81%D0%BE%D0%BA-%D0%BF%D1%80%D0%B8%D1%81%D1%83%D1%82%D0%BD%D0%BE%D1%81%D1%82%D1%96-%D0%B2-goog/appcnhiefcidclcdjeahgklghghihfok" target="_blank">
Посилання
</a>

## Завантаження та запуск
### Завантаження релізу
1. Завантажте останню версію програми з GitHub Releases.
2. Запустіть виконуваний файл
### Завантаження репозиторію
1. Клонуйте репозиторій
2. Встановити python 3.8 (для windows 7) або вище
3. Встановити всі необхідні бібліотеки `pip install -r requirements.txt`
4. В папці клонованого репозиторію виконайте команду `python src/main.py`

## Збірка
Щоб створити збірку для Windows встановити `pyinstaller` командою `pip install pyinstaller`, з директорії репозиторія виконайте команду `build.bat 0.0` де `0.0` - це бажана версія збірки.

## Основні можливості
- Імпорт списку присутніх (CSV).
- Автоматичне визначення групи студентів.
- Сортування за логіном та групою.
- Редагування бази
  - В Excel
  - В програмі
 
## Гарячі клавіші
- `Ctrl + S` - Зберігає вихідний файл
- `Enter` - виконує "Редагувати групи вибрані елементи" для вибраних елементів
- `Enter` - зберірає змінену групу в "Редагувати групи вибрані елементи"
- зажати `Ctrl` або `Shift` і клікнути по елементу таблиці - вибрати кілька елементів

## База даних
База реалізована в Excel, дані розділяються комою.

Шлях по замовчуванню `src\database\groups.csv`

## Редагування бази в програмі
У програмі в поточному списку можна вибрати студента (або студентів)  і вибрати відповідну кнопку **Редагувати групи вибраних студентів**

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
- os, sys, pathlib - для роботи з файловою системою

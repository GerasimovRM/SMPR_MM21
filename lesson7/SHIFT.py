import time
from datetime import datetime, timedelta
import os

def time_until(day, time):
    # Сопоставляем введенный день с днем недели
    days = {
        "понедельник": 0,
        "вторник": 1,
        "среда": 2,
        "четверг": 3,
        "пятница": 4,
        "суббота": 5,
        "воскресенье": 6
    }

    # Получаем текущую дату и время
    current_datetime = datetime.now()

    # Получаем день недели от текущей даты
    current_day = current_datetime.weekday()

    # Получаем день недели, к которому нужно вычислить время
    target_day = days[day.lower()]

    # Если указанный день уже прошел в текущей неделе,
    # то прибавляем 7 дней, чтобы перейти к следующей неделе
    if current_day > target_day:
        target_day += 7

    # Вычисляем разницу в днях между текущим днем и целевым днем
    days_difference = target_day - current_day

    # Создаем объект datetime для указанного времени
    target_time = datetime.strptime(time, "%H:%M")

    # Получаем текущее время
    current_time = datetime.now().replace(second=0, microsecond=0)

    # Если указанное время уже прошло сегодня, добавляем 1 день
    if current_time.time() > target_time.time():
        days_difference += 1

    # Вычисляем дату и время, когда будет указанный день и время
    target_datetime = current_datetime + timedelta(days=days_difference)
    target_datetime = target_datetime.replace(hour=target_time.hour, minute=target_time.minute)

    # Вычисляем разницу во времени между текущим моментом и целевым моментом
    time_difference = target_datetime - current_datetime

    return time_difference

# Получаем ввод пользователя
while True:
    sozvons = [('понедельник', '20:30'), ('четверг', '20:30'), ('суббота', '17:30')]
    time_delta, (day, time_) = min((map(lambda x: (time_until(*x), x), sozvons)))
    print("До созвона:", time_delta)
    print(f"Созвон: {day.capitalize()} в {time_}")
    time.sleep(1)
    os.system('cls')

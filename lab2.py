from datetime import datetime, timedelta

class DateTime:
    def __init__(self, year, month, day, hour=0, minute=0, second=0):
        self.datetime = datetime(year, month, day, hour, minute, second)

    def add_days(self, days):
        self.datetime += timedelta(days=days)

    def add_hours(self, hours):
        self.datetime += timedelta(hours=hours)

    def add_minutes(self, minutes):
        self.datetime += timedelta(minutes=minutes)

    def add_seconds(self, seconds):
        self.datetime += timedelta(seconds=seconds)

    def subtract_days(self, days):
        self.datetime -= timedelta(days=days)

    def subtract_hours(self, hours):
        self.datetime -= timedelta(hours=hours)

    def subtract_minutes(self, minutes):
        self.datetime -= timedelta(minutes=minutes)

    def subtract_seconds(self, seconds):
        self.datetime -= timedelta(seconds=seconds)

    def get_date(self):
        return self.datetime.date()

    def get_time(self):
        return self.datetime.time()

    def __str__(self):
        return self.datetime.strftime("%Y-%m-%d %H:%M:%S")

# Пример использования класса DateTime
dt = DateTime(2023, 9, 27, 10, 30, 0)
print("Исходная дата и время:", dt)

dt.add_days(1)
print("После добавления 1 дня:", dt)

dt.subtract_hours(2)
print("После вычитания 2 часов:", dt)

print("Дата:", dt.get_date())
print("Время:", dt.get_time())

class Forecast:
    def __init__(self, date, day, weather):
        self.date = date
        self.day = day
        self.weather = weather

n = int(input())

fc = [tuple(input().split()) for _ in range(n)]
data = [Forecast(date, day, weather) for date, day, weather in fc]

rainy_dates = []
for i in range(n):
    if data[i].weather == "Rain":
        rainy_dates.append(tuple(data[i].date.split("-")))

rainy_dates.sort()
ans_date = "-".join(rainy_dates[0])

target_idx = 0
for j in range(n):
    if data[j].date == ans_date:
        target_idx = j

print(f"{data[target_idx].date} {data[target_idx].day} {data[target_idx].weather}")
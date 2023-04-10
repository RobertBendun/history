#!/usr/bin/env python3
from datetime import datetime
from glob import glob
import json

current_year = datetime.now().year
begin = datetime(current_year, 1, 1)
end = datetime(current_year, 12, 31)
days = (end - begin).days

all_dates = []

for path in glob("*.json"):
    with open(path) as f:
        file = json.load(f)

    if "category" not in file:
        continue

    if file["category"] == "people":
        dates = [person["birthday"] for person in file["people"] if person["birthday"]]
    elif file["category"] == "programming languages":
        dates = [release["date"] for release in file["releases"]]
    else:
        assert False, f"Category {file['category']} in file {path} is not supported"

    for date in dates:
        try:
            all_dates.append(datetime.strptime(date, "%Y-%m-%d"))
        except Exception as e:
            print(f"{path}: {e}")


calendar = [31 * [0] for _ in range(12)]

for event in all_dates:
    calendar[event.month - 1][event.day - 1] += 1

print("   ", end="")
for n in range(31):
    n = (n+1) // 10
    if n < 1:
        print(" ", end="")
    else:
        print(n, end="")
print()
print("   ", end="")
for n in range(31):
    print((n + 1) % 10, end="")
print()

for n, month in enumerate(calendar):
    print("%2d " % (n + 1,), end="")

    for day in month:
        if day > 0:
            print("x", end="")
        else:
            print(" ", end="")
    print()

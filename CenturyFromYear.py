"""
The first century spans from the year 1 up to and including the year 100, the second century - 
from the year 101 up to and including the year 200, etc.
"""


def century(year):
    century = year // 100
    if year % 100 == 0:
        return century
    return century + 1


year_to_check = 1990
result = century(year_to_check)

print(f"THe century for the year {year_to_check} is: {result}")
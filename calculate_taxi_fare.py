"""
After a lengthy meeting, the company's director decided to order a taxi to take the staff home. He ordered N cars
exactly as many employees as he had. However,
when taxi drivers arrived, it turned out that each taxi driver has a different fare for
1 kilometer.The director knows the distance from work to home for each employee
(unfortunately, all employees live in different directions, so it is impossible to send two employees in one car).
Now the director wants to find out how much to pay for a taxi for all employees.
Obviously, the director wants to pay as little as possible.

Input format: The first line contains N numbers through a space specifying distances in kilometers
from work to the homes of employees.The second line contains N numbers rates for one kilometer in a taxi.

Output format: The smallest price for delivery of all employees.
------------------------
Input data:
10 20 30
50 20 30

Program output:
1700

------------------------
Input data:
10 20 1 30 30
3 3 3 2 3

Program output:
243
------------------------
Input data:
1 2 3
1 2 3

Program output:
10
"""


def calculate_min_tax_fare() :
    min_price = 0
    for x, y in zip(list_of_employees_total_home_distance_in_km, list_of_taxi_fares_per_km):
        min_price += x * y
    print(min_price)


def collect_data() :
    global list_of_employees_total_home_distance_in_km, list_of_taxi_fares_per_km
    user_input1 = input()
    user_input2 = input()
    list_of_employees_total_home_distance_in_km = sorted(list(map(int, user_input1.split())), reverse=True)
    list_of_taxi_fares_per_km = sorted(list(map(int, user_input2.split())))
    calculate_min_tax_fare()


collect_data()

"""
After a lengthy meeting, the company's director decided to order a taxi to take the staff home. He ordered N cars
exactly as many employees as he had. However, when taxi drivers arrived,
it turned out that each taxi driver has a different fare for
1 kilometer.The director knows the distance from work to home for each employee (unfortunately,
all employees live in different directions, so it is impossible to send two employees in one car).
Now the director wants to select a taxi for each employee.
Obviously, the director wants to pay as little as possible.

Input format: The first line contains N numbers through a space
specifying distances in kilometers from work to the homes of employees.
The second line contains N fares for one kilometer in a taxi.
All distances are unique and all rates are unique too.

Output format: Give taxi cars integer indexes starting from zero.
For each employee print the index of the taxi they should choose.

Note: Loops, iterations, and list comprehensions are forbidden in this task.


------------------------
Input data:
10 20 30
50 20 30

Program output:
0 2 1

------------------------
Input data:
10 20 1 30 35
1 3 5 2 4

Program output:
4 1 2 3 0
"""


def calculate_original_index_of_taxi_fare():
    result_index_list = list(map(get_original_index, list_of_employees_total_home_distance_in_km))
    print(*result_index_list, sep=" ")


def get_original_index(employees_total_home_distance_in_km):
    return list_of_tax_fare_per_km.index(zipped_dictionary[employees_total_home_distance_in_km])


def collect_data():
    global sorted_list_of_employees_total_home_distance_in_km, \
        sorted_list_of_taxi_fares_per_km, \
        list_of_tax_fare_per_km,\
        list_of_employees_total_home_distance_in_km,\
        zipped_dictionary
    user_input1 = input()
    user_input2 = input()
    list_of_employees_total_home_distance_in_km = list(map(int, user_input1.split()))
    sorted_list_of_employees_total_home_distance_in_km = sorted(list_of_employees_total_home_distance_in_km,
                                                                reverse=True)
    list_of_tax_fare_per_km = list(map(int, user_input2.split()))
    sorted_list_of_taxi_fares_per_km = sorted(list_of_tax_fare_per_km)
    zipped_dictionary = dict(zip(sorted_list_of_employees_total_home_distance_in_km, sorted_list_of_taxi_fares_per_km))
    calculate_original_index_of_taxi_fare()


collect_data()

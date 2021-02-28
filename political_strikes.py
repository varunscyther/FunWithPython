"""
Political life in one country is very lively. There are K political parties in the country.
Each party regularly declares a national strike.
The days when at least one party goes on strike, provided it is not Saturday or Sunday (when nobody is working anyway),
are very damaging to the economy.
The i−th party declares strikes strictly every bi days, starting with the day with the number ai.
It means that the i−th party declares strikes on the days ai, ai+bi, ai+2bi etc.
If several parties go on strike on the same day, this is considered one national strike. In the calendar of the country
there are N days numbered from 1 to N.
The first day of the year is Monday, the sixth and seventh days of the year are weekends,the week consists of seven days


Input format: The program gets the number of days in year N(1≤N≤10^6) and the number of political parties
K(1≤K≤100). Next comes K lines describing the schedule of strikes. i−th line contains the numbers
ai and bi (1<=ai, bi<= N)

Output format: Print the number of strikes that took place during the year.


Comment: The first party declares strikes on days 2,5,8,11,14,17. The second party declares strikes on days
3,8,13,18. The third party - on days 9 and 17. Days 6,7,13,14 are days off. Thus, strikes will take place on days
2,3,5,8,9,11,17,18.


---------------------------------------------------------------------------------------------------------------
Input data:
19 3
2 3
3 5
9 8

Program output:
8

----------------------------------------------------------------------------------------------------------------

Input data:
5 2
1 2
2 2

Program output:
5

---------------------------------------------------------------------------------------------------------------
Input data:
1000 1
1 1

Program output:
715



"""
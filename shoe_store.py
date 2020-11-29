"""
The shoe store sells shoes of different sizes. It is known that one pair of shoes can be put on another if it is at least three sizes larger.
 A customer came to the store. Need to find how many pairs of shoes can offer him the seller so that customer can put them all on at the same time.

Input format: The first number is the size of the customer's foot (he will not be able to put on a smaller shoe), in the next line - the size of each pair of shoes in the store through a space.

Output format: Print one number - the maximum number of pairs of shoes that the customer can wear at the same time.

Possible tests -

--------------------------------------
Input data:
60
60 63

Program output:
2

-------------------------------------

Input data:
26
30 35 40 41 42

Program output:
3

--------------------------------------

Input data:
43
43

Program output:
1

--------------------------------------
Input:
13
11 22 33 44 55 66 77 88 99

Answer:
8

--------------------------------------
Input:
35
30 40 35 42 35

Answer:
2
"""


def compare_size_and_give_possible_options() :
    available_shoe_sizes_lst = list(map(int, formatted_data[1].split()))
    sorted_available_shoe_size_lst = sorted(available_shoe_sizes_lst, key=compare_size)

    for x in sorted_available_shoe_size_lst :
        if x < customer_shoe_size :
            sorted_available_shoe_size_lst.remove(x)

    result_lst = []
    for x in sorted_available_shoe_size_lst :
        if not result_lst :
            result_lst.append(x)
            y = x
        else :
            if x >= y + 3 :
                result_lst.append(x)
                y = x
    print(len(result_lst))


def compare_size(x) :
    global customer_shoe_size
    customer_shoe_size = int(formatted_data[0])
    if x > customer_shoe_size :
        return 1
    elif x < customer_shoe_size :
        return -1
    return 0


def collect_data() :
    global formatted_data
    user_data = []
    while True :
        line = input()
        if line :
            user_data.append(line)
        else :
            break
    formatted_data = "\n".join(user_data).split("\n")


collect_data()
compare_size_and_give_possible_options()

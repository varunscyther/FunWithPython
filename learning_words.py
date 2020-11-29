"""
Peter wants to learn new English words, but wants to do it in a certain sequence.
First he chooses short words, and if the words are the same length he chooses in lexicographical
order when reading from right to left. Help Peter to put the order of words from the given list.

Input format: The first line contains the number of words N.
The next N lines contain one word each.

Output format: Print the words in the specified order. Print each word on a separate line.

Possible output -

-------------------------------
Input data:
3
news
are
taxi

Program output:
are
taxi
news

-------------------------------

Input data:
9
west
tax
size
sea
use
think
yard
word
town

Program output:
sea
use
tax
yard
word
size
town
west
think
"""


def print_words__in_specific_order() :
    sorted_list = sorted(list_of_words, key=lambda x: (len(x), x[::-1]))
    print(*sorted_list, sep='\n')


def collect_data() :
    global formatted_data, no_of_words, list_of_words
    user_data = []
    list_of_words = []
    no_of_words = int(input())

    for i in range(0, no_of_words) :
        line = input()
        user_data.append(line)

    list_of_words = list("\n".join(user_data).split("\n"))


collect_data()
print_words__in_specific_order()

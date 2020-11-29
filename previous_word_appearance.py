"""
The text is given. A word is considered a sequence of non-space characters. Words
are separated by one or more spaces. For each word from this text find the index of
ts previous appearance in the text. The index of the first word is 0. If a word occur
the first time print −1

Input format: Text is supplied to the input. The input ends with an empty line.

Output format: Print the answer to the task.

Possible Inputs/Outputs -
-----------------------
Input data:
one two one
tho three


Program output:
-1 -1 0 -1 -1
-----------------------
Input data:
She sells sea shells on the sea shore;
The shells that she sells are sea shells I'm sure.
So if she sells sea shells on the sea shore,
I'm sure that the shells are sea shore shells.


Program output:
-1 -1 -1 -1 -1 -1 2 -1 -1 3 -1 -1 1 -1 6 9 -1 -1 -1 -1 11 12 14 15 4 5 22 -1 16 -1 10 25 23 13 26 -1 -1
------------------------
Input data:
aba aba;
aba @?"


Program output:
-1 -1 0 -1

"""
'''
First read the user input from multiple lines
and then create an list of data
'''


def collect_data() :
    global formatted_data
    user_data = []
    while True :
        line = input()
        if line :
            user_data.append(line)
        else :
            break
    formatted_data = "\n".join(user_data).split()


'''Now check the previous appearance of word '''


def check_previous_appearance_of_word() :
    input_dic = {}
    i = 0
    for x in formatted_data :
        input_dic[i] = x
        i = i + 1
    result_dic = {}
    result_list = []
    for k, v in input_dic.items() :
        result_list.append(result_dic.get(v, -1))
        result_dic[v] = k
    print(' '.join([str(v) for v in result_list]))


collect_data()
check_previous_appearance_of_word()
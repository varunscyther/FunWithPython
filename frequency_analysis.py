"""
The text is given. Print all unique words found in the text, one for each line. Words should be sorted by their frequency in the text,
 and in the lexicographical order, if they appear at the same frequency.

Input format: Text is supplied to the input. The input ends with an empty line.

Output format: Print the answer to the task.

Possible tests

--------------------------------
Input data:
hi
hi
what is your name
my name is bond
james bond
my name is damme
van damme
claude van damme
jean claude van damme


Program output:
damme
is
name
van
bond
claude
hi
my
james
jean
what
your
-------------------------------
Input data:
ai ai ai ai ai ai ai ai ai ai


Program output:
ai
"""


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


def split_text() :
    global text_list
    text_list = []
    for x in formatted_data :
        temp_lst = x.split()
        for y in temp_lst :
            text_list.append(y)


def calculate_frequency() :
    global text_frequency_dic
    text_frequency_dic = {}
    for text in text_list :
        last_frequency = text_frequency_dic.get(text)
        if last_frequency is not None :
            text_frequency_dic[text] = last_frequency + 1
        else :
            text_frequency_dic[text] = 1
    sorted_dic = sorted(text_frequency_dic.items(), key=lambda x : (-x[1], x[0]))
    for k, v in sorted_dic :
        print(k)


collect_data()
split_text()
calculate_frequency()

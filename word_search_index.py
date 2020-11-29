"""
Modern text assistants offer possible word completion options when you start typing a word.
This process should be very fast, so you need to search the first letters of the word.
For this purpose it is suggested to use one-letter and two-letter prefixes of words.
Write a program that builds a hierarchical index from a list of words,
where at the first level there is a prefix of length

1, at the second level there is a prefix of length
2, and at the next level there are full words.

Input format: The first line contains the number N the number of words.
The next N lines contain words.
The next line contains the name of the file to save the search index.

Output format: Write the resulting search index to the specified file.

Possible tests
-------------------------------------
Input data:
7
station
safety
quality
sales
quarterback
stability
standard
search_index.json

-------------------------------------
"""
import json
import operator


def collect_data() :
    global sorted_words_list, \
        output_file_name
    number_of_words = int(input())
    words_list = []
    for words in range(1, number_of_words + 1):
        words_list.append(input())
    output_file_name = input()
    sorted_words_list = sorted(map(str, words_list) ,reverse=True)


def index_words() :
    global merged_dic
    merged_dic = {}
    """Create dictionary with first level indexing"""
    dic_with_first_level_index = {}
    for word in sorted_words_list:
        dic_with_first_level_index.setdefault(word[0], {})
    sorted_dic_with_first_level_index = dict(sorted(dic_with_first_level_index.items(),
                                                    key=lambda x:x[0], reverse=True))

    """Create dictionary with second level indexing"""
    dic_with_second_level_index = {}
    for word in sorted_words_list:
        dic_with_second_level_index.setdefault(word[0:2], []).append(word)
        value = sorted(dic_with_second_level_index.setdefault(word[0:2]))
        dic_with_second_level_index[word[0:2]] = value

    """Now merge dictionaries"""
    for k, y in sorted_dic_with_first_level_index.items():
        for m, n in dic_with_second_level_index.items():
            if k == m[0]:
                merged_dic.setdefault(k, {}).update({m:n})


def write_output() :
    with open(output_file_name, 'w') as write_file :
        json.dump(merged_dic, write_file)


collect_data()
index_words()
write_output()

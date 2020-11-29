"""
Web spider crawled several websites to index the Internet pages.
It recorded the results of its work as a JSON file.
This file has the form of nested dictionaries, the site domain is written on the first level,
the available sections are written in the dictionary values,
then subsections, and so on. You need to print the pages in an easy-to-read format.

Input format: The first line contains the name of the JSON file

Output format: Print web addresses in lexicographical order

----------------------------------------------------
Input data:
input_03.json

Program output:
vz.com/news/12/4/1011.html
vz.com/news/12/4/798.html
vz.com/news/12/6/101.html
vz.com/news/12/6/2187.html
www.euro-football.com/article/29/10
www.euro-football.com/article/29/142
www.euro-football.com/article/31/508
www.euro-football.com/article/31/600
----------------------------------------------------
Input file content :

{
  "www.euro-football.com": {
    "article": {
      "29": {
        "10": {},
        "142": {}
      },
      "31": {
        "508": {},
        "600": {}
      }
    }
  },
  "vz.com": {
    "news": {
      "12": {
        "4": {
          "1011.html": {},
          "798.html": {}
        },
        "6": {
          "2187.html": {},
          "101.html": {}
        }
      }
    }
  }
}
"""
import json


def build_internal_list(dictionary, result_list) :

    for k, v in dictionary.items() :
        if bool(v) :
            result_list.append(k)
            build_internal_list(v, result_list)
        else :
            internal_list.append("/".join(result_list))
            internal_list.append("/".join(internal_list.append(k)))
            result_list


# def build_web_crawler_list() :
#     print(internal_list)
#     global intermediate_list
#     intermediate_list = []
#     url = []
#     for x in internal_list :
#         if x != "NONE" :
#             url += x + "/"
#         else :
#             intermediate_list.append(url[:-1])
#             url = ""
#     print(intermediate_list)


def collect_data_and_load_json() :
    global input_json_dict, internal_list
    input_json_dict = {}
    internal_list = []
    input_file_name = input()

    with open(input_file_name, 'r') as read_file :
        input_json_dict = json.load(read_file)

    build_internal_list(input_json_dict, internal_list)


collect_data_and_load_json()
# build_web_crawler_list()

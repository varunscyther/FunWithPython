from operator import itemgetter

words = input().split()
similarity_score = map(float, input().split())
filter_lst = list(filter(lambda x : float(x[0] > 0.5), list(zip(similarity_score, words))))
sorted_lst = sorted(filter_lst, key=itemgetter(0, 1), reverse=True)
result_list = map(itemgetter(1), sorted_lst)
print(*result_list, sep='\n')



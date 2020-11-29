"""
To create a quiz you need to select words similar to the correct answer.
 You are given proposed words and their similarity score. Leave only words with similarity score greater than 0.5.
 Print these words in descending order of similarity score.
Input format: The first line contains the proposed words. The second line contains similarity score of each word.
 It is guaranteed that all words have different similarity scores.

Output format: Print words in descending order of similarity score after filtering.

Note: Loops, iterations, and list comprehensions are forbidden in this task. Find some information about the function filter.

Possible test cases -

# car cars jeep mercedes motorcycle scooter truck van vehicle vehicles
# 0.99 0.74 0.65 0.61 0.63 0.64 0.67 0.61 0.78 0.6

car
vehicle
cars
truck
jeep
scooter
motorcycle
van
mercedes
vehicles

---------------------------------------------------

Input data:
cat computer mice monkeys mouse paw rat rats spider typing
0.47 0.39 0.59 0.44 1.00 0.40 0.46 0.42 0.38 0.37

Program output:
mouse
mice


"""

from operator import itemgetter

words = input().split()
'''Convert the second input in float'''
similarity_score = map(float, input().split())
'''Zip both the inputs and filter on the basis of score'''
filter_lst = list(filter(lambda x : float(x[0] > 0.5), list(zip(similarity_score, words))))
sorted_lst = sorted(filter_lst, key=itemgetter(0, 1), reverse=True)
'''Only get the words)'''
result_list = map(itemgetter(1), sorted_lst)
print(*result_list, sep='\n')



"""

Batch generator -
    At input you have a list of elements, you need to generate batches (non overlapping sub samples).
    At first shuffle (use random.shuffle) the input list. For a shuffled list with batch_size = 3
            - the result is: [1, 5, 8, 9, 3, 2, 0, 1, 2, 9] -> [1, 5, 8], [9, 3, 2], [0, 1, 2].
    Ignore the last part [9] in this example.

"""

# Built in modules
import random


def batch_gen(input_list, batch_size) :
    random.shuffle(input_list)

    batches = int(len(input_list) // batch_size)

    for b in range(batches):
        x_train = input_list[b * batch_size : (b + 1) * batch_size]
        yield x_train


if __name__ == '__main__' :
    generated_batch = batch_gen([1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 11 , 12, 15], 4)

    for i in generated_batch:
        print(i)

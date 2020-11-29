"""
Guess the number

August and Beatrice keep playing the game, but August started cheating. For each
Beatrice's question, he chooses the answer
 - YES
 - NO
Example - if August has a numbers between 1 and 5 , and Beatrice asked about numbers
1 and 3 , then August answers
-   NO
and if Beatrice asked about 1,3,4, then August answers
 - YES
But if Beatrice mentions exactly half of the remaining numbers in her question, then August always answers
 - NO
"""
global result_set
guess_largest_number = int(input())
mid_index = guess_largest_number // 2
create_first_half_values_set = set(range(1, mid_index + 1))
create_later_half_values_set = set(range(mid_index + 1, guess_largest_number + 1))

guess_incorrect = True
in_memory_guess_set = set()
result_set = set()


def print_set_items(values):
    print(' '.join(map(str, values)))


while guess_incorrect :
    user_guess_input = input()
    'Handling in case HELP option is not selected'
    if user_guess_input != "HELP":
        guess_set = set(list(map(int, user_guess_input.split())))
        'Handling in case HELP option is  selected'
        'Check whether half of the remaining numbers'
        if guess_set == create_first_half_values_set or guess_set == create_later_half_values_set :
            in_memory_guess_set = in_memory_guess_set | guess_set
            result_set = (create_first_half_values_set | create_later_half_values_set) - in_memory_guess_set
            print("NO")
        elif ((len(guess_set) >= len(create_first_half_values_set)) \
              or (len(guess_set) >= len(create_first_half_values_set))) \
                and (guess_set != create_first_half_values_set
                     and guess_set != create_later_half_values_set) :
            in_memory_guess_set = guess_set - in_memory_guess_set
            result_set = in_memory_guess_set
            print("YES")
            'Print in case when only one number is remaining in set'
        elif len(result_set) == 1 :
            print_set_items(sorted(result_set))
            break
        else :
            in_memory_guess_set = in_memory_guess_set | guess_set
            result_set = (create_first_half_values_set | create_later_half_values_set) - in_memory_guess_set
            print("NO")
        'Handling in case HELP option is  selected'
    elif user_guess_input == "HELP" :
        guess_incorrect = False
        print_set_items(sorted(result_set))
        break

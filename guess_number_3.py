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
possible_value_set = set(range(1, guess_largest_number + 1))

guess_incorrect = True


def print_set_items(values):
    print(' '.join(map(str, values)))


while guess_incorrect :
    user_guess_input = input()
    'Handling in case HELP option is not selected'
    if user_guess_input != "HELP" :
        guess_set = set(list(map(int, user_guess_input.split())))
        guess_set = guess_set & possible_value_set
        if len(guess_set) <= len(possible_value_set) / 2:
            possible_value_set = possible_value_set - guess_set
            print("NO")
        else:
            possible_value_set = guess_set
            print("YES")
    elif user_guess_input == "HELP":
        guess_incorrect = False
        print_set_items(sorted(possible_value_set))
        break

'''
projekt_2.py: druhý projekt do Engeto Online Python Akademie
author: Alžběta Karolyiová
email: akarolyiova@gmail.com
discord: betykar
'''
import random
import time


# Greeting and introduction.
my_separator = "-" * 47
print("Hi there!", my_separator,
      "I've generated a random 4 digit number for you.",
      "Let's play a bulls and cows game.", my_separator, sep="\n")

# Generating a four-digit number (unique digits, does not start with "0").
unique_numbers = []
for number in range(1000, 9999):
    if len(set(str(number))) == 4:
        unique_numbers.append(str(number))
random_number = random.choice(unique_numbers)
print(random_number)


# Creating a function for comparing numbers.
def compare_numbers(guess, random_number):
    bulls = 0
    cows = 0
    for i in range(len(guess)):
        if guess[i] == random_number[i]:
            bulls += 1
        elif guess[i] in random_number:
            cows += 1
    return (
        f"{bulls} {'bull' if bulls == 1 else 'bulls'}, "
        f"{cows} {'cow' if cows == 1 else 'cows'}"
    )


start_time = time.perf_counter()  # time count inicialisation
input_count = 0

# Input validation.
while True:
    guess = input("Enter a number: ")
    if len(guess) != 4:
        print("Please enter a four-digit number.")  # not four-digit numbers
        continue
    elif not guess.isnumeric():
        print("Input is not a number.")  # not numeric input
        continue
    elif guess[0] == "0":
        print("Number starts with zero.")  # input starst with 0
        continue
    elif len(set(guess)) < 4:
        print("Your number contains repeating digits.")  # duplicity
        continue
    else:
        result = (compare_numbers(guess, random_number))

        if result.startswith("4 bulls"):
            input_count += 1
            end_time = time.perf_counter()
            elapsed_time = round(end_time - start_time, 4)
            print(
                "Correct, you've guessed the right number"
                f" in {input_count}"
                f" {'guess' if input_count == 1 else 'guesses'}"
                f" and {elapsed_time} seconds!",
                my_separator,
                sep="\n"
            )

            if input_count <= 6:  # result message (classification of results)
                result_message = "amazing!"
            elif 7 <= input_count <= 16:
                result_message = "average."
            else:
                result_message = "not so good."
            print(f"That's {result_message}")
            break
        else:
            input_count += 1
            print(result)
            continue

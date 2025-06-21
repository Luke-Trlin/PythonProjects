import random

results_file = open("result_file.txt", "a")

def integer_checker(prompt):
    while True:
        try: 
            return(int(input(prompt)))
        
        except ValueError:
            print("Error! That is an invalid number")

def guess_checker(minimum, maximum):
    while True:
        guess = integer_checker("What Is Your Guess: ")
        if minimum <= guess <= maximum:
            return guess
        else:
            print("Number is outside the range of the values you set, retry your guess")




def replay_checker():
    while True:
        replay_detection = input("\nPlay Again? (y/n) ").lower()
        if replay_detection in ["y", "n", "yes", "no"]:
            return replay_detection[0]
        else: 
            print("Invalid Response")
            
        
def number_generator():
    range_minimum = integer_checker("What Do You Want The Minimum Number To Be: ")
    while True:
        range_maximum = integer_checker("What Do You Want The Maximum Number To Be: ")
        if range_maximum <= range_minimum:
            print("Invalid Maximum Number, Try Again")
        else:
            return(random.randint(range_minimum, range_maximum), range_minimum, range_maximum)
        
def gameplay_loop(target, minimum, maximum):
    guess_count = 0
    print(f"Im Thinking Of A Number Between {minimum} and {maximum}! ")
    while True:
        guess = guess_checker(minimum, maximum)
        if guess > target:
            print("Too High!")
            guess_count += 1
        elif guess < target:
            print("Too Low!")
            guess_count += 1

        else:
            guess_count += 1
            return guess_count 


def replay_loop():
    with open("result_file.txt", "a") as results_file:
        while True:

            generated_number, minimum, maximum = number_generator()
            total_guesses = gameplay_loop(generated_number, minimum, maximum)
            print(f"Well Done! The Number Was {generated_number}")
            print(f"You Got It In {total_guesses} guesses! \n")
            results_file.write("Minimum: " + str(minimum) + ", Maximum " + str(maximum) + ", Random Number " + str(generated_number) + ", Guess Count "  + str(total_guesses) + "\n")
            results_file.flush()
            replay_choice = replay_checker()
            if replay_choice == "n":
                print("Thanks For Playing!")
                break
        


replay_loop()





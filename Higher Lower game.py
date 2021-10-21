import random
from Data import data

def get_data():
    x = random.choice(data)
    return x

def format_data(x):
    name =x['name']
    description = x['description']
    country = x['country']
    return f"{name}, a {description}, from {country}"

def check_answer(guess, a_followers, b_followers):
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"

def game():
    should_continue = True
    a = get_data()
    b = get_data()
    score = 0
    while should_continue:
        a = b
        b = get_data()
        while a == b:
            b = get_data()

        print(f"Compare A: {format_data(a)}")
        print("vs")
        print(f"Against B: {format_data(b)}")

        guess = input("Who has more followers? A or B : ").lower()
        a_followers = a['follower_count']
        b_followers = b["follower_count"]

        is_correct = check_answer(guess,a_followers,b_followers)

        if is_correct:
            score += 1
            print(f"You are rite. Your score is {score}")
        else:
            should_continue = False
            print(f"you lost! Your final score is {score}")

game()
#James adebayo
#Lab 5
#Question 1

print("Neural Engine for Rapid Decisions artificial intelligence booting...")
print("NERD gaining consciousness...\n")
print("NERD: Hello, let's play dice! you can go first.\n")

import random
def roll_d20():
    return random.randint(1, 20)

def main():
    human_total = 0
    nerd_total = 0

    print("Human's turn:")
    for i in range(1,4):
        roll = roll_d20()
        human_total += roll
        print(f"Roll {i} is a {roll}")

    print("\nNERD's turn:")
    for i in range(1,4):
        roll = roll_d20()
        nerd_total += roll
        print(f"Roll {i} is a {roll}")

    print(f"\nHuman's total is: {human_total}")
    print(f"NERD's total is: {nerd_total}")

    if human_total > nerd_total:
        print("\nHuman's win!")
    elif nerd_total > human_total:
        print("NERD's win!")
    else:
        print("it's a tie!")

if __name__ == "__main__":
    main()
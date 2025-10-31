#James adebayo
#Lab 5
#Question 3

print("Vowel counting system booting...")

def vowel_counting_function(word_or_phrase):
    vowels = "aeiou"
    vowel_count = 0
    for char in word_or_phrase:
        if char.lower() in vowels:
            vowel_count += 1
    return vowel_count

def menu_function():
    while True:
        user_input = input("Enter a word or phrase: ")
        if user_input.lower() == "exit":
            break

        count = vowel_counting_function(user_input)
        print(f"{user_input} has {count} vowels")
    print("Vowel counting system shutting down...")

if __name__ == "__main__":
    menu_function()
import sys
import math
import random

# getting the values from the command line executed by process.php
number = int(sys.argv[1])
text = sys.argv[2]

# 1-Number Puzzle
# if the number is divisible by 2, its an even number, if not, it's an odd number
if number % 2 == 0:
    result_number = f"The number {number} is even. Its square root is {math.sqrt(number)}."
else:
    result_number = f"The number {number} is odd. Its cube is {number ** 3}."

# 2-Text Puzzle
#for every character in the text, it translates to Unicode, then into binary, and finally joining them in a string
binary_text = ' '.join(format(ord(char), '08b') for char in text)
#it adds 1 for each character that is in the string "aeiou"
vowel_count = sum(1 for char in text if char.lower() in 'aeiou')


# 3-Treasure Hunt
#getting the random number
secret_number = random.randint(1, 100)
#saving the number of attempts
attempts = 0
max_attempts = 5

# creating the treasure hunt result string
result_treasure = f'<span class="answer">The secret number is {secret_number}.</span>'

while attempts < max_attempts:
    guess = random.randint(1, 100)
    attempts += 1
    if guess == secret_number:
        # if the guess is correct, show the attempts and the final message
        result_treasure += f'<span class="answer">Attempt {attempts}: {guess} (Correct!)</span><span class="answer">You found the treasure in {attempts} attempts!</span>'
        break
    else:
        # if the guess is too high or low, show the attempts and gets the appropriate message
        response_attempt = "Too high!" if guess > secret_number else "Too low!"
            
        result_treasure += f'<span class="answer">Attempt {attempts}: {guess} ({response_attempt})</span>'
        
        if attempts == max_attempts:
            # if it's the final attempt, it shows the attempts and the final message
            result_treasure += '<span class="answer">You did not find the treasure.</span>'

# printing results, sending it to process.php, adding some classes for asigning the css style
print(f'<div class="asw_container"><b class="title">Number Puzzle:</b><span class="answer">{result_number}</span></div>')
print(f'<div class="asw_container"><b class="title">Text Puzzle:</b><span class="answer">Binary: {binary_text}</span><span class="answer">Vowel Count: {vowel_count}</span></div>')
print(f'<div class="asw_container"><b class="title">Treasure Hunt:</b>{result_treasure}</div>')


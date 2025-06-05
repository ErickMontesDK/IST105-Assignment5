import random
from django.shortcuts import render
from django.http import HttpResponse
from .forms import PuzzleForm

# Create your views here.
def puzzle(request):
    if request.method == 'POST':
        form = PuzzleForm(request.POST)
        if form.is_valid():
            # Getting the data from the form
            number = form.cleaned_data['number']
            text = form.cleaned_data['text']
            
            # 1-Number Puzzle
            # if the number is divisible by 2, its an even number, if not, it's an odd number
            if number % 2 == 0:
                number_puzzle = f"The number {number} is even. Its square root is {number**0.5}."
            else:
                number_puzzle = f"The number {number} is odd. Its cube is {number ** 3}."
                
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
            attempts_results = {}
            
            # creating the treasure hunt result string
            while attempts < max_attempts:
                guess = random.randint(1, 100)
                attempts += 1
                if guess == secret_number:
                    # if the guess is correct, show the attempts and the final message
                    attempts_results[attempts] = {
                        "attempt_info": f"Attempt {attempts}: {guess} (Correct!)",
                        "treasure_info": f"You found the treasure in {attempts} attempts!"
                    }
                    break
                else:
                    # if the guess is too high or low, show the attempts and gets the appropriate message
                    response_attempt = "Too high!" if guess > secret_number else "Too low!"
                    attempts_results[attempts] = {
                        "attempt_info": f"Attempt {attempts}: {guess} ({response_attempt})",
                    }
                    
                    if attempts == max_attempts:
                        # if it's the final attempt, it shows the attempts and the final message
                        attempts_results[attempts] = {
                            "treasure_info": f"You did not find the treasure."
                        }
            
            return render(request, 'result.html', {
                'number_puzzle': number_puzzle,
                'binary_text': binary_text,
                'vowel_count': vowel_count,
                'attempts_results': attempts_results
            })
    else:
        form = PuzzleForm()
        return render(request, 'puzzle.html', {
            'form': form,
        })



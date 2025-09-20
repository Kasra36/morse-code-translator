from MorseCode import MorseCode
from MorseCode import ALPHA_TO_MORSE, MORSE_TO_ALPHA
from art import logo

print(logo)

while True:
    try:
        print("\nChoose a number to proceed:")
        print("1. Translate to Morse Code")
        print("2. Translate from Morse Code")
        print("3. Quit")

        user_choice = int(input("Your choice: "))
        
        if user_choice == 1:
            user_prompt = input("Enter your text: ")
            ms_code = MorseCode(user_prompt)

            try:
                ms_code.encoder()
                ms_code.player()
                
            except KeyError:
                print("Only the following characters are allowed:",
                      ", ".join(ALPHA_TO_MORSE.keys()))
        
        elif user_choice == 2:
            user_prompt = input("Enter Morse Code: ")
            ms_code = MorseCode(user_prompt)

            try:
                ms_code.decoder()
        
            except KeyError:
                print("Only the following sequences are allowed:",
                      ", ".join(MORSE_TO_ALPHA.keys()))
        
        elif user_choice == 3:
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

    except ValueError:
        print('Invalid input. Please choose among given numbers only.')


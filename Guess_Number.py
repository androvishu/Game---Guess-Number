# Exercise 3- Guess Numbers
def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.SpVoice")
    speak.speak(str)
n = 21
i = 5
while True:
    print("Remaining_attempt:=", i)
    speak(f"Remaining attempt {i} Times")
    i = i - 1
    inp = int(input("Enter the number:="))

    if inp > n:
        print("you enter the large number!\n")
        speak(f"you enter the larger number")
        if i >= 1:
            continue
        else:
            print("Game Over!")
            break
    elif inp < n:
        print("you enter the smaller number!\n")
        speak("you enter the smaller number!")
        if i >= 1:
            continue
        else:
            print("Game Over!")
            speak("Game Over")
            break
    elif inp == n:
        print("You Won! in ", i)
        speak(f"You Won in {i} Times Thanks for Playing my game")
        break


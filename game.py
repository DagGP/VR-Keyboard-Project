import random
import time
import threading
import Controller

sentences = [
    "Hello",
    "My name is Pol",
    "Welcome",
]

def main():
    def run_function_in_thread():
        # Create a thread to run the function
        thread = threading.Thread(target=Controller.all)
        thread.start()

    
    run_function_in_thread()
    print("Welcome to the typing game!")
    print("Type the following sentences as fast as you can:\n")

    while True:
        sentence = random.choice(sentences).lower()
        print(sentence)
        start_time = time.time()
        user_input = input().lower()
        end_time = time.time()

        if user_input == sentence:
            elapsed_time = end_time - start_time
            print("Great job! You typed the sentence correctly in {:.2f} seconds.\n".format(elapsed_time))
        else:
            print("Sorry, you made a mistake. Try again.\n")

main()
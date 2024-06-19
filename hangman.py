#Teka huruf/aksara pada perkataan

import random

#senarai nama negeri di malaysia
#6kali percubaan
def hangman():
    word_list = ["kedah", "selangor", "kelantan", "pahang", "sabah", "sarawak", "terengganu", "perak", "johor", "melaka", "perlis", "negeri sembilan", "pulau pinang", "kuala lumpur"]
    chosen_word = random.choice(word_list)
    word_length = len(chosen_word)
    display = ["_"] * word_length
    guesses = 6

#pengenalan hangman
    
    print("\nSelamat Datang!")
    print("Jom Teka Nama Negeri Di Malaysia")
    print("Arahan: Masukkan huruf atau aksara\n")
    print("Selamat mencuba\n")
    
    while guesses > 0 and "_" in display:
        print(f"Negeri : {' '.join(display)}")
        guess = input("Huruf anda: ").lower()
        
#huruf/aksara yang dimasukkan oleh user
        if guess in chosen_word:
            for index, letter in enumerate(chosen_word):
                if letter == guess:
                    display[index] = guess
        else:
            guesses -= 1
            print(f"Salah huruf. Anda mempunyai {guesses} peluang menjawab.")
        
        if "_" not in display:
            print(f"Tahniah! nama negeri adalah : {''.join(display)}")
            break
        elif guesses == 0:
            print(f"Permainan Tamat: {chosen_word}")

hangman()

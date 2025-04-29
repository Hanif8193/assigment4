import random

def hangman():
    words = ['python', 'computer', 'science', 'hangman', 'project']
    word = random.choice(words)
    guessed_letters = []
    tries = 6  # غلطیوں کی زیادہ سے زیادہ اجازت

    print("🎉 Welcome to Hangman Game!")
    print("_ " * len(word))

    while tries > 0:
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("⚠️ Please enter a single alphabet letter.")
            continue

        if guess in guessed_letters:
            print("⛔ You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("✅ Correct!")
        else:
            tries -= 1
            print(f"❌ Wrong! You have {tries} tries left.")

        # لفظ کی موجودہ حالت دکھانا
        display_word = ''
        for letter in word:
            if letter in guessed_letters:
                display_word += letter + ' '
            else:
                display_word += '_ '
        print(display_word)

        # جیت کی جانچ
        if all(letter in guessed_letters for letter in word):
            print("🎉 Congratulations! You guessed the word:", word)
            break

    if tries == 0:
        print("💀 You lost! The word was:", word)

# Start the game
hangman()

import random
from hangman_mappings import hang_man_mappings
from hangman_match import HangmanMatch
from nations import nations


def start_game_loop():
    """Starts a new console based hangman match with a random word (a nation)."""

    max_attempts = len(hang_man_mappings)
    private_term = random.choice(nations)
    match = HangmanMatch(private_term, max_attempts)
    print(f"Secret term: {match.get_public_term_string()}")

    while not (match.has_won() or match.has_lost()):
        try:
            next_letter = input("Please enter your next move (a single letter): ")
            guess_correct = match.make_move(next_letter)
        except ValueError:
            print("Please restrict yourself to exact one letter at a time!")
        except KeyboardInterrupt:
            print("\nSee you next time!")
            return 0
        else:
            if guess_correct:
                print(f"Secret term: {match.get_public_term_string()}")
            else:
                print(hang_man_mappings[max_attempts - match.attempts - 1])
                print(f"Secret term: {match.get_public_term_string()}")

    if match.has_won():
        print("Congratulations, you have won the game. This time...")
    else:
        print("YOU LOSE. Try again, you fool...")


if __name__ == "__main__":
    start_game_loop()

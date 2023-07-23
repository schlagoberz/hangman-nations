class HangmanMatch:
    """Represents a hangman-nations match."""

    def __init__(self, private_term, attempts):
        """Initializes a new match with a given private term and a number of maximum attempts."""

        self.private_term = list(private_term)
        self.public_term = list("*" * len(private_term))
        self.attempts = attempts

    def has_won(self):
        return self.attempts > 0 and self._terms_equal()

    def has_lost(self):
        return self.attempts <= 0

    def make_move(self, letter):
        if len(letter) != 1:
            raise ValueError("You have to specify exactly one letter at a time.")
        elif self.has_won() or self.has_lost():
            raise ValueError("You cannot make another move since the game is over.")

        if letter in self.private_term:
            for index in range(len(self.private_term)):
                if self.private_term[index] == letter:
                    self.public_term[index] = letter
            return True
        else:
            self.attempts -= 1
            return False

    def get_public_term_string(self):
        return "".join(self.public_term)

    def _terms_equal(self):
        for index in range(len(self.private_term)):
            if self.private_term[index] != self.public_term[index]:
                return False

        return True

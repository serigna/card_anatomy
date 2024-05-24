class CardAccount:

    def __init__(self, card_num, card_pin):
        self.card_num = card_num
        self.card_pin = card_pin
        self.logged_in = False
        self.balance = 0

    def login(self, card_num, card_pin):
        if card_num == self.card_num and card_pin == self.card_pin:
            self.logged_in = True
            return True, "You have successfully logged in!"

    def display_balance(self):
        if self.logged_in:
            print("Balance:", self.balance, "\n")

    def logout(self):
        self.logged_in = False
        return False, "You have successfully logged out!"

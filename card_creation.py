import random


class CardCreation:
    """ Represents card creation object. """
    card_issuer_id = "400000"

    def __init__(self):
        self.card_number = self.card_issuer_id + str(random.randint(1000000000, 9999999999))
        self.card_pin = str(random.randint(1000, 9999))

    def print_card_details(self):
        print(f"Your card number:\n{self.card_number}")
        print(f"Your card PIN:\n{self.card_pin}")

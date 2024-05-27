import random


class CardCreation:
    """ Represents card creation object. """
    card_issuer_id = "400000"

    def __init__(self):
        self.card_number = self._generate_card_number()
        self.card_pin = str(random.randint(1000, 9999))

    def print_card_details(self) -> None:
        print(f"Your card number:\n{self.card_number}")
        print(f"Your card PIN:\n{self.card_pin}")

    def _generate_base_card_number(self) -> str:
        return self.card_issuer_id + str(random.randint(100000000, 999999999))

    def _generate_card_number(self) -> str:
        card_num = self._generate_base_card_number()
        processed_digits_sum = self.luhn_algorithm(
            list(map(int, card_num))
        )
        last_digit = (10 - processed_digits_sum) % 10
        card_num = card_num + str(last_digit)
        return card_num

    @staticmethod
    def luhn_algorithm(digits: list) -> int:
        total_sum = 0
        for i, digit in enumerate(digits):
            if i % 2 == 0:
                digit *= 2
                if digit > 9:
                    digit -= 9
            total_sum += digit
        return total_sum

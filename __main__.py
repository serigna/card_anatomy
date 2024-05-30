from card_creation import CardCreation
from card_account import CardAccount
import sqlite3
from sqlite3 import Cursor, Connection
import os


def initialize_db(db_name: str) -> tuple[Connection, Cursor]:
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()
    return connection, cursor


def create_table(c: Cursor):
    c.execute("""CREATE TABLE card(
    id INT,
    number TEXT,
    pin TEXT,
    balance INT DEFAULT 0);
    """)


conn, cur = initialize_db('card.s3db')
if not os.path.exists("./card.s3db"):
    create_table(cur)

menu_active = 1
user_account = None

while menu_active != 0:
    menu_active = int(input("""1. Create an account
2. Log into account
0. Exit\n"""))

    if menu_active == 1:
        print("Your card has been created")
        obj_ = CardCreation()
        obj_.print_card_details()
        user_account = CardAccount(obj_.card_number, obj_.card_pin)
        obj_.insert_data_to_db(conn, cur)
        print()

    if menu_active == 2:
        card_num = input("Enter your card number:\n")
        card_pin = input("Enter your PIN:\n")

        logged_state, login_message = user_account.login(card_num, card_pin)
        print("\n", login_message, "\n")

        while logged_state is True:
            print("1. Balance", "2. Log out", "0. Exit", sep="\n")
            account_action = int(input())

            if account_action == 1:
                user_account.display_balance()
            if account_action == 2:
                logged_state, login_message = user_account.logout()
                print(login_message)
            if account_action == 0:
                print("\nBye!")
                exit()

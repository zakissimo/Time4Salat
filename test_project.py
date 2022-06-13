import os
import re
from datetime import datetime
import requests
from project import make_log, parse, get_next_salat

now = datetime.now()
today_string = now.strftime("%D")
log_path = "./Time4Salat.json"
url = "https://mawaqit.net/fr/gm-saint-denis"

r = requests.get(url)
regex_data = re.findall(r"times\":\[(.*?)\]", r.text)
time_string = str(regex_data[0])[1:-1].replace('"', "").split(",")


def test_parse():
    assert str(time_string) == parse()


def test_make_log():
    make_log(log_path, today_string)
    assert os.path.exists(log_path) is True


def test_get_next_salat():
    assert isinstance(get_next_salat(now, time_string), str)

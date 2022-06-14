# Time4Salat

Video presentation [here](https://youtu.be/12huQGLWDj8).

Time4Salat is a small python script that scrapes [mawaqit](https://mawaqit.net) and parses the website to determine when is the next islamic prayer.

Salat means prayer in arabic.

## Why ?

Because I found myself checking multiple times a day the mawaqit website. I always had my browser open, and it felt very inefficient. I'm also using a [tiling window manager](https://en.wikipedia.org/wiki/Tiling_window_manager) and can seemlessly integrate the output of my script in my bar.

![Qtile bar](./2022-06-13_14-31.png)

## Requirements

The only outside library is [requests](https://pypi.org/project/requests/)

```cmd
$ git clone https://github.com/zakissimo/Time4Salat
$ cd Time4Salat
$ pip install -r requirements.txt
```

## Usage

Replace the 47th line with the mawaqit link corresponding to the closest city to you.

```python
url = "https://mawaqit.net/fr/gm-saint-denis"
```

[Find the list of all mosques using mawaqit](https://mawaqit.net/en/#mosquees)

```cmd
$ python Time4Salat.py
```

The script outputs the time remaining until the next prayer, unless it's between midnight and the time for the first prayer. In which case it will simply display the time for the [fajr prayer](https://en.wikipedia.org/wiki/Fajr_prayer).

## How It Works

The script creates a log file `log_path = "./Time4Salat.json"` where Time4Salat.py is located. The content is a dictionnary with two values: 
 - Today's date
 - Today's prayer's times

```python
def make_log(log_path, today_string):

    to_encode = {
        "today": today_string,
        "salat_table": parse()
    }

    with open(log_path, "w", encoding="utf8") as log_file:
        json.dump(to_encode, log_file)
```

If a logfile already exists it checks the date and compares it to the current date, if they match the logged times are used to calculate the duration to the next prayer. If they don't match, the content of the logfile gets replaced by today's values. This has the benefit of only using the internet once a day, even if the script is ran multiple times a day.

[Regular expressions](https://docs.python.org/3/library/re.html) are used to parse the website.

```python
def parse():

    url = "https://mawaqit.net/fr/gm-saint-denis"

    r = requests.get(url)
    regex_data = re.findall(r"times\":\[(.*?)\]", r.text)
    time_string = str(regex_data[0])[1:-1].replace('"', "").split(",")

    return str(time_string)
```

## Possible Improvements

Add arguments to change the 'mawaqit' url and the path of the logfile.

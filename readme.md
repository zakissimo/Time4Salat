# Time4Salat

---

Time4Salat is a small python script that scrapes [mawaqit](https://mawaqit.net) and parses the website to determine when is the next islamic prayer.

Salat means prayer in arabic.

## Why ?

Because I found myself checking multiple times a day the mawaqit website. I always had my browser open, and it felt very inefficient. I'm also using a [tiling window manager](https://en.wikipedia.org/wiki/Tiling_window_manager) and can seemlessly integrate the output ofmy script in my bar.  

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

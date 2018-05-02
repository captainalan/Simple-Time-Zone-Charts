# Time Table Generator

This program was written to solve the practical problem of giving
calls to overseas family and friends. It simply outputs a Markdown
table to standard output alligning hours across two time zones.

Tables will appear something like:

| US/Pacific   | Asia/Tokyo   |
| ------------ | ------------ |
|        23:00 |        15:00 |
|         0:00 |        16:00 |
|         1:00 |        17:00 |
|         2:00 |        18:00 |
|         3:00 |        19:00 |
|         4:00 |        20:00 |
|         5:00 |        21:00 |
|         6:00 |        22:00 |
|         7:00 |        23:00 |
|         8:00 |         0:00 |
|         9:00 |         1:00 |
|        10:00 |         2:00 |
|        11:00 |         3:00 |
|        12:00 |         4:00 |
|        13:00 |         5:00 |
|        14:00 |         6:00 |
|        15:00 |         7:00 |
|        16:00 |         8:00 |
|        17:00 |         9:00 |
|        18:00 |        10:00 |
|        19:00 |        11:00 |
|        20:00 |        12:00 |
|        21:00 |        13:00 |
|        22:00 |        14:00 |

Now, by default, I just convert between Pacific Time and Tokyo Time.

Plain text tables may be converted to HTML, LaTeX etc. using Pandoc. 

    python3 time_table.py PST GMT > myTable.md
    pandoc myTable.md -o forTheWeb.html

## Dependencies

Made with Python 3.

- [pytz](https://github.com/newvem/pytz) library.



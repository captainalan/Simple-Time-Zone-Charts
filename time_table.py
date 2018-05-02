import sys
from datetime import datetime, timedelta
import pytz # Time zone info

"""Read in time offset as command line arguments"""

# Change the default families here
def makeTable(timeZone1='US/Pacific', timeZone2='Asia/Tokyo', hrs=24):
    """Generate a Markdown table aligned by hours
    Table will contain `hrs` rows"""

    """ From the pytz documentation, a suggestion:
    The preferred way of dealing with times is to always work in UTC,
    converting to localtime only when generating output to be read
    by humans."""
    utc = pytz.utc

    try:
        fromTimeZone = pytz.timezone(timeZone1)
        toTimeZone = pytz.timezone(timeZone2)
    except:
        print("Invalid timezone given")
        raise

    # Get today in UTC (Universal time)
    # Then generate times in the two target times zones from the UTC
    # representation.

    today = datetime.today()
    hrOnlyFormat = "%H"
    # print(today.strftime(hrOnlyFormat))
    # today.astimezone(fromTimeZone).strftime(hrOnlyFormat)
    # print(today.astimezone(toTimeZone))

    # Table Header
    print("| {:<13}| {:<12} |".format(timeZone1,timeZone2))
    print("| ------------ | ------------ |")
    for i in range(hrs):
        # Print nicely formatted rows in Markdown
        pass
        fromHour = \
        (int(today.astimezone(fromTimeZone).strftime(hrOnlyFormat))
                + i) % 24
        toHour = \
        (int(today.astimezone(toTimeZone).strftime(hrOnlyFormat))
                + i) % 24
        print("| {0: >9}:00 | {1: >9}:00 |".format(fromHour, toHour)) 

def main():
    fromTimeZone, toTimeZone = "",""
    try:
        # 0th sys.argv is the filename
        fromTimeZone = sys.argv[1]
        toTimeZone = sys.argv[2]
    except:
        pass
        # print("We have a problem.")

    makeTable()

if __name__ == "__main__":
    main()



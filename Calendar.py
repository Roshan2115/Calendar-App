import calendar
import datetime
import sys
#import pdb


def Calendar(year, month, day):
    cal = calendar.monthcalendar(year, month)
    #pdb.set_trace()
    header = f" {calendar.month_name[month]} {year}"
    days_of_week = "Mo  Tu  We  Th  Fr  Sa  Su "
    print(header.center(len(days_of_week) * 1))
    print(days_of_week)

    for week in cal:
        for day_num in week:
            if day_num == 0:
                print(" ", end=" ")
            elif day_num == day:
                print(f"[{day_num:1d}]", end="")
            else:
                print(f"{day_num:3d}", end=" ")
        print()


def calculate_new_date(base_date, offset):
    return base_date + datetime.timedelta(days=offset)


def main():
    if len(sys.argv) == 1:
        today = datetime.date.today()
        Calendar(today.year, today.month, today.day)
    elif len(sys.argv) == 2 and sys.argv[1] == '-help':
        print("Help:This application should be run with the following command line parameters:")
        print("A positive integer,a negative integer,or zero.")
        print("The positive integer cannot be more than 12 or less than-12.")
        print("example:pythoncalendar_app.py +5")
        print("example:pythoncalendar_app.py -3")
    elif len(sys.argv) == 2 and sys.argv[1].isdigit():
        offset = int(sys.argv[1])
        if -12 <= offset <= 12:
            today = datetime.date.today()
            new_date = calculate_new_date(today, offset * 30)
            Calendar(new_date.year, new_date.month, today.day)
        else:
            print("Invalid offset.Please use a positive integer,a negative integer,or zero.")
    else:
        print("Invalid Command Line Parameters. Use'-help' For Assitance.")


if __name__ == "__main__":
    main()


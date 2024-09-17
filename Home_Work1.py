from datetime import datetime

#func for counting days from today date
def get_days_from_today(time_date):

    try:
        converted_date = datetime.strptime(time_date, "%Y-%m-%d").date()
    except ValueError:
        converted_date = datetime.strptime(time_date, "%Y.%m.%d").date()

    today_date = datetime.now().date() #today date
    diff_days = today_date - converted_date #counting

    return diff_days.days

print(get_days_from_today('2024.03.12'))

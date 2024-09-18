from datetime import datetime


#func for counting days from today date
def get_days_from_today(time_date):
    try:
        converted_date = datetime.strptime(time_date, "%Y-%m-%d").date()
        today_date = datetime.now().date()
        diff_days = today_date - converted_date
        return diff_days
    except ValueError:
        print('Value i`snt correct')
        return None


print(get_days_from_today('2024-3-12'))
print(get_days_from_today("12.2.2000"))

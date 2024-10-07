from datetime import datetime

def get_days_from_today(date : str) -> int:
    now = datetime.now()
    date_datetime = datetime.strptime(date,"%Y-%m-%d")
    return -(now - date_datetime).days

print(get_days_from_today('2024-10-5'))
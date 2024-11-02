from datetime import datetime

def get_days_from_today(date : str) -> int:
    now = datetime.today()
    result = 0
    try:
        date_datetime = datetime.strptime(date,"%Y-%m-%d")
        result = -(now - date_datetime).days
    except ValueError:
        print("Incorect date foramat")
    
    return result

print(get_days_from_today('2024-10-5'))
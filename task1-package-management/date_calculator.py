from datetime import datetime

def date_difference(date1: str, date2: str) -> int:
    try:
        d1 = datetime.strptime(date1, "%Y-%m-%d")
        d2 = datetime.strptime(date2, "%Y-%m-%d")
        return (d2 - d1).days
    except ValueError as e:
        raise ValueError(f"Invalid date format. Please use 'YYYY-MM-DD'. Error: {e}")
try:
    d1=input(print("please Enter first date in YYYY-MM-DD format"))
    d2=input(print("please Enter second date in YYYY-MM-DD format"))
    print(date_difference(d1,d2))  
except ValueError as err:
    print("Error")
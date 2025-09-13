
import datetime

def adjust_position_size(volatility_index=20, max_size=1.0):
    if volatility_index > 30:
        return max_size * 0.5
    return max_size

def blackout_period():
    today = datetime.date.today()
    if today.day <= 7 and today.weekday() == 2:
        return True
    return False

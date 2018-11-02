from datetime import datetime
now = datetime.now()
now.year, now.month, now.day
delta = datetime(2011, 1, 7) - datetime(2008, 6, 24, 8, 15)
delta.days, delta.seconds
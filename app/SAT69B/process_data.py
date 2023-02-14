import pandas as pd
import schedule
import time

from .webscraping import webscrapping_69b

def formating_data():
    df = webscrapping_69b()

def migrate_data():
    pass

# Program when need to get the list.
schedule.every().day.at('06:00').do(formating_data)

while True:
    schedule.run_pending()
    time.sleep(1)

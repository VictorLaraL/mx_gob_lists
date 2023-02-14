import pandas as pd

from .webscraping import webscrapping_69b

def migrate_data():
    df = webscrapping_69b()
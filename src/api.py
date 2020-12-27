import pandas as pd
import requests


class Api(object):
    def __init__(self):
        self.BASE_URL = 'https://exoplanetarchive.ipac.caltech.edu/cgi-bin/nstedAPI/nph-nstedAPI?&'
        self.BASE_FORMAT = 'json'
    
    def get_table(self, table: str) -> None:
        url = f'{self.BASE_URL}&table={table}&format={self.BASE_FORMAT}'
        response = requests.get(url)
        return pd.DataFrame(response.json())

    def write_table(self, df: pd.DataFrame, name: str):
        df.to_csv(f'{name}.csv', index=False)

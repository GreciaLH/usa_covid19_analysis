import requests
import pandas as pd
from pathlib import Path

def get_state_data():
    url = "https://api.covidtracking.com/v1/states/daily.json"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        df = pd.DataFrame(data)
        df['date'] = pd.to_datetime(df['date'], format='%Y%m%d')
        df = df.sort_values(['state', 'date'])
        return df
    else:
        print(f"Error al obtener datos: {response.status_code}")
        return None

def save_data(df, filename):
    data_dir = Path(__file__).parent.parent.parent / 'data' / 'raw'
    data_dir.mkdir(parents=True, exist_ok=True)
    df.to_csv(data_dir / filename, index=False)
    print(f"Datos guardados en {data_dir / filename}")

if __name__ == "__main__":
    covid_data = get_state_data()
    if covid_data is not None:
        save_data(covid_data, 'usa_covid19_data.csv')
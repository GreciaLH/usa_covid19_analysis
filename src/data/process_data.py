import pandas as pd
from pathlib import Path

def load_data(filename):
    data_dir = Path(__file__).parent.parent.parent / 'data' / 'raw'
    return pd.read_csv(data_dir / filename, parse_dates=['date'])

def process_data(df):
    # Eliminar filas con valores nulos en columnas críticas
    critical_columns = ['state', 'positive', 'death', 'hospitalized']
    df = df.dropna(subset=critical_columns)

    # Calcular la tasa de mortalidad
    df['mortality_rate'] = (df['death'] / df['positive']) * 100

    # Calcular casos nuevos diarios
    df = df.sort_values(['state', 'date'])
    df['new_cases'] = df.groupby('state')['positive'].diff()

    return df

def save_processed_data(df, filename):
    data_dir = Path(__file__).parent.parent.parent / 'data' / 'processed'
    data_dir.mkdir(parents=True, exist_ok=True)
    df.to_csv(data_dir / filename, index=False)
    print(f"Datos procesados guardados en {data_dir / filename}")

if __name__ == "__main__":
    raw_data = load_data('usa_covid19_data.csv')
    processed_data = process_data(raw_data)
    save_processed_data(processed_data, 'cleaned_covid19_data.csv')
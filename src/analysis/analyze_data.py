import pandas as pd
import numpy as np
from pathlib import Path

def load_data():
    data_dir = Path(__file__).parent.parent.parent / 'data' / 'processed'
    return pd.read_csv(data_dir / 'cleaned_covid19_data.csv', parse_dates=['date'])

def analyze_data(df):
    results = {}

    # Estados más afectados
    results['top_5_states'] = df.groupby('state')['positive'].max().nlargest(5)

    # Tasa de mortalidad promedio
    results['avg_mortality_rate'] = df['mortality_rate'].mean()

    # Estado con la tasa de mortalidad más alta
    results['highest_mortality_rate'] = df.groupby('state')['mortality_rate'].mean().idxmax()

    # Correlación entre casos positivos y hospitalizaciones
    results['correlation'] = df['positive'].corr(df['hospitalized'])

    # Día con más casos nuevos
    results['peak_new_cases_date'] = df.loc[df['new_cases'].idxmax(), 'date']

    return results

def save_results(results):
    report_dir = Path(__file__).parent.parent.parent / 'reports'
    report_dir.mkdir(parents=True, exist_ok=True)
    
    with open(report_dir / 'analysis_results.txt', 'w') as f:
        for key, value in results.items():
            f.write(f"{key}: {value}\n")
    
    print("Resultados del análisis guardados en reports/analysis_results.txt")

if __name__ == "__main__":
    df = load_data()
    results = analyze_data(df)
    save_results(results)
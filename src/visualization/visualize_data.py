import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

def load_data():
    data_dir = Path(__file__).parent.parent.parent / 'data' / 'processed'
    return pd.read_csv(data_dir / 'cleaned_covid19_data.csv', parse_dates=['date'])

def plot_total_cases_by_state(df):
    plt.figure(figsize=(12, 6))
    cases_by_state = df.groupby('state')['positive'].max().sort_values(ascending=False)
    cases_by_state.plot(kind='bar')
    plt.title('Casos totales de COVID-19 por estado')
    plt.xlabel('Estado')
    plt.ylabel('Número de casos')
    plt.xticks(rotation=90)
    plt.tight_layout()
    save_plot('total_cases_by_state.png')

def plot_cases_evolution(df):
    plt.figure(figsize=(12, 6))
    top_5_states = df.groupby('state')['positive'].max().nlargest(5).index
    for state in top_5_states:
        state_data = df[df['state'] == state].sort_values('date')
        plt.plot(state_data['date'], state_data['positive'], label=state)
    plt.title('Evolución de casos en los 5 estados más afectados')
    plt.xlabel('Fecha')
    plt.ylabel('Número de casos')
    plt.legend()
    plt.tight_layout()
    save_plot('cases_evolution.png')

def plot_mortality_rate(df):
    plt.figure(figsize=(12, 6))
    mortality_rate = df.groupby('state')['mortality_rate'].mean().sort_values(ascending=False)
    mortality_rate.plot(kind='bar')
    plt.title('Tasa de mortalidad promedio por estado')
    plt.xlabel('Estado')
    plt.ylabel('Tasa de mortalidad (%)')
    plt.xticks(rotation=90)
    plt.tight_layout()
    save_plot('mortality_rate_by_state.png')

def save_plot(filename):
    plot_dir = Path(__file__).parent.parent.parent / 'reports' / 'figures'
    plot_dir.mkdir(parents=True, exist_ok=True)
    plt.savefig(plot_dir / filename)
    plt.close()

if __name__ == "__main__":
    df = load_data()
    plot_total_cases_by_state(df)
    plot_cases_evolution(df)
    plot_mortality_rate(df)
    print("Visualizaciones generadas y guardadas.")
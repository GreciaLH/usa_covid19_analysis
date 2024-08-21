# Análisis de COVID-19 en Estados Unidos

Este proyecto analiza los datos históricos de COVID-19 en Estados Unidos utilizando la API pública de The COVID Tracking Project.

## Tabla de Contenidos

- [Requisitos](#requisitos)
- [Configuración](#configuración)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Uso](#uso)
- [Scripts](#scripts)
- [Análisis en Jupyter Notebook](#análisis-en-jupyter-notebook)
- [Contribuir](#contribuir)
- [Licencia](#licencia)

## Requisitos

- Python 3.7+
- pip
- virtualenv (opcional, pero recomendado)

## Configuración

1. Clona este repositorio:
   ```
   git clone https://github.com/tu-usuario/usa_covid19_analysis.git
   cd usa_covid19_analysis
   ```

2. (Opcional) Crea y activa un entorno virtual:
   ```
   python -m venv venv
   source venv/bin/activate  # En Windows usa `venv\Scripts\activate`
   ```

3. Instala las dependencias:
   ```
   pip install -r requirements.txt
   ```

## Estructura del Proyecto

```
usa_covid19_analysis/
│
├── data/
│   ├── raw/
│   └── processed/
├── notebooks/
│   └── covid19_analysis.ipynb
├── src/
│   ├── data/
│   │   ├── collect_data.py
│   │   └── process_data.py
│   ├── visualization/
│   │   └── visualize_data.py
│   └── analysis/
│       └── analyze_data.py
├── reports/
│   └── figures/
├── requirements.txt
└── README.md
```

## Uso

1. Recolecta los datos:
   ```
   python src/data/collect_data.py
   ```

2. Procesa los datos:
   ```
   python src/data/process_data.py
   ```

3. Realiza el análisis:
   ```
   python src/analysis/analyze_data.py
   ```

4. Genera visualizaciones:
   ```
   python src/visualization/visualize_data.py
   ```

## Scripts

- `collect_data.py`: Descarga los datos más recientes de la API de COVID Tracking Project.
- `process_data.py`: Limpia y preprocesa los datos brutos.
- `analyze_data.py`: Realiza análisis estadísticos sobre los datos procesados.
- `visualize_data.py`: Genera gráficos y visualizaciones basados en el análisis.

## Análisis en Jupyter Notebook

Para un análisis interactivo, utiliza el notebook Jupyter:

1. Inicia Jupyter Notebook:
   ```
   jupyter notebook
   ```

2. Abre `notebooks/covid19_analysis.ipynb` en tu navegador.

3. Ejecuta las celdas para realizar el análisis paso a paso.

## Contribuir

Las contribuciones son bienvenidas. Por favor, sigue estos pasos:

1. Haz fork del repositorio.
2. Crea una nueva rama (`git checkout -b feature/AmazingFeature`).
3. Realiza tus cambios y haz commit (`git commit -m 'Add some AmazingFeature'`).
4. Push a la rama (`git push origin feature/AmazingFeature`).
5. Abre un Pull Request.